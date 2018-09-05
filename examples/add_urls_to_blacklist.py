# -*- coding: utf-8 -*-

import json
import time
import zscaler_python_sdk


def main():

	print("\n\n ##########  STARTING SDK  ##########\n\n")
	z = zscaler_python_sdk.zscaler()
	z.get_zia_creds_from_env(True)
	z.set_cloud('betacloud')
	z.authenticate_zia_api()

	# 
	print("\n\n ##########  GET BLACKLIST (BEFORE)  ##########\n\n")
	z.get_blacklist_urls()

	# 
	url_list = [
		'umbrella.cisco.com',
		'.paloaltonetworks.com',
		'.versa-networks.com'
	]
	print("\n\n ##########  URL LIST TO ADD TO BLACKLIST  ##########\n\n")	
	print (url_list)

	# 
	print("\n\n ##########  ADD URL LIST TO BLACKLIST  ##########\n\n")
	z.add_blacklist_urls(url_list)

	# Activate change
	print("\n\n ##########  ACTIVATE CHANGES  ##########\n\n")	
	z.activate()

	# Sleep for 10 seconds
	print("\n\n ##########  Sleep for 10 seconds  ##########\n\n")	
	time.sleep(10)

	# 
	print("\n\n ##########  GET BLACKLIST (AFTER)  ##########\n\n")
	z.get_blacklist_urls()


if __name__ == '__main__':
	main()
