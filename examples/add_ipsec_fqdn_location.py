# -*- coding: utf-8 -*-

import zscaler_python_sdk


def main():

	fqdn          = 'test@example.com'
	location_name = 'sjc_sdwan_1 (San Jose, CA)'

	print("\n\n ##########  STARTING SDK ##########\n\n")
	z = zscaler_python_sdk.zscaler()
	z.get_zia_partner_creds_from_env(True)
	z.set_cloud('betacloud')
	z.authenticate_partner_api()

	# Get Locations (Before add)
	print("\n\n ##########  GET LOCATIONS (BEFORE) ##########\n\n")
	z.get_locations()	

	# Pass FQDN.  Will resposnd with VPN credential id 
	print("\n\n ##########  CREATE VPN CREDENTIAL  ##########\n\n")	
	res = z.create_vpn_credential(fqdn, None)

	# Extract ID from the prior response. 
	print("\n\n ##########  EXTRACT VPN CREDENTIAL ID  ##########\n\n")		
	vpn_id = z.extract_id_from_response(res.content)

	# Pass location name, VPN credential id, and FQDN
	print("\n\n ##########  CREATE LOCATION  ##########\n\n")	
	res = z.create_location_with_vpn_credential(
		location_description,
		vpn_id,
		fqdn
	)	    

	# Extract ID from the prior response. 
	print("\n\n ##########  EXTRACT LOCATION ID  ##########\n\n")
	location_id = z.extract_location_id(res.content)

	# Activate change
	print("\n\n ##########  ACTIVATE CHANGES  ##########\n\n")	
	z.activate()

	# Get Locations (After add)
	print("\n\n ##########  GET LOCATIONS (AFTER)  ##########\n\n")	
	z.get_locations()

	# Get VPN Credentials
	print("\n\n ##########  GET VPN CREDENTIALS  ##########\n\n")	
	z.get_vpn_credentials()

	# Get VPN Credentials by Id
	print("\n\n ##########  GET VPN CREDENTIALS BY ID ##########\n\n")		
	z.get_vpn_credential_by_id(vpn_id)


if __name__ == '__main__':
	main()
