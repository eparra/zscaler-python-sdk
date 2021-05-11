
import logging


class Activation(object):

	def get_status(self):

		uri = '{}api/v1/status'.format(
			self.api_url
			)

		self._set_header(self.jsessionid)
		res = self._perform_get_request(
			uri,
			self._set_header(self.jsessionid)
		)
		return res


	def activate(self):

		uri = '{}api/v1/status/activate'.format(
			self.api_url
			)

		res = self._perform_post_request(
			uri,
			"",
			self._set_header(self.jsessionid)
		)
		return res
        
