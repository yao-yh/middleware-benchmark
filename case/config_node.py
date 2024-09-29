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
    "cpu_reservation": '6',
    "cpu_limit": '6',
    "mem_reservation": '6Gi',
    "mem_limit": '6Gi',
}
base_iot_service = {
    "type": "deploy",
    "namespace": namespace_dev,
    "container": "iot-device-manager",
    "replicas": 1,
    "cpu_reservation": '300m',
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
        "throughput": 50000,
        "thread_count": 10,
        "client_list": ['emqx', 'kafka'],
        "config_file": config_file,
        "service_list": {
            "emqx": {**base_emqx_service},
            "logstash": {**base_logstash_service},
            "iot-device-manager": {**base_iot_service, **{"replicas": 1}}
        },
    }, {
        "case_name": "iotdevicemanager 单节点 动态调整 cpu_reservation",
        "throughput": 50000,
        "thread_count": 10,
        "client_list": ['emqx', 'kafka'],
        "config_file": config_file,
        "service_list": {
            "emqx": {**base_emqx_service},
            "logstash": {**base_logstash_service},
            "iot-device-manager": {**base_iot_service, **{"replicas": 2}}
        },
    }, {
        "case_name": "iotdevicemanager 单节点 动态调整 cpu_reservation",
        "throughput": 50000,
        "thread_count": 10,
        "client_list": ['emqx', 'kafka'],
        "config_file": config_file,
        "service_list": {
            "emqx": {**base_emqx_service},
            "logstash": {**base_logstash_service},
            "iot-device-manager": {**base_iot_service, **{"replicas": 3}}
        },
    }, {
        "case_name": "iotdevicemanager 单节点 动态调整 cpu_reservation",
        "throughput": 50000,
        "thread_count": 10,
        "client_list": ['emqx', 'kafka'],
        "config_file": config_file,
        "service_list": {
            "emqx": {**base_emqx_service},
            "logstash": {**base_logstash_service},
            "iot-device-manager": {**base_iot_service, **{"replicas": 4}}
        },
    }, {
        "case_name": "iotdevicemanager 单节点 动态调整 cpu_reservation",
        "throughput": 50000,
        "thread_count": 10,
        "client_list": ['emqx', 'kafka'],
        "config_file": config_file,
        "service_list": {
            "emqx": {**base_emqx_service},
            "logstash": {**base_logstash_service},
            "iot-device-manager": {**base_iot_service, **{"replicas": 5}}
        },
    }, {
        "case_name": "iotdevicemanager 单节点 动态调整 cpu_reservation",
        "throughput": 50000,
        "thread_count": 10,
        "client_list": ['emqx', 'kafka'],
        "config_file": config_file,
        "service_list": {
            "emqx": {**base_emqx_service},
            "logstash": {**base_logstash_service},
            "iot-device-manager": {**base_iot_service, **{"replicas": 6}}
        },
    }, {
        "case_name": "iotdevicemanager 单节点 动态调整 cpu_reservation",
        "throughput": 50000,
        "thread_count": 10,
        "client_list": ['emqx', 'kafka'],
        "config_file": config_file,
        "service_list": {
            "emqx": {**base_emqx_service},
            "logstash": {**base_logstash_service},
            "iot-device-manager": {**base_iot_service, **{"replicas": 7}}
        },
    }, {
        "case_name": "iotdevicemanager 单节点 动态调整 cpu_reservation",
        "throughput": 50000,
        "thread_count": 10,
        "client_list": ['emqx', 'kafka'],
        "config_file": config_file,
        "service_list": {
            "emqx": {**base_emqx_service},
            "logstash": {**base_logstash_service},
            "iot-device-manager": {**base_iot_service, **{"replicas": 8}}
        },
    }, {
        "case_name": "iotdevicemanager 单节点 动态调整 cpu_reservation",
        "throughput": 50000,
        "thread_count": 10,
        "client_list": ['emqx', 'kafka'],
        "config_file": config_file,
        "service_list": {
            "emqx": {**base_emqx_service},
            "logstash": {**base_logstash_service},
            "iot-device-manager": {**base_iot_service, **{"replicas": 9}}
        },
    }, {
        "case_name": "iotdevicemanager 单节点 动态调整 cpu_reservation",
        "throughput": 50000,
        "thread_count": 10,
        "client_list": ['emqx', 'kafka'],
        "config_file": config_file,
        "service_list": {
            "emqx": {**base_emqx_service},
            "logstash": {**base_logstash_service},
            "iot-device-manager": {**base_iot_service, **{"replicas": 10}}
        },
    }
]

