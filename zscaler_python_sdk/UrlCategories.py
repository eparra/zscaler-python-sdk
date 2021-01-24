import logging
from .Defaults import *


class UrlCategories(object):


	def get_url_categories(self):

		uri = self.api_url + '/api/v1/urlCategories?customOnly=true'

		res = self._perform_get_request(
			uri,
			self._set_header(self.jsessionid)
		)
		return res		


	def create_url_categories(self):
		pass


	def get_url_categories_lite(self):

		uri = self.api_url + '/api/v1/urlCategories/lite'

		res = self._perform_get_request(
			uri,
			self._set_header(self.jsessionid)
		)
		return res	


	def get_url_categories_by_id(self, category_id):

		uri = self.api_url + '/api/v1/urlCategories/' + str(category_id)

		res = self._perform_get_request(
			uri,
			self._set_header(self.jsessionid)
		)
		return res	


	def update_url_categories_by_id(self):
		pass	


	def delete_url_categories_by_id(self):
		pass	


	def get_url_lookup(self, urls):

		uri = self.api_url + 'api/v1/urlLookup' 

		body = urls

		res = self._perform_post_request(
			uri,
			body, 
			self._set_header(self.jsessionid)
		)
		return res   