import time

# from case.config import SECOND_WAIT
from config import *
import threading
import logging
logger = logging.getLogger('base')
from src.common.global_data import g


class Base(threading.Thread):
    """
    父类
    部分中间件只支持获取当前消息总数
    所以需要一个起始值和一个结束值，计算差值作为真实消息个数

    成员变量：
    client_start_count: 用于记录测试开始的中间件的消息个数
    client_end_count: 用于记录测试结束的中间件的消息个数
    client_start_time: 用于记录首条消息的生成时间
    client_end_time: 用于记录最后一条消息的生成时间

    """
    type = 'base'

    def __init__(self, callback):
        super().__init__()
        self.callback = callback
        self.config = g.config[self.type]

        self.client_start_count = 0
        self.client_end_count = 0
        self.client_start_time = 0
        self.client_end_time = 0

    def init(self):
        """
        获取当前中间件的消息起始值，并记录当前时间
        """
        self.client_start_count, self.client_start_time = self.get_current_count(0)

    def run(self):
        self.client_end_count, self.client_end_time = self.get_current_count(SECOND_WAIT)

    def get_timestamp(self):
        return int(time.time() * 1000)

    def get_message_count(self):
        logger.info(f'type: {self.type}, client_end_count: {self.client_end_count}, client_start_count: {self.client_start_count}')
        return self.client_end_count - self.client_start_count

    def get_test_time(self):
        return self.client_start_time, self.client_end_time

    def get_current_count(self, timer):
        """
        获取当前中间件的消息个数。

        参数：
        timer (int):  此参数做为等待时间，单位为毫秒
                      由于服务处理有延迟，需要轮询监听中间件消息个数
                      例：timer为1000。需要连续1秒内，中间件消息个数不变，视为真实的消息个数

        返回：
        int: 当前消息数
        int: 当前时间（毫秒）
        """
        self._before_get_current_count()

        time_start = self.get_timestamp()
        current_count_bak = 0
        while True:
            try:
                time_now = self.get_timestamp()
                current_count = self._get_current_count()
                if current_count and current_count != current_count_bak:
                    current_count_bak = current_count
                    time_start = time_now
                if time_now >= time_start + timer:
                    self._after_get_current_count()
                    return current_count, time_start
                time.sleep(0.3)
            except Exception as e:
                logger.error('error')
                logger.error(e)

    def _get_current_count(self):
        """
        和中间件交互，获取当前个数的实现函数
        需要子类重写实现。

        返回：
        int: 当前消息数
        """
        return 0

    def _before_get_current_count(self):
        """
        和中间件交互前的准备工作的实现函数
        需要子类重写实现。
        """
        pass

    def _after_get_current_count(self):
        """
        和中间件交互后的释放资源的实现函数
        需要子类重写实现。
        """
        pass

    def send_message(self, thread_count, message_count):
        """
        向中间件发送消息的实现函数
        需要子类重写实现。

        参数：
        message_count (int): 消息个数(单线程个数)
        thread_count (int): 线程数
        """
        pass

    def get_message(self):
        """
        向中间件发送消息的实现函数
        需要子类重写实现。

        参数：
        message_count (int): 消息个数(单线程个数)
        thread_count (int): 线程数
        """
        return self.callback.get_data(self.type)
