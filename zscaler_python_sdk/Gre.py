
import logging
from .Defaults import *


class Gre(object):
	

	def get_gre_tunnel_details(self):

		uri = self.api_url + 'api/v1/orgProvisioning/ipGreTunnelInfo'

		res = self._perform_get_request(
			uri,
			self._set_header(self.jsessionid)
		)
		return res
