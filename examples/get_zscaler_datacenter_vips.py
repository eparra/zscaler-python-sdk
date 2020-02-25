# -*- coding: utf-8 -*-

import time
import zscaler_python_sdk


def main():


	print("\n\n ##########  STARTING SDK ##########\n\n")
	z = zscaler_python_sdk.zscaler()
	z.get_zia_partner_creds_from_env(True)
	z.set_cloud('betacloud')
	z.authenticate_partner_api()

	# Get all public and private Zscaler Datacenter VIPs
	print("\n\n ##########  GET ALL PUBLIC AND PRIVATE VIPS ##########\n\n")
	z.get_all_vips()	

	time.sleep(2)

	# Get all public Zscaler Datacenter VIPs
	print("\n\n ##########  GET ALL PUBLIC VIPS ##########\n\n")
	z.get_all_public_vips()	

	time.sleep(2)

	# Get all private Zscaler Datacenter VIPs
	print("\n\n ##########  GET ALL PRIVATE VIPS ##########\n\n")
	z.get_all_private_vips()		

	
if __name__ == '__main__':
	main()
