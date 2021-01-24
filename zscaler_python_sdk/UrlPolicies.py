import logging
from .Defaults import *


class UrlPolicies(object):


	def get_url_filtering_rules(self):

		uri = self.api_url + '/api/v1//urlFilteringRules'

		res = self._perform_get_request(
			uri,
			self._set_header(self.jsessionid)
		)
		return res


	def create_url_filtering_rules(self):
		pass


	def get_url_filtering_rules_by_id(self, rule_id):

		uri = self.api_url + '/api/v1/urlFilteringRules/' + str(category_id)

		res = self._perform_get_request(
			uri,
			self._set_header(self.jsessionid)
		)
		return res		


	def update_url_filtering_rules_by_id(self):
		pass	


	def delete_url_filtering_rules_by_id(self):
		pass	
	    