import logging
import os
from .Defaults import *


class Auth(object):


	def get_settings_from_dict(self, **kwargs):
		pass


	def get_zia_creds_from_env(self, debug):
		"""
		Gets the  ZIA Credentials from the Shell Environmnnet.
		Must pass True | False for Debug Logging.  Default = True
    	"""
		if debug:
			self.debug = debug
		else:
			self.debug = DEBUG_DEFAULT

		# Username should be stored as an environmental variable named "ZIA_USERNAME"
		if os.environ.get('ZIA_USERNAME') is not None:
			self.zia_username = os.environ.get('ZIA_USERNAME')
		else:
			logging.debug("ENV IMPORT ERROR: {}".format("ZIA_USERNAME not found"))
			exit()

		# Password should be stored as an environmental variable named "ZIA_PASSWORD"
		if os.environ.get('ZIA_PASSWORD') is not None:
			self.zia_password = os.environ.get('ZIA_PASSWORD')
		else:
			logging.debug("ENV IMPORT ERROR: {}".format("ZIA_PASSWORD not found"))
			exit()

		# ZIA API Key should be stored as an environmental variable named "ZIA_API"
		if os.environ.get('ZIA_API') is not None:
			self.zia_api_key  = os.environ.get('ZIA_API')
			if len(self.zia_api_key) < MIN_API_KEY_LENGTH:
				logging.debug("ZIA API Key must be %{} characters".format(MIN_API_KEY_LENGTH))
				exit()
		else:
			logging.debug("ENV IMPORT ERROR: {}".format("ZIA_API not found"))
			exit()


	def get_zia_partner_creds_from_env(self, debug):			
		"""
		Gets the  Partner Credentials from the Shell Environmnnet.
		Must pass True | False for Debug Logging.  Default = True
    	"""
		if debug:
			self.debug = debug
		else:
			self.debug = DEBUG_DEFAULT

		# Partner username should be stored as an environmental variable named "PARTNER_USERNAME"
		if os.environ.get('ZIA_PARTNER_USERNAME') is not None:
			self.partner_username = os.environ.get('ZIA_PARTNER_USERNAME')
		else:
			logging.debug("ENV IMPORT ERROR: {}".format("ZIA_PARTNER_USERNAME not found"))
			exit()

		# Partner password should be stored as an environmental variable named "PARTNER_PASSWORD"
		if os.environ.get('ZIA_PARTNER_PASSWORD') is not None:
			self.partner_password = os.environ.get('ZIA_PARTNER_PASSWORD')
		else:
			logging.debug("ENV IMPORT ERROR: {}".format("ZIA_PARTNER_PASSWORD not found"))
			exit()

		# Partner API Key should be stored as an environmental variable named "PARTNER_API"
		if os.environ.get('ZIA_PARTNER_API') is not None:
			self.partner_api_key  = os.environ.get('ZIA_PARTNER_API')
			if len(self.partner_api_key) < MIN_API_KEY_LENGTH:
				logging.debug("Partner API Key must be %{} characters".format(MIN_API_KEY_LENGTH))
				exit()
		else:
			logging.debug("ENV IMPORT ERROR: %{}".format("ZIA_PARTNER_API not found"))
			exit()


	def authenticate_zia_api(self):
		self._set_obfuscateApiKey(self.zia_api_key)
		self._get_jsessionid('api')


	def authenticate_partner_api(self):
		self._set_obfuscateApiKey(self.partner_api_key)
		self._get_jsessionid('partner')


	def set_cloud(self, cloud):

		if cloud in Z_CLOUDS:
			self.api_url = Z_CLOUDS[cloud]
			if self.debug:
				logging.debug("CLOUD SET TO: {}".format(cloud))
		else:
                        if self.debug:
                                logging.debug("CLOUD ERROR: {}".format("Unknown Cloud"))
                        return "Unknown Cloud"
