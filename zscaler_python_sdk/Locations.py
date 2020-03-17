
import logging
import json
from .Defaults import *


class Locations(object):


	def extract_location_id(self, json_response):

		data = json_response
		if self.debug:
			logging.debug("Extract Location ID: {}".format(data['id']))
		return data['id']


	def get_locations(self, page_size=1000, page_count=1):

		uri = self.api_url + f'api/v1/locations?pageSize={page_size}&page={page_count}'

		res = self._perform_get_request(
			uri,
			self._set_header(self.jsessionid)
		)
		return res


	def get_sub_locations(self, location_id, page_size=1000, page_count=1):

		if not location_id:
			return 'Location ID Required'

		uri = self.api_url + \
			  f'api/v1/locations/{location_id}/sublocations?pageSize={page_size}&page={page_count}'

		res = self._perform_get_request(
			uri,
			self._set_header(self.jsessionid)
		)
		return res


	def create_location(self, location_name, vpn_cred_id, fqdn, gateway_options = None):

		uri = self.api_url + 'api/v1/locations'

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


	def create_location_by_payload(self, z_loc_payload, is_sub_loc=False):
		"""
		Create location or sub-location by passing the correct payload.
		Use this method to pass constructed zscaler location payload.

		* To create zscaler location, these fields are mandatory:
			* name
			* vpnCredentials = [{},{}...]

		* To create zscaler sub-location, these fields are mandatory:
			* parentId
			* name
			* ipAddresses
			* vpnCredentials = must be none or empty

		For other non-mandatory fields, see - https://help.zscaler.com/zia/api#/Locations/addLocation

		:param z_loc_payload: zscaler location payload
		:param is_sub_loc: To create zscaler sub-location pass it True
		"""

		if not (z_loc_payload and isinstance(z_loc_payload, dict)):
			return 'Location Payload Required'

		if not z_loc_payload.get('name', None):
			return 'Location Name Required'

		vpn_creds = z_loc_payload.get('vpnCredentials', [])

		if not is_sub_loc and not vpn_creds:
			return 'Location VPN Credentials Required'

		if is_sub_loc:
			if not z_loc_payload.get('parentId', None):
				return 'Sub-Location Parent Id Required'

			if not z_loc_payload.get('ipAddresses', []):
				return 'Sub-Location Ip Addresses Required'

			if vpn_creds:
				return 'Sub-Location VPN Credentials Not Required'

		uri = self.api_url + 'api/v1/locations'

		res = self._perform_post_request(
			uri,
			z_loc_payload,
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
			return 'Location ID Required'

		uri = self.api_url + 'api/v1/locations/' + str(location_id)

		res = self._perform_get_request(
			uri,
			self._set_header(self.jsessionid)
		)
		return res


	def update_location_by_id(self, location_id):
		pass


	def update_location(self, location):

		if not location:
			return 'Location Required'

		uri = self.api_url + 'api/v1/locations/' + str(location['id'])

		res = self._perform_put_request(
			uri,
			location,
			self._set_header(self.jsessionid)
		)
		return res


	def delete_location_by_id(self, location_id):

		if not location_id:
			return 'Location Required'

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
