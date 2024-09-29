from kubernetes import client, config
import time
import logging
import datetime
logger = logging.getLogger('k8s')
logger.setLevel(logging.INFO)


class Kubernetes:

    def __init__(self, test_config):
        self.test_config = test_config
        config.load_kube_config(config_file=self.test_config['config_file'])
        self.app_client = client.AppsV1Api()
        self.pod_client = client.CoreV1Api()
        self.start_time = 0

    def edit_all(self):
        self.start_time = int(time.time())

        for service_name in self.test_config['service_list']:
            logger.info(f"{service_name} pod")
            service_config = self.test_config['service_list'][service_name]
            if service_config['type'] == 'deploy':
                self.edit_deploy(service_name, service_config)
            elif service_config['type'] == 'statefulset':
                self.edit_statefulset(service_name, service_config)

    def edit_deploy(self, service_name, service_config):
        deployment_detail = self.app_client.read_namespaced_deployment(
            name=service_name,
            namespace=service_config['namespace']
        )
        replicas_edit_flag = deployment_detail.spec.replicas != service_config['replicas']
        resources_edit_flag = False

        deployment_detail.spec.replicas = service_config['replicas']

        for container in deployment_detail.spec.template.spec.containers:
            if container.name == service_config['container']:
                resources_edit_flag = resources_edit_flag or (container.resources.requests["cpu"] != service_config['cpu_reservation'])
                resources_edit_flag = resources_edit_flag or (container.resources.requests["memory"] != service_config['mem_reservation'])
                resources_edit_flag = resources_edit_flag or (container.resources.limits["cpu"] != service_config['cpu_limit'])
                resources_edit_flag = resources_edit_flag or (container.resources.limits["memory"] != service_config['mem_limit'])

                container.resources.requests["cpu"] = service_config['cpu_reservation']
                container.resources.requests["memory"] = service_config['mem_reservation']
                container.resources.limits["cpu"] = service_config['cpu_limit']
                container.resources.limits["memory"] = service_config['mem_limit']

        if not resources_edit_flag and not replicas_edit_flag:
            return

        self.app_client.replace_namespaced_deployment(
            name=service_name,
            namespace=service_config['namespace'],
            body=deployment_detail
        )

        self.loading(service_name, service_config, resources_edit_flag)

    def edit_statefulset(self, service_name, service_config):
        statefulset_detail = self.app_client.read_namespaced_stateful_set(
            name=service_name,
            namespace=service_config['namespace']
        )
        replicas_edit_flag = statefulset_detail.spec.replicas != service_config['replicas']
        resources_edit_flag = False

        statefulset_detail.spec.replicas = service_config['replicas']
        for container in statefulset_detail.spec.template.spec.containers:
            if service_config['container'] == container.name:
                resources_edit_flag = resources_edit_flag or (container.resources.requests["cpu"] != service_config['cpu_reservation'])
                resources_edit_flag = resources_edit_flag or (container.resources.requests["memory"] != service_config['mem_reservation'])
                resources_edit_flag = resources_edit_flag or (container.resources.limits["cpu"] != service_config['cpu_limit'])
                resources_edit_flag = resources_edit_flag or (container.resources.limits["memory"] != service_config['mem_limit'])

                container.resources.requests["cpu"] = service_config['cpu_reservation']
                container.resources.requests["memory"] = service_config['mem_reservation']
                container.resources.limits["cpu"] = service_config['cpu_limit']
                container.resources.limits["memory"] = service_config['mem_limit']

        if not resources_edit_flag and not replicas_edit_flag:
            return

        self.app_client.replace_namespaced_stateful_set(
            name=service_name,
            namespace=service_config['namespace'],
            body=statefulset_detail
        )

        self.loading(service_name, service_config, resources_edit_flag)

    def loading(self, service_name, service_config, resources_edit_flag):
        logger.info(f"{service_name} loading start")
        time.sleep(1)
        timeout_seconds = 300
        def is_run(pod):
            # print(111)
            # print(pod.status.container_statuses)

            ready = all((status and status.ready) for status in pod.status.container_statuses)
            # print(pod.status.phase)
            # print(pod.status.phase == "Running")
            # print(self.start_time)
            # print(int(pod.status.start_time.timestamp()))
            # print(self.start_time <= int(pod.status.start_time.timestamp()))
            # print(ready)
            # print(resources_edit_flag)
            if resources_edit_flag:
                return ready and (pod.status.phase == "Running") and (self.start_time <= int(pod.status.start_time.timestamp()))
            else:
                return ready and pod.status.phase == "Running"

        while True:
            # print(222)
            # print(self.pod_client.list_namespaced_pod(
            #     namespace=service_config['namespace'],
            #     label_selector=f"app={service_name}"
            # ))

            pod_list = self.pod_client.list_namespaced_pod(
                namespace=service_config['namespace'],
                label_selector=f"app={service_name}"
            ).items
            # print(pod_list)
            if all(is_run(pod) for pod in pod_list) and len(pod_list) == service_config['replicas']:
                # print("所有 Pod 已成功运行。")
                break

            if int(time.time()) - self.start_time >= timeout_seconds:
                print("等待超时，未能确保所有 Pod 运行成功。")
                break

            time.sleep(5)
        time.sleep(2)

# with open("default.yaml", "r", encoding="utf-8") as f:
#     config_data = yaml.safe_load(f)
# a = Kubernetes(config_data['k8s'])
# a.edit_deploy()
# with open("default.yaml", "r", encoding="utf-8") as f:
#     config_data = yaml.safe_load(f)
if __name__ == "__main__":
    a = Kubernetes({
        "config_file": "config/env/dev.yaml",
        "service_list": {
            "iot-device-manager": {
                "type": "deploy",
                "namespace": "qa4-dev",
                "container": "iot-device-manager",
                "replicas": 3,
                "cpu_reservation": '200m',
                "cpu_limit": '1',
                "mem_reservation": '1Gi',
                "mem_limit": '1Gi',
            },
            "emqx": {
                "type": "statefulset",
                "namespace": "qa4-dev",
                "container": "emqx",
                "replicas": 3,
                "cpu_reservation": '2',
                "cpu_limit": '2',
                "mem_reservation": '3Gi',
                "mem_limit": '3Gi',
            }
        }
    })
    a.edit_all()
    # a.edit_deploy()
