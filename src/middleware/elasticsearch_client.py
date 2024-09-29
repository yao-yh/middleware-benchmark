from src.common.global_data import g
from src.middleware.base import Base
import requests
import logging

logger = logging.getLogger('emqx')
logger.setLevel(logging.INFO)


class ElasticsearchClient(Base):
    def __init__(self, callback):
        super().__init__(callback)
        self.config = g.es

    def _get_current_count(self):
        """
        获取es当前的消息数
        可能需要登录
        可能ssl证书不合法

        返回：
        int： 消息数
        """
        response = requests.get(f"{self.config['protocol']}://{self.config['servers']}/{self.config['index']}/_count",
                                auth=(self.config['username'], self.config['password']))
        result_json = response.json()
        return result_json['count'] if 'count' in result_json else 0

if __name__ == "__main__":
    response = requests.get(f"https://elasticsearch.qa4.inchtek.tech/logs_es-*/_count",
                            auth=('elastic','elastic'))
    print(response.text)