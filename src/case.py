from src.common.global_data import g
from src.common.result import save_to__result
from src.middleware.kafka_client import KafkaClient
from src.middleware.emqx_client import EmqxClient
from src.middleware.elasticsearch_client import ElasticsearchClient

from k8s_ctrl import Kubernetes
from config import *
import datetime

import time
from openpyxl import load_workbook
import logging
logger = logging.getLogger('case')

class_map = {
    'emqx': EmqxClient,
    'kafka': KafkaClient,
    'kafka2': KafkaClient,
    # 'elasticsearch': ElasticsearchClient,
}


class CaseTest:
    kafka_client = None
    kafka1_client = None
    emqx_client = None
    elasticsearch_client = None

    test_start_time = 0

    emqx_message_count = 0
    emqx_start_time = 0
    emqx_end_time = 0

    kafka_message_count = 0
    kafka_start_time = 0
    kafka_end_time = 0

    kafka2_message_count = 0
    kafka2_start_time = 0
    kafka2_end_time = 0

    elasticsearch_message_count = 0
    elasticsearch_start_time = 0
    elasticsearch_end_time = 0

    def __init__(self, case_data, callback):
        self.callback = callback
        self.case_data = case_data
        self.client_list = self.case_data['client_list']

    def print_result(self):
        # 分析测试结果
        service_list = ['iot-device-manager', 'emqx', 'logstash']
        service_list = []

        for key in self.client_list:
            attr_key = f'{key}_message_count'
            if getattr(self, attr_key) == 0:
                setattr(self, attr_key, 0)

        all_test_time = round((getattr(self, f'{self.client_list[-1]}_end_time') - self.test_start_time) / 1000, 2)

        def get_time_string(timestamp_current):
            return datetime.datetime.fromtimestamp(timestamp_current / 1000.0).strftime('%Y-%m-%d %H:%M:%S.%f')

        logger.info(f"测试开始时间： {get_time_string(self.test_start_time)}")
        logger.info(f"总测试时长： {all_test_time} s")

        for key in self.client_list:
            logger.info(f"{key} 消息个数： {getattr(self, f'{key}_message_count')}")
            logger.info(f"{key} 消息个数停止更新时间： {get_time_string(getattr(self, f'{key}_end_time'))}")

        for index in range(len(self.client_list)):
            if index == 0:
                continue
            key1 = self.client_list[index - 1]
            key2 = self.client_list[index]
            lost_count = getattr(self, f'{key1}_message_count') - getattr(self, f'{key2}_message_count')
            lost = round((lost_count / getattr(self, f'{key1}_message_count')) * 100, 2)

            logger.info(f"{key2} 消息丢失： {lost} %")

        for index in range(len(self.client_list)):
            if index == 0:
                continue
            key1 = self.client_list[index - 1]
            key2 = self.client_list[index]
            delay = getattr(self, f'{key2}_end_time') - getattr(self, f'{key1}_end_time')
            denominator = getattr(self, f'{key2}_message_count')
            if denominator:
                arv_delay = round(delay / denominator, 5)
            else:
                arv_delay = '-'

            logger.info(f"{key2} 最大时延： {round(delay / 1000, 2)} s")
            logger.info(f"{key2} 平均时延（仅供参考）： {arv_delay} ms")

        for key in self.client_list:
            test_time = getattr(self, f'{key}_end_time') - self.test_start_time
            throughput = round( getattr(self, f'{key}_message_count') / test_time * 1000, 2)

            logger.info(f"{key} 吞吐： {throughput} /s")

        row_result = [self.case_data['case_name'], get_time_string(self.test_start_time), all_test_time]

        for key in service_list:
            if key in self.case_data['service_list']:
                config = self.case_data['service_list'][key]
                row_result = row_result + [config['cpu_reservation'], config['cpu_limit'], config['mem_reservation'], config['mem_limit'], config['replicas']]
            else:
                row_result = row_result + ['-' for _ in range(5)]

        for key in class_map.keys():
            if hasattr(self, f'{key}_message_count'):
                row_result.append(getattr(self, f'{key}_message_count'))
                row_result.append(get_time_string(getattr(self, f'{key}_end_time')))
            if key == 'mqtt':
                continue
            if key not in self.client_list:
                row_result = row_result + ['-' for _ in range(3)]
                continue
            last_index = self.client_list.index(key) - 1
            if last_index < 0:
                row_result = row_result + ['-' for _ in range(3)]
                continue
            last_key = self.client_list[last_index]

            lost_count = getattr(self, f'{last_key}_message_count') - getattr(self, f'{key}_message_count')
            lost = round((lost_count / getattr(self, f'{last_key}_message_count')) * 100, 2)
            delay = getattr(self, f'{key}_end_time') - getattr(self, f'{last_key}_end_time')
            denominator = getattr(self, f'{key}_message_count')
            if denominator:
                arv_delay = round(delay / denominator, 5)
            else:
                arv_delay = '-'

            row_result.append(lost)
            row_result.append(round(delay / 1000, 2))
            row_result.append(arv_delay)

        for key in class_map.keys():
            if hasattr(self, f'{key}_message_count'):
                test_time = getattr(self, f'{key}_end_time') - self.test_start_time
                throughput = round(getattr(self, f'{key}_message_count') / test_time * 1000, 2)
                row_result.append(throughput)
            else:
                row_result.append('-')

        save_to__result(row_result)

    def init_all_client(self):
        """
        初始化所有中间件
        """
        for key in self.client_list:
            client = class_map[key](self.callback)
            client.init()
            logger.info(f"{key}_client init success")

            # hasattr(self, f'{key}_client')
            setattr(self, f'{key}_client', client)
            time.sleep(1)

    def start_all_client(self):
        """
        启动所有中间件，去查询各自的消息个数
        """
        for key in self.client_list:
            client = getattr(self, f'{key}_client')
            client.start()
            logger.info(f"{key}_client start success")

    def join_all_client(self):
        """
        等待所有中间件获取消息成功
        """
        for key in self.client_list:
            client = getattr(self, f'{key}_client')
            if client.is_alive():
                client.join(SECOND_WAIT * 2)
            message_count = client.get_message_count()
            start_time, end_time = client.get_test_time()
            setattr(self, f'{key}_message_count', message_count)
            setattr(self, f'{key}_start_time', start_time)
            setattr(self, f'{key}_end_time', end_time)
            logger.info(f"{key}_client end")

    def send_message(self):
        """
        发送消息
        只支持一个中间件作为消息的生产者
        轮询中间件，只要有一个发送成功，就退出
        """

        self.test_start_time = int(time.time() * 1000)

        for key in self.client_list:
            logger.info(f"{key}_client send message")
            client = getattr(self, f'{key}_client')
            client.send_message(self.case_data['thread_count'], self.case_data['throughput'])
            return

    def init_env(self):
        """
        初始化k8s换进
        """
        return
        a = Kubernetes(self.case_data)
        a.edit_all()

    def start(self):
        self.init_env()
        self.init_all_client()

        self.start_all_client()
        self.send_message()
        self.join_all_client()

        self.print_result()
        logger.info(f"end")

