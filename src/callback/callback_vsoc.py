import logging
import struct
import random
import src.callback.idps_988b_pb2 as idps_pb2

from src.callback.base import Base

logger = logging.getLogger('vsoc')

FIELD_TYPE_DOUBLE = 1
FIELD_TYPE_FLOAT = 2
FIELD_TYPE_INT64 = 3
FIELD_TYPE_UINT64 = 4
FIELD_TYPE_INT32 = 5
FIELD_TYPE_FIXED64 = 6
FIELD_TYPE_FIXED32 = 7
FIELD_TYPE_BOOL = 8
FIELD_TYPE_STRING = 9
FIELD_TYPE_GROUP = 10
FIELD_TYPE_MESSAGE = 11
FIELD_TYPE_BYTES = 12
FIELD_TYPE_UINT32 = 13
FIELD_TYPE_ENUM = 14
FIELD_TYPE_SFIXED32 = 15
FIELD_TYPE_SFIXED64 = 16
FIELD_TYPE_SINT32 = 17
FIELD_TYPE_SINT64 = 18

class CallBack(Base):
    func_map = {
        # "info/base": idps_pb2.InfoBase,
        # "info/error": idps_pb2.RinfoLog,  # 待注释
        # "hstatus/res": idps_pb2.HidsResourceUsage,
        # "hstatus/cpu": idps_pb2.HidsCpuUsage,
        # "hstatus/mem": idps_pb2.HidsMemUsage,
        "hinfo/cpu": idps_pb2.HidsCpuOvldDet,
        # "hinfo/mem": idps_pb2.HidsMemOvldDet,
        # "hinfo/disk": idps_pb2.HidsDiskOvldDet,
        # "hinfo/exe": idps_pb2.HidsAppMonInfo,
        # "hinfo/dport": idps_pb2.HidsDebugPortStaMon,
        # "hinfo/comfile": idps_pb2.HidsFileMon,
        # "hinfo/keyfile": idps_pb2.HidsKeyFileStaDet,
        # "hinfo/folder": idps_pb2.HidsFolderCreateDet,
        # "hinfo/file": idps_pb2.HidsFileIntegrityDet,
        # "hstatus/process": idps_pb2.HidsProcessMonInfo,
        # "hinfo/login": idps_pb2.HidsLoginDet,
        # "hinfo/process": idps_pb2.HidsAbnmlProMon,
        # "hinfo/listprocess": idps_pb2.HidsListProcessDet,
        # "hstatus/flow": idps_pb2.HidsTrafficMon,
        # "hstatus/flowcheck": idps_pb2.HidsTrafficBurstMon,
        # "hstatus/vlanflow": idps_pb2.HidsTraffic,
        # "hinfo/pcap": idps_pb2.HidsPcap,
        # "hstatus/tuple": idps_pb2.HidsTupleData,
        # "hinfo/tcp": idps_pb2.HidsTcpConnDet,
        # "hinfo/udp": idps_pb2.HidsUdpConnDet,
        # "hinfo/log": idps_pb2.HinfoLog,
        # "ninfo/event": idps_pb2.NidsDetectInfo,
        # "ninfo/log": idps_pb2.NinfoLog,
        # "cstatus/load": idps_pb2.CanidsBusLoadDetInfo,
        # "cinfo/message": idps_pb2.CanidsMsgNumInfo,
        # "cinfo/id": idps_pb2.CanIdDetInfo,
        # "cinfo/dlc": idps_pb2.CanidsDlcDetInfo,
        # "cinfo/cycle": idps_pb2.CanidsCycleDetInfo,
        # "cinfo/sequence": idps_pb2.CanidsSeqDetInfo,
        # "cinfo/rms": idps_pb2.CanidsSigValueDetInfo,
        # "cinfo/udscert": idps_pb2.CanidsUdsAccessDetInfo,
        # "cinfo/udslen": idps_pb2.CanidsUdsLenDetInfo,
        # "cinfo/node": idps_pb2.CanidsNodeLossInfo,
        # "cinfo/log": idps_pb2.CaninfoLog
    }

    vehicle_list = ['56EZPWQA', '8JBUK42X', '8JBUPIWF', '56F4B0BT', 'WFEHKPL3', '8JBQ3BXC', '56EUHCKX', '8JBV9VXP']

    def __init__(self):
        self.vehicle_list_len = len(self.vehicle_list) - 1
        self.func_list = list(self.func_map.keys())
        self.func_list_len = len(self.func_list) - 1

    def get_data(self, middleware_type):
        """
        获取当前中间件的消息起始值，并记录当前时间
        {topic, payload, qos, retain, properties}
        """
        if middleware_type == 'emqx':
            vehicle_id = self.get_vehicle_id()
            action = self.get_action()
            return {
                "topic": self.get_random_topic(vehicle_id, action),
                "payload": self.generate_random_proto(action),
            }

    def get_vehicle_id(self):
        return self.vehicle_list[random.randint(0, self.vehicle_list_len)]

    def get_action(self):
        return self.func_list[random.randint(0, self.func_list_len)]

    def get_random_topic(self, vehicle_id, action):
        # print(f"vsoc/v1/SU7/{action}/{vehicle_id}")
        return f"vsoc/v1/SU7/{action}/{vehicle_id}"

    def generate_random_proto(self, action):
        my_message = self.func_map[action]()

        descriptor = self.func_map[action].DESCRIPTOR
        for field in descriptor.fields:
            if field.name == 'controller':
                setattr(my_message, field.name, 64)
                # setattr(my_message, field.name, 128)
            elif field.type == FIELD_TYPE_MESSAGE:
                my_message.msgHeader.protVer = 65535
                my_message.msgHeader.transTimestamp = 1
                my_message.msgHeader.sevTimestamp = 1
                # gps_item = _gps_map[random.randint(0, len(_gps_map) - 1)]
                # my_message.msgHeader.longitude = gps_item[1]
                # my_message.msgHeader.latitude = gps_item[0]
                my_message.msgHeader.longitude = 121
                my_message.msgHeader.latitude = 32
            elif field.type <= FIELD_TYPE_FIXED32 or field.type == FIELD_TYPE_UINT32:
                setattr(my_message, field.name, random.randint(1, 100) * 4096)
            elif field.type == FIELD_TYPE_STRING:
                setattr(my_message, field.name, 'udp flood')
            elif field.type == FIELD_TYPE_BOOL:
                setattr(my_message, field.name, True)
            elif field.type == FIELD_TYPE_BYTES:
                setattr(my_message, field.name, b'udp flood')

        return my_message.SerializeToString()
