
import logging
import json
from .Defaults import *


class Locations(object):


	def extract_location_id(self, json_response):

		data = json.loads(json_response)
		if self.debug:
			logging.debug("Extract Location ID: {}".format(data['id']))
		return data['id']


	def get_locations(self):

		uri = self.api_url + 'api/v1/locations'

		res = self._perform_get_request(
			uri,
			self._set_header(self.jsessionid)
		)
		return res


	def create_location(self, location_name, vpn_cred_id, fqdn):

		uri = self.api_url + 'api/v1/locations'

		if not vpn_cred_id:
			return 'VPN Credential ID Required'

		if not fqdn:
			return 'FQDN Required'

		body = {
			"name": location_name,
			"vpnCredentials": [
				{
					"id": vpn_cred_id,
					"type": "UFQDN",
					"fqdn": fqdn
				}
			]
		}

		res = self._perform_post_request(
			uri,
			body,
			self._set_header(self.jsessionid)
		)
		return res


	def get_locations_lite(self):

		uri = self.api_url + 'api/v1/locations/lite' 

		res = self._perform_get_request(
			uri,
			self._set_header(self.jsessionid)
		)
		return res


	def get_locations_by_id(self, location_id):

		if not location_id:
			return "Location Requried"

		uri = self.api_url + 'api/v1/locations/lite/' + str(location_id)

		res = self._perform_get_request(
			uri,
			self._set_header(self.jsessionid)
		)
		return res


	def update_location_by_id(self, location_id):
		pass


	def delete_location_by_id(self, location_id):
		pass


	def get_vpn_endpoints(self, ipv4_addr):

		if not ipv4_addr:
			return 'IPv4 Address Requried'

		uri = 'https://pac.zscalerbeta.net/getVpnEndpoints?srcIp=' + ipv4_addr

		res = self._perform_get_request(
			uri,
			self._set_header(self.jsessionid)
		)
		return res
	
