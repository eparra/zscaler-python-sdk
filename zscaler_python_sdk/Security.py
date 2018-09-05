
import json
import logging

class Security(object):


	def get_whitelist_urls(self):

		uri = self.api_url + 'api/v1/security'

		res = self._perform_get_request(
			uri,
			self._set_header(self.jsessionid)
		)
		return res


	def update_whitelist_urls(self):
		pass


	def get_blacklist_urls(self):

		uri = self.api_url + 'api/v1/security/advanced'

		res = self._perform_get_request(
			uri,
			self._set_header(self.jsessionid)
		)
		return res


	def update_blacklist_urls(self):
		pass	


	def add_blacklist_urls(self, black_list_urls):

		uri = self.api_url + 'api/v1/security/advanced/blacklistUrls?action=ADD_TO_LIST'

		body = {
			"blacklistUrls": [
			]
		}

		for url in black_list_urls:
			body['blacklistUrls'].append(str(url))

		res = self._perform_post_request(
			uri,
			body,
			self._set_header(self.jsessionid)
		)
		return res


	def remove_blacklist_urls(self):
		pass	
        
body = {
    "url-filter": [
    ]
}