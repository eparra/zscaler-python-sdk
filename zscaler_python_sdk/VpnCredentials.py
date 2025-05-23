import random
import string
import json
import logging
from .Defaults import *


class VpnCredentials(object):


	def _randomize_psk(self):
		
		psk = ''.join(random.choices(string.ascii_letters + string.digits, k=MAX_PSK_LENGTH))
		if self.debug:
			logging.debug("RANDOM PSK: {} (PSK Length: {})".format(
				psk,
				len(psk)
			))
		return psk	



	def get_vpn_credentials(self):

		uri = self.api_url + 'api/v1/vpnCredentials'

		res = self._perform_get_request(
			uri,
			self._set_header(self.jsessionid)
		)
		return res


	def create_vpn_credential(self, fqdn, psk):

		uri = self.api_url + 'api/v1/vpnCredentials'

		if not fqdn:
			if self.debug:
				logging.error("ERROR: {}".format("No FQDN Provided"))
			return 'No FQDN Provided'

		if psk and self.debug:
			logging.debug("PREDEFINED PSK: {}".format(psk))
		elif not psk:
			psk = self._randomize_psk()

		body = {
			'type'         : 'UFQDN',
			'fqdn'         : fqdn, 
			'comments'     : 'Zscaler SDK',
			'preSharedKey' : psk
		}

		res = self._perform_post_request(
			uri,
			body,
			self._set_header(self.jsessionid)
		)
		return res


	def get_vpn_credential_by_id(self, vpn_id):

		uri = self.api_url + 'api/v1/vpnCredentials/' + str(vpn_id)

		res = self._perform_get_request(
			uri,
			self._set_header(self.jsessionid)
		)
		return res


	def update_vpn_credential_by_id(self, vpn_id, fqdn, psk):

		uri = self.api_url + 'api/v1/vpnCredentials/' + str(vpn_id)

		if not fqdn:
			if self.debug:
				logging.error("ERROR: {}".format("No FQDN Provided"))
			return 'No FQDN Provided'

		if psk and self.debug:
			logging.debug("PREDEFINED PSK: {}".format(psk))
		elif not psk:
			psk = self._randomize_psk()

		body = {
			'type'         : 'UFQDN',
			'fqdn'         : fqdn,
			'comments'     : 'Zscaler SDK',
			'preSharedKey' : psk
		}

		res = self._perform_put_request(
			uri,
			body,
			self._set_header(self.jsessionid)
		)
		return res


	def delete_vpn_credential_by_id(self, vpn_id):

		uri = self.api_url + 'api/v1/vpnCredentials/' + str(vpn_id)

		res = self._perform_delete_request(
			uri,
			self._set_header(self.jsessionid)
		)
		return res