case_list = [
    {
        "case_name": "emqx 1Core 6G 单节点",
        "throughput": 100000,
        "thread_count": 3,
        "client_list": ['emqx', 'kafka'],
        "config_file": config_file,
        "service_list": {
            "emqx": {**base_emqx_service},
            "logstash": {**base_logstash_service},
            "iot-device-manager": {**base_iot_service}
        },
    },
    {
        "case_name": "emqx 2Core 6G 单节点",
        "throughput": 100000,
        "thread_count": 3,
        "client_list": ['emqx', 'kafka'],
        "config_file": config_file,
        "service_list": {
            "emqx": {**base_emqx_service, **{"cpu_reservation": '2', "cpu_limit": '2'}},
            "logstash": {**base_logstash_service},
            "iot-device-manager": {**base_iot_service}
        },
    },
    {
        "case_name": "emqx 3Core 6G 单节点",
        "throughput": 100000,
        "thread_count": 3,
        "client_list": ['emqx', 'kafka'],
        "config_file": config_file,
        "service_list": {
            "emqx": {**base_emqx_service, **{"cpu_reservation": '3', "cpu_limit": '3'}},
            "logstash": {**base_logstash_service},
            "iot-device-manager": {**base_iot_service}
        },
    },
    {
        "case_name": "emqx 4Core 6G 单节点",
        "throughput": 100000,
        "thread_count": 3,
        "client_list": ['emqx', 'kafka'],
        "config_file": config_file,
        "service_list": {
            "emqx": {**base_emqx_service, **{"cpu_reservation": '4', "cpu_limit": '4'}},
            "logstash": {**base_logstash_service},
            "iot-device-manager": {**base_iot_service}
        },
    },
    {
        "case_name": "emqx 5Core 6G 单节点",
        "throughput": 100000,
        "thread_count": 3,
        "client_list": ['emqx', 'kafka'],
        "config_file": config_file,
        "service_list": {
            "emqx": {**base_emqx_service, **{"cpu_reservation": '5', "cpu_limit": '5'}},
            "logstash": {**base_logstash_service},
            "iot-device-manager": {**base_iot_service}
        },
    },
    {
        "case_name": "emqx 6Core 6G 单节点",
        "throughput": 100000,
        "thread_count": 3,
        "client_list": ['emqx', 'kafka'],
        "config_file": config_file,
        "service_list": {
            "emqx": {**base_emqx_service, **{"cpu_reservation": '6', "cpu_limit": '6'}},
            "logstash": {**base_logstash_service},
            "iot-device-manager": {**base_iot_service}
        },
    },
    {
        "case_name": "emqx 7Core 6G 单节点",
        "throughput": 100000,
        "thread_count": 3,
        "client_list": ['emqx', 'kafka'],
        "config_file": config_file,
        "service_list": {
            "emqx": {**base_emqx_service, **{"cpu_reservation": '7', "cpu_limit": '7'}},
            "logstash": {**base_logstash_service},
            "iot-device-manager": {**base_iot_service}
        },
    }
]


