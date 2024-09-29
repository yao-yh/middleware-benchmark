from src.middleware.base import Base
from config import *
import requests
import logging
import paho.mqtt.client as mqtt
import json
import base64
import threading
import multiprocessing


logger = logging.getLogger('emqx')
logger.setLevel(logging.INFO)


class EmqxClient(Base):
    type = 'emqx'
    def __init__(self, callback):
        super().__init__(callback)
        self.base_url = self.config['api_url']
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': "Basic " + base64.b64encode(
                f"{self.config['api_key']}:{self.config['api_secret']}".encode()).decode()
        }

    def send_message(self, thread_count, message_count):
        """
        发送emqx消息

        参数：
        message_count (int): 消息个数(单线程个数)
        thread_count (int): 线程数
        """
        def publish_messages(index):
            client = mqtt.Client()
            client.connect(self.config['server_address'], self.config['server_port'], 60)
            # client.loop_start()
            message_count_part = message_count // 10
            for count in range(message_count):
                client.publish(**self.get_message())
                count += 1
                if count >= message_count_part:
                    message_count_part += message_count // 10
                    logger.info(f"{index} 已发送消息数: {count}")
            # client.loop_stop()

        threads = []
        for index in range(thread_count):
            thread = threading.Thread(target=publish_messages, args=(index,))
            thread.start()
            threads.append(thread)
            # p = multiprocessing.Process(target=publish_messages, args=())
            # threads.append(p)
            # p.start()  # 启动进程

        for thread in threads:
            thread.join()


    def _send_api(self):
        """
        获取emqx当前的消息数
        通过api topic_metrics实现
        调用前需要先创建，否则提示错误

        返回：
        int： 消息数
        """
        response = requests.get(f'{self.base_url}', headers=self.headers)
        data = json.loads(response.text)
        return data.get('messages.received', 0)

    def _get_current_count(self):
        return self._send_api()

if __name__ == "__main__":
    # response = requests.get(f'{self.base_url}/{emqx_topic.replace("/", "%2F")}', headers=self.headers)
    response = requests.get("http://10.100.64.214:31084/api/v5/mqtt/topic_metrics/vsoc%2Fv1%2FS1%2Fhstatus%2Ftuple%2FVIN112100004", auth=('e4bf2f2b0806872e', 'oVy0MiL4UlAX9CRSRMdCBlOrFQ8TIuWB2RHOdBHhJG5P'))
    print(response.text)
    # response = requests.delete("http://10.100.64.214:31084/api/v5/mqtt/topic_metrics/vsoc%2Fv1%2FS1%2Fhstatus%2Ftuple%2FVIN112100004", auth=('e4bf2f2b0806872e', 'oVy0MiL4UlAX9CRSRMdCBlOrFQ8TIuWB2RHOdBHhJG5P'))
