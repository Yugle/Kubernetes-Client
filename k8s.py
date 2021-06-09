from kubernetes import client, config
import re

class UpdateSevice:
	def __init__(self, config_file):
		config.kube_config.load_kube_config(config_file = config_file)

		core_v1 = client.CoreV1Api()
		for namespace in core_v1.list_namespace().items:
		    if(re.findall("-gitops", namespace.metadata.name) != []):
		    	self.namespace_name = namespace.metadata.name
		    	break

		self.v1  = client.AppsV1Api()

	def getDeploymentList(self):
		item_list = self.v1.list_namespaced_deployment(namespace = self.namespace_name).items
		sevice_list = []
		for sevice in item_list:
			sevice_list.append(sevice.metadata.name)

		return sevice_list

	def getCurrentVersion(self, sevice_name):
		info = self.v1.read_namespaced_deployment(namespace = self.namespace_name, name = sevice_name)
		current_version = info.spec.template.spec.containers[0].image.split("/")[1]

		return current_version
	
	def updateServie(self, sevice_name, new_version):
		info = self.v1.read_namespaced_deployment(namespace = self.namespace_name, name = sevice_name)

		old_image = info.spec.template.spec.containers[0].image
		new_image = "lan.dhms.net:5000/"+ new_version
		info.spec.template.spec.containers[0].image = new_image

		response = self.v1.patch_namespaced_deployment(namespace = self.namespace_name, name = sevice_name, body = info)
		return response.spec.template.spec.containers[0].image