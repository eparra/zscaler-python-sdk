
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

	def get_location_all_sub_locations(self, location_id):

		if not location_id:
			return "Location ID Required"

		uri = self.api_url + 'api/v1/locations/' + str(location_id) + '/sublocations'

		res = self._perform_get_request(
			uri,
			self._set_header(self.jsessionid)
		)
		return res

	def create_location_with_vpn_credential(self, location_name, vpn_cred_id, fqdn, gateway_options = None):

		if not location_name:
			return 'Location Name Required'

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
		return self._create_location_with_ip_address(body, gateway_options)


	def create_location_with_ip_address(self, location_name, ip_address, gateway_options = None):

		if not location_name:
			return 'Location Name Required'

		if not ip_address:
			return 'Static IP ID Required'

		body = {
			"name": location_name,
			"ipAddresses" :  [ ip_address ]
		}
		return self._create_location_with_ip_address(body, gateway_options)


	def _create_location_with_ip_address(self, body, gateway_options = None):

		uri = self.api_url + 'api/v1/locations'

		if gateway_options:
			body = {**body, **gateway_options}

		res = self._perform_post_request(
			uri,
			body,
			self._set_header(self.jsessionid)
		)
		return res


	def create_sub_location(self, parent_id, location_name, ip_addresses, gateway_options = None):

		uri = self.api_url + 'api/v1/locations'

		if not parent_id:
			return 'Location Parent ID Required'

		if not location_name:
			return 'Location Name Required'

		if not ip_addresses:
			return 'IP Addresses Required'			

		body = {
			"name": location_name,
			"parentId": parent_id,			
			"ipAddresses": [
				ip_addresses
			],
		}

		if gateway_options:
			body = {**body, **gateway_options}

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
			return "Location ID Required"

		uri = self.api_url + 'api/v1/locations/' + str(location_id)

		res = self._perform_get_request(
			uri,
			self._set_header(self.jsessionid)
		)
		return res


	def update_location_by_id(self, location_id, body):

		if not location_id:
			return "Location Required"

		uri = self.api_url + 'api/v1/locations/' + str(location_id)

		res = self._perform_put_request(
			uri,
			body,
			self._set_header(self.jsessionid)
		)
		return res


	def delete_location_by_id(self, location_id):
		if not location_id:
			return "Location Required"

		uri = self.api_url + 'api/v1/locations/' + str(location_id)

		res = self._perform_delete_request(
			uri,
			self._set_header(self.jsessionid)
		)
		return res

	def get_vpn_endpoints(self, ipv4_addr):

		if not ipv4_addr:
			return 'IPv4 Address Required'

		uri = 'https://pac.zscalerbeta.net/getVpnEndpoints?srcIp=' + ipv4_addr

		res = self._perform_get_request(
			uri,
			self._set_header(self.jsessionid)
		)
		return res
