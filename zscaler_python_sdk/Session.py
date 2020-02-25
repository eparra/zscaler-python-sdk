
import json
import time
import platform
import re
import logging
from .Defaults import *


class Session(object):


	def _set_header(self, cookie=None):      
		header = {
			'Content-Type'  : 'application/json',
			'Cache-Control' : 'no-cache',
			'User-Agent'    : self.user_agent
		}
		if cookie:
			header['cookie'] = cookie
		if self.debug:
			logging.debug("HTTP Header: {}".format(header))
		return header


	def _parse_jsessionid(self, cookie):
		jsessionid = re.sub(r';.*$', "", cookie)
		if self.debug:
			logging.debug("JSESSION ID: {}".format(jsessionid))		
		return jsessionid


	def _set_obfuscateApiKey(self, api_key):
		now = str(int(time.time() * 1000))  
		n = now[-6:]
		r = str(int(n) >> 1).zfill(6)
		key = ""
		for i in range(0, len(n), 1):
			key += api_key[int(n[i])]
		for j in range(0, len(r), 1):
			key += api_key[int(r[j])+2]
		self.obfuscatedApiKey = key
		self.ts = now
		if self.debug:
			logging.debug("OBFUSCATED APY KEY / Time: {} / {}".format(self.obfuscatedApiKey, self.ts))		


	def _get_jsessionid(self, type):

		uri = self.api_url + 'api/v1/authenticatedSession'
		
		if type is 'api':
			body = {
				'username'  : self.zia_username,
				'password'  : self.zia_password,
				'apiKey'    : self.obfuscatedApiKey,
				'timestamp' : self.ts
			}

		if type is 'partner':
			body = {
				'username'  : self.partner_username,
				'password'  : self.partner_password,
				'apiKey'    : self.obfuscatedApiKey,
				'timestamp' : self.ts
			}	

		if self.debug:
			logging.debug("HTTP BODY: {}".format(body))	

		res = self._perform_post_request(
			uri,
			body,
			self._set_header()
		)
		self.jsessionid = self._parse_jsessionid(res.headers['Set-Cookie'])        


	def _handle_response(self, response, content):

		status = response.status_code
		if status in (301, 302, 303, 307):
			if self.debug:
				logging.debug("HTTP RESPONSE (Redirection) - Status Code: {}".format(status))
		elif 200 <= status <= 299:
			if self.debug:
				logging.debug("HTTP RESPONSE (Success) - Status Code: {}".format(status))
		elif 401 <= status <= 499:
			if self.debug:
				logging.debug("HTTP RESPONSE (Client Error) - Status Code: {}".format(status))
		else:
			if self.debug:
				logging.debug("HTTP RESPONSE (Unknown ) - Status Code: {}".format(status))


	def _perform_get_request(self, uri, header):

		res = self.session.get(
			uri, 
			headers=header,
			timeout=REQUEST_TIMEOUTS			
		)

		if res.content:
			parsed = json.loads(res.content)
			json_response = json.dumps(parsed, sort_keys=True, indent=4, separators=(',', ': ')) if res.content else {}		
		
			if self.debug:
				logging.debug("GET RESPONSE FROM (URI): {}\nRESPONSE BODY: {}".format(
					uri,
					json_response)
				)	
		
		self._handle_response(res, res.content.decode('utf-8'))
		return res


	def _perform_post_request(self, uri, body, header):
	
		attempt = json.dumps(body, sort_keys=True, indent=4, separators=(',', ': '))
		if self.debug:
			logging.debug("ATTEMPTING POST (URI): {}\nPOST BODY: {}".format(
				uri,
				attempt)
			)	
		res = self.session.post(
			uri, 
			json=body, 
			headers=header,
			timeout=REQUEST_TIMEOUTS			
		)

		if res.content:
			parsed = json.loads(res.content)
			json_response = json.dumps(parsed, sort_keys=True, indent=4, separators=(',', ': ')) if res.content else {}

			if self.debug:
				logging.debug("POST RESPONSE FROM (URI): {}\nRESPONSE BODY: {}".format(
					uri,
					json_response)
				)	

		self._handle_response(res, res.content.decode('utf-8'))
		return res


	def _perform_put_request(self, uri, body, header):

		attempt = json.dumps(body, sort_keys=True, indent=4, separators=(',', ': '))
		if self.debug:
			logging.debug("ATTEMPTING PUT (URI): {}\nPUT BODY: {}".format(
				uri,
				attempt)
			)
		res = self.session.put(
			uri,
			json=body,
			headers=header,
			timeout=REQUEST_TIMEOUTS
		)

		if res.content:
			parsed = json.loads(res.content)
			json_response = json.dumps(parsed, sort_keys=True, indent=4, separators=(',', ': ')) if res.content else {}

			if self.debug:
				logging.debug("PUT RESPONSE FROM (URI): {}\nRESPONSE BODY: {}".format(
					uri,
					json_response)
				)

		self._handle_response(res, res.content.decode('utf-8'))
		return res


	def _perform_delete_request(self, uri, header):
	
		res = self.session.delete(
			uri, 
			headers=header,
			timeout=REQUEST_TIMEOUTS
		)	

		if res.content:
			if self.debug:
				logging.debug("DELETE METHOD (URI): {}, HEADERS: {}".format(
					uri,
					header)
				)	
		
		self._handle_response(res, res.content.decode('utf-8'))
		return res
