SECOND_WAIT = 20

# config_file = "config/env/dev.yaml"
# namespace_dev = "qa4-dev"
# env = 'qa4'
namespace_dev = "qa2"
env = 'qa2'
config_file = "config/env/dev-v1.24.yaml"

case_list = [
    {
        "case_name": "单秒10hz的测试",
        "throughput": 10000,
        "thread_count": 10,
        "client_list": ['emqx', 'kafka', 'kafka2'],
        "config_file": config_file,
        "service_list": {
        },
    },
    {
        "case_name": "单秒20hz的测试",
        "throughput": 10000,
        "thread_count": 10,
        "client_list": ['emqx', 'kafka', 'kafka2'],
        "config_file": config_file,
        "service_list": {
        },
    }
]

