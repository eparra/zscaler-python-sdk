
import logging

class Activation(object):

	def get_status(self):

		uri = self.api_url + 'api/v1/status'

		self._set_header(self.jsessionid)
		res = self._perform_get_request(
			uri,
			self._set_header(self.jsessionid)
		)
		return res


	def activate(self):

		uri = self.api_url + 'api/v1/status/activate'

		res = self._perform_post_request(
			uri,
			"",
			self._set_header(self.jsessionid)
		)
		return res
        
