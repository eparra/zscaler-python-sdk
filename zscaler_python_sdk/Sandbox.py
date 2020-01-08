import logging
from .Defaults import *


class Sandbox(object):


	def get_sanbox_report_md5(self, md5hash):

		uri = self.api_url + 'api/v1/sandbox/report/' + str(md5hash) + '?details=full'

		res = self._perform_get_request(
			uri,
			self._set_header(self.jsessionid)
		)
		return res		


	def get_sanbox_report_sha1(self):
		pass


	def get_sanbox_report_sha256(self):	
		pass

	
	def is_md5hash_malicious(self):
		pass


	def is_sha1_malicious(self):
		pass


	def is_sha256_malicious(self):
		pass				
