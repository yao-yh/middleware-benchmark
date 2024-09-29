emqx_message = b'\n\t\x08o\x10\xb1\xa0\xc0\xc8\xc11\x10A\x18\x08 \x0b(\x040\t8\x10'
emqx_topic = "vsoc/v1/S1/hstatus/tuple/VIN112100004"
SECOND_WAIT = 10000

# config_file = "config/env/dev.yaml"
# namespace_dev = "qa4-dev"
# env = 'qa4'
namespace_dev = "qa3-dev"
env = 'qa3'
config_file = "config/env/dev-v1.24.yaml"

base_logstash_service = {
    "type": "none",
    "namespace": namespace_dev,
    "container": "logstash",
    "replicas": 3,
    "cpu_reservation": '1',
    "cpu_limit": '1',
    "mem_reservation": '1Gi',
    "mem_limit": '1Gi',
}
base_emqx_service = {
    "type": "statefulset",
    "namespace": 'ops',
    "container": "emqx",
    "replicas": 3,
    "cpu_reservation": '2',
    "cpu_limit": '2',
    "mem_reservation": '2Gi',
    "mem_limit": '2Gi',
}
base_iot_service = {
    "type": "deploy",
    "namespace": namespace_dev,
    "container": "iot-device-manager",
    "replicas": 1,
    "cpu_reservation": '200m',
    "cpu_limit": '1',
    "mem_reservation": '1Gi',
    "mem_limit": '1Gi',
}

# 'limits': {'cpu': '1', 'memory': '1Gi'},
# 'requests': {'cpu': '200m', 'memory': '1Gi'}}
# "client_list": ['emqx', 'kafka', 'kafka2'],
# "client_list": ['emqx', 'kafka', 'kafka2', 'elasticsearch'],
# "iot-device-manager": {**base_iot_service, **{"replicas": 1}}