case_list = [
    {
        "case_name": "emqx 1G 6Core 单节点",
        "throughput": 100000,
        "thread_count": 3,
        "client_list": ['emqx', 'kafka'],
        "config_file": config_file,
        "service_list": {
            "emqx": {**base_emqx_service, **{"mem_reservation": '1Gi', "mem_limit": '1Gi'}},
            "logstash": {**base_logstash_service},
            "iot-device-manager": {**base_iot_service}
        },
    },
    {
        "case_name": "emqx 2G 6Core 单节点",
        "throughput": 100000,
        "thread_count": 3,
        "client_list": ['emqx', 'kafka'],
        "config_file": config_file,
        "service_list": {
            "emqx": {**base_emqx_service, **{"mem_reservation": '2Gi', "mem_limit": '2Gi'}},
            "logstash": {**base_logstash_service},
            "iot-device-manager": {**base_iot_service}
        },
    },
    {
        "case_name": "emqx 3G 6Core 单节点",
        "throughput": 100000,
        "thread_count": 3,
        "client_list": ['emqx', 'kafka'],
        "config_file": config_file,
        "service_list": {
            "emqx": {**base_emqx_service, **{"mem_reservation": '3Gi', "mem_limit": '3Gi'}},
            "logstash": {**base_logstash_service},
            "iot-device-manager": {**base_iot_service}
        },
    },
    {
        "case_name": "emqx 4G 6Core 单节点",
        "throughput": 100000,
        "thread_count": 3,
        "client_list": ['emqx', 'kafka'],
        "config_file": config_file,
        "service_list": {
            "emqx": {**base_emqx_service, **{"mem_reservation": '4Gi', "mem_limit": '4Gi'}},
            "logstash": {**base_logstash_service},
            "iot-device-manager": {**base_iot_service}
        },
    },
    {
        "case_name": "emqx 5G 6Core 单节点",
        "throughput": 100000,
        "thread_count": 3,
        "client_list": ['emqx', 'kafka'],
        "config_file": config_file,
        "service_list": {
            "emqx": {**base_emqx_service, **{"mem_reservation": '5Gi', "mem_limit": '5Gi'}},
            "logstash": {**base_logstash_service},
            "iot-device-manager": {**base_iot_service}
        },
    },
    {
        "case_name": "emqx 6G 6Core 单节点",
        "throughput": 100000,
        "thread_count": 3,
        "client_list": ['emqx', 'kafka'],
        "config_file": config_file,
        "service_list": {
            "emqx": {**base_emqx_service, **{"mem_reservation": '6Gi', "mem_limit": '6Gi'}},
            "logstash": {**base_logstash_service},
            "iot-device-manager": {**base_iot_service}
        },
    },
    {
        "case_name": "emqx 7G 6Core 单节点",
        "throughput": 100000,
        "thread_count": 3,
        "client_list": ['emqx', 'kafka'],
        "config_file": config_file,
        "service_list": {
            "emqx": {**base_emqx_service, **{"mem_reservation": '7Gi', "mem_limit": '7Gi'}},
            "logstash": {**base_logstash_service},
            "iot-device-manager": {**base_iot_service}
        },
    }
]


case_list = [
    {
        "case_name": "emqx 3G 3Core 单节点",
        "throughput": 100000,
        "thread_count": 3,
        "client_list": ['emqx', 'kafka'],
        "config_file": config_file,
        "service_list": {
            "emqx": {**base_emqx_service, **{"replicas": 1}},
            "logstash": {**base_logstash_service},
            "iot-device-manager": {**base_iot_service}
        },
    },
    {
        "case_name": "emqx 3G 3Core 2节点",
        "throughput": 100000,
        "thread_count": 3,
        "client_list": ['emqx', 'kafka'],
        "config_file": config_file,
        "service_list": {
            "emqx": {**base_emqx_service, **{"replicas": 2}},
            "logstash": {**base_logstash_service},
            "iot-device-manager": {**base_iot_service}
        },
    },
    {
        "case_name": "emqx 3G 3Core 3节点",
        "throughput": 100000,
        "thread_count": 3,
        "client_list": ['emqx', 'kafka'],
        "config_file": config_file,
        "service_list": {
            "emqx": {**base_emqx_service, **{"replicas": 3}},
            "logstash": {**base_logstash_service},
            "iot-device-manager": {**base_iot_service}
        },
    },
    {
        "case_name": "emqx 3G 3Core 4节点",
        "throughput": 100000,
        "thread_count": 3,
        "client_list": ['emqx', 'kafka'],
        "config_file": config_file,
        "service_list": {
            "emqx": {**base_emqx_service, **{"replicas": 4}},
            "logstash": {**base_logstash_service},
            "iot-device-manager": {**base_iot_service}
        },
    }
]

