from src.common.global_data import g
from src.middleware.base import Base
import logging
from confluent_kafka import Consumer, TopicPartition, Producer
# from kafka import KafkaConsumer

import threading

logger = logging.getLogger('kafka')
logger.setLevel(logging.INFO)

message = "{\"asset_id\":3,\"asset_safety_level\":\"0\",\"asset_type\":\"控制器112102\",\"asset_type_id\":2,\"category\":129,\"consumeTime\":2,\"controller\":65,\"device_sn\":\"\",\"getMessageTime\":1701334846213,\"id\":\"17012275323371644029\",\"idsm_code\":\"VIN112100004_1\",\"is_importance\":0,\"logData\":{\"ipDes\":11,\"portDes\":9,\"controller\":65,\"protocol\":16,\"portSrc\":4,\"ipSrc\":8,\"msgHeader\":{\"protver\":111,\"timestamp\":1701227532337}},\"log_type\":\"HidsTupleData\",\"manufacturer\":0,\"model\":\"S1\",\"occur_time\":1701227532337,\"tenant_id\":\"smart\",\"vehicle_id\":8,\"vehicle_model\":\"S1\",\"vehicle_model_id\":3,\"vehicle_safety_level\":\"\",\"vin\":\"VIN112100004\"}"
class KafkaClient(Base):
    type = 'kafka'

    def __init__(self, callback):
        super().__init__(callback)
        self.partitions = []
        self.topic = self.config['topic']
        self.conf = {
            'bootstrap.servers': self.config['servers'],
            'group.id': self.config['group_id'],
            'auto.offset.reset': self.config['offset'],
        }

    def send_message(self, thread_count, message_count):
        """
        发送emqx消息

        参数：
        message_count (int): 消息个数(单线程个数)
        thread_count (int): 线程数
        """
        def publish_messages():
            producer = Producer(self.conf)
            message_value = message
            count= 0
            for i in range(message_count):
                producer.produce(self.topic, value=message_value)
                count += 1
                if  count > 100:
                    count = 0
                    producer.flush()

            producer.flush()

        threads = []
        for _ in range(thread_count):
            thread = threading.Thread(target=publish_messages)
            thread.start()
            threads.append(thread)

        for thread in threads:
            thread.join()

    def _before_get_current_count(self):
        """
        连接kafka consumer。
        """
        self.consumer = Consumer(self.conf)
        self.consumer.assign([TopicPartition(self.topic, self.config['partition'])])

        metadata = self.consumer.list_topics(topic=self.topic, timeout=10)
        partitions = metadata.topics[self.topic].partitions if self.topic in metadata.topics else []
        self.partitions = [partitions[index].id for index in partitions]

    def _get_current_count(self):
        """
        获取kafka的最大offset。

        返回：
        int： 最大offset
        """
        offset_sum = 0
        for index in self.partitions:
            partition_index = self.partitions[index]
            partition = TopicPartition(self.topic, partition_index)
            self.consumer.assign([partition])

            # self.consumer.offsets_for_times([partition])
            watermark_offsets = self.consumer.get_watermark_offsets(partition)

            offset_sum += int(watermark_offsets[1]) if watermark_offsets else 0

        logger.info(f'kafka offset: {offset_sum}')

        return offset_sum

    def _after_get_current_count(self):
        """
        关闭kafka consumer。
        """
        self.consumer.close()

if __name__ == "__main__":
    import time
    topic = 'topic1'
    consumer = Consumer({
        "bootstrap.servers": "10.100.64.78:9094,10.100.64.79:9094",
        "group.id": "test_group_id"

    })
    partition = TopicPartition(topic, 0)
    consumer.assign([partition])
    kafka = KafkaClient()
    for i in range(1000):
        kafka.send_message(1, 1)
        time.sleep(1)

    consumer.close()