case_list = [
    {
        "case_name": "iotdevicemanager 单节点 动态调整 cpu_reservation",
        "throughput": 10000,
        "thread_count": 2,
        "client_list": ['emqx', 'kafka'],
        "config_file": config_file,
        "service_list": {
            "emqx": {**base_emqx_service},
            "logstash": {**base_logstash_service},
            "iot-device-manager": {**base_iot_service, **{"cpu_reservation": '200m'}}
        },
    },
    {
        "case_name": "iotdevicemanager 单节点 动态调整 cpu_reservation",
        "throughput": 10000,
        "thread_count": 2,
        "client_list": ['emqx', 'kafka'],
        "config_file": config_file,
        "service_list": {
            "logstash": {**base_logstash_service},
            "emqx": {**base_emqx_service},
            "iot-device-manager": {**base_iot_service, **{"cpu_reservation": '300m'}}
        },
    },
    {
        "case_name": "iotdevicemanager 单节点 动态调整 cpu_reservation",
        "throughput": 10000,
        "thread_count": 2,
        "client_list": ['emqx', 'kafka'],
        "config_file": config_file,
        "service_list": {
            "logstash": {**base_logstash_service},
            "emqx": {**base_emqx_service},
            "iot-device-manager": {**base_iot_service, **{"cpu_reservation": '400m'}}
        },
    },
    {
        "case_name": "iotdevicemanager 单节点 动态调整 cpu_reservation",
        "throughput": 10000,
        "thread_count": 2,
        "client_list": ['emqx', 'kafka'],
        "config_file": config_file,
        "service_list": {
            "logstash": {**base_logstash_service},
            "emqx": {**base_emqx_service},
            "iot-device-manager": {**base_iot_service, **{"cpu_reservation": '500m'}}
        },
    },
    {
        "case_name": "iotdevicemanager 单节点 动态调整 cpu_reservation",
        "throughput": 10000,
        "thread_count": 2,
        "client_list": ['emqx', 'kafka'],
        "config_file": config_file,
        "service_list": {
            "logstash": {**base_logstash_service},
            "emqx": {**base_emqx_service},
            "iot-device-manager": {**base_iot_service, **{"cpu_reservation": '600m'}}
        },
    },
    {
        "case_name": "iotdevicemanager 单节点 动态调整 cpu_reservation",
        "throughput": 10000,
        "thread_count": 2,
        "client_list": ['emqx', 'kafka'],
        "config_file": config_file,
        "service_list": {
            "logstash": {**base_logstash_service},
            "emqx": {**base_emqx_service},
            "iot-device-manager": {**base_iot_service, **{"cpu_reservation": '700m'}}
        },
    },
    {
        "case_name": "iotdevicemanager 单节点 动态调整 cpu_reservation",
        "throughput": 10000,
        "thread_count": 2,
        "client_list": ['emqx', 'kafka'],
        "config_file": config_file,
        "service_list": {
            "logstash": {**base_logstash_service},
            "emqx": {**base_emqx_service},
            "iot-device-manager": {**base_iot_service, **{"cpu_reservation": '800m'}}
        },
    },
    {
        "case_name": "iotdevicemanager 单节点 动态调整 cpu_reservation",
        "throughput": 10000,
        "thread_count": 2,
        "client_list": ['emqx', 'kafka'],
        "config_file": config_file,
        "service_list": {
            "logstash": {**base_logstash_service},
            "emqx": {**base_emqx_service},
            "iot-device-manager": {**base_iot_service, **{"cpu_reservation": '900m'}}
        },
    },
    {
        "case_name": "iotdevicemanager 单节点 动态调整 cpu_reservation",
        "throughput": 10000,
        "thread_count": 2,
        "client_list": ['emqx', 'kafka'],
        "config_file": config_file,
        "service_list": {
            "logstash": {**base_logstash_service},
            "emqx": {**base_emqx_service},
            "iot-device-manager": {**base_iot_service, **{"cpu_reservation": '1'}}
        },
    },
    {
        "case_name": "iotdevicemanager 单节点 动态调整 cpu_limit",
        "throughput": 10000,
        "thread_count": 2,
        "client_list": ['emqx', 'kafka'],
        "config_file": config_file,
        "service_list": {
            "logstash": {**base_logstash_service},
            "emqx": {**base_emqx_service},
            "iot-device-manager": {**base_iot_service, **{"cpu_limit": '200m'}}
        },
    },
    {
        "case_name": "iotdevicemanager 单节点 动态调整 cpu_limit",
        "throughput": 10000,
        "thread_count": 2,
        "client_list": ['emqx', 'kafka'],
        "config_file": config_file,
        "service_list": {
            "logstash": {**base_logstash_service},
            "emqx": {**base_emqx_service},
            "iot-device-manager": {**base_iot_service, **{"cpu_limit": '300m'}}
        },
    },
    {
        "case_name": "iotdevicemanager 单节点 动态调整 cpu_limit",
        "throughput": 10000,
        "thread_count": 2,
        "client_list": ['emqx', 'kafka'],
        "config_file": config_file,
        "service_list": {
            "logstash": {**base_logstash_service},
            "emqx": {**base_emqx_service},
            "iot-device-manager": {**base_iot_service, **{"cpu_limit": '400m'}}
        },
    },
    {
        "case_name": "iotdevicemanager 单节点 动态调整 cpu_limit",
        "throughput": 10000,
        "thread_count": 2,
        "client_list": ['emqx', 'kafka'],
        "config_file": config_file,
        "service_list": {
            "logstash": {**base_logstash_service},
            "emqx": {**base_emqx_service},
            "iot-device-manager": {**base_iot_service, **{"cpu_limit": '500m'}}
        },
    },
    {
        "case_name": "iotdevicemanager 单节点 动态调整 cpu_limit",
        "throughput": 10000,
        "thread_count": 2,
        "client_list": ['emqx', 'kafka'],
        "config_file": config_file,
        "service_list": {
            "logstash": {**base_logstash_service},
            "emqx": {**base_emqx_service},
            "iot-device-manager": {**base_iot_service, **{"cpu_limit": '600m'}}
        },
    },
    {
        "case_name": "iotdevicemanager 单节点 动态调整 cpu_limit",
        "throughput": 10000,
        "thread_count": 2,
        "client_list": ['emqx', 'kafka'],
        "config_file": config_file,
        "service_list": {
            "logstash": {**base_logstash_service},
            "emqx": {**base_emqx_service},
            "iot-device-manager": {**base_iot_service, **{"cpu_limit": '700m'}}
        },
    },
    {
        "case_name": "iotdevicemanager 单节点 动态调整 cpu_limit",
        "throughput": 10000,
        "thread_count": 2,
        "client_list": ['emqx', 'kafka'],
        "config_file": config_file,
        "service_list": {
            "logstash": {**base_logstash_service},
            "emqx": {**base_emqx_service},
            "iot-device-manager": {**base_iot_service, **{"cpu_limit": '800m'}}
        },
    },
    {
        "case_name": "iotdevicemanager 单节点 动态调整 cpu_limit",
        "throughput": 10000,
        "thread_count": 2,
        "client_list": ['emqx', 'kafka'],
        "config_file": config_file,
        "service_list": {
            "logstash": {**base_logstash_service},
            "emqx": {**base_emqx_service},
            "iot-device-manager": {**base_iot_service, **{"cpu_limit": '900m'}}
        },
    },
    {
        "case_name": "iotdevicemanager 单节点 动态调整 cpu_limit",
        "throughput": 10000,
        "thread_count": 2,
        "client_list": ['emqx', 'kafka'],
        "config_file": config_file,
        "service_list": {
            "logstash": {**base_logstash_service},
            "emqx": {**base_emqx_service},
            "iot-device-manager": {**base_iot_service, **{"cpu_limit": '1'}}
        },
    },
    {
        "case_name": "iotdevicemanager 单节点 动态调整 cpu_limit",
        "throughput": 10000,
        "thread_count": 2,
        "client_list": ['emqx', 'kafka'],
        "config_file": config_file,
        "service_list": {
            "logstash": {**base_logstash_service},
            "emqx": {**base_emqx_service},
            "iot-device-manager": {**base_iot_service, **{"cpu_limit": '1100m'}}
        },
    },
    {
        "case_name": "iotdevicemanager 单节点 动态调整 cpu_limit",
        "throughput": 10000,
        "thread_count": 2,
        "client_list": ['emqx', 'kafka'],
        "config_file": config_file,
        "service_list": {
            "logstash": {**base_logstash_service},
            "emqx": {**base_emqx_service},
            "iot-device-manager": {**base_iot_service, **{"cpu_limit": '1200m'}}
        },
    },
    {
        "case_name": "iotdevicemanager 单节点 动态调整 cpu_limit",
        "throughput": 10000,
        "thread_count": 2,
        "client_list": ['emqx', 'kafka'],
        "config_file": config_file,
        "service_list": {
            "logstash": {**base_logstash_service},
            "emqx": {**base_emqx_service},
            "iot-device-manager": {**base_iot_service, **{"cpu_limit": '1300m'}}
        },
    },
    {
        "case_name": "iotdevicemanager 单节点 动态调整 cpu_limit",
        "throughput": 10000,
        "thread_count": 2,
        "client_list": ['emqx', 'kafka'],
        "config_file": config_file,
        "service_list": {
            "logstash": {**base_logstash_service},
            "emqx": {**base_emqx_service},
            "iot-device-manager": {**base_iot_service, **{"cpu_limit": '1400m'}}
        },
    },
    {
        "case_name": "iotdevicemanager 单节点 动态调整 cpu_limit",
        "throughput": 10000,
        "thread_count": 2,
        "client_list": ['emqx', 'kafka'],
        "config_file": config_file,
        "service_list": {
            "logstash": {**base_logstash_service},
            "emqx": {**base_emqx_service},
            "iot-device-manager": {**base_iot_service, **{"cpu_limit": '1500m'}}
        },
    },
    {
        "case_name": "iotdevicemanager 单节点 动态调整 cpu_limit",
        "throughput": 10000,
        "thread_count": 2,
        "client_list": ['emqx', 'kafka'],
        "config_file": config_file,
        "service_list": {
            "logstash": {**base_logstash_service},
            "emqx": {**base_emqx_service},
            "iot-device-manager": {**base_iot_service, **{"cpu_limit": '1600m'}}
        },
    }
]