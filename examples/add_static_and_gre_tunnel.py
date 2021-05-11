# -*- coding: utf-8 -*-

import zscaler_python_sdk


def main():

	static_ipv4       = 'X.X.X.X'  # Your public static IP address 
	latitude          = '47.608013'
	longitude         = '-122.335167'
	primary_gre_vip   = '199.168.148.131'  # BetaCloud - Bay Area, CA 
	secondary_gre_vip = '104.129.194.46'   # BetaCloud - Washington, D.C.
	location_name     = 'sjc_sdwan_1 (San Jose, CA)'


	print("\n\n ##########  STARTING SDK ##########\n\n")
	z = zscaler_python_sdk.zscaler()
	z.get_zia_partner_creds_from_env(True)
	z.set_cloud('betacloud')
	z.authenticate_partner_api()


	# Create static IP address
	print("\n\n ##########  CREATE STATIC IP ##########\n\n")
	res = z.create_static_ip(
		static_ipv4,
		latitude, 
		longitude
	)

	# Extract Static IP ID. 
	print("\n\n ##########  EXTRACT STATIC IP ID  ##########\n\n")		
	static_id = z.extract_id_from_response(res.content)

	# Get VIPs by Source IP
	print("\n\n ##########  GET GRE VIPS BY SOURCE IP  ##########\n\n")	
	z.get_gre_vips(static_ipv4)

	# Create GRE tunnel
	print("\n\n ##########  CREATE GRE TUNNEL ##########\n\n")
	res = z.create_gre_tunnel(
		static_ipv4,
		primary_gre_vip,
		secondary_gre_vip
	)

	# Extract GRE Tunnel ID. 
	print("\n\n ##########  EXTRACT GRE ID  ##########\n\n")		
	gre_id = z.extract_id_from_response(res.content)

	# Create Location with GRE Tunnel ID
	print("\n\n ##########  CREATE LOCATION WITH IP ADDRESS ##########\n\n")
	res = z.create_location_with_ip_address(
		location_name,
		static_ipv4
	)

	# Extract Location ID. 
	print("\n\n ##########  EXTRACT LOCATION ID  ##########\n\n")		
	location_id = z.extract_id_from_response(res.content)


if __name__ == '__main__':
	main()
