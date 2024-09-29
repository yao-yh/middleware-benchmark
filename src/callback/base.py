import time
import logging
logger = logging.getLogger('base')


class Base():
    """
    父类
    用来定义中间件的 消息结构，需要根据支持的中间件并结合业务进行实现

    可重构成员函数：
    get_data: 用于获取中间件的消息数据，根据不同中间件和不同的库，返回格式不同
    send_data: 用于记录测试结束的中间件的消息个数

    """

    def __init__(self):
        pass

    def get_data(self, middleware_type):
        """
        获取当前中间件的消息起始值，并记录当前时间
        """
        if middleware_type == 'emqx':
            return {
                "topic": '',
                "payload": '',
            }

