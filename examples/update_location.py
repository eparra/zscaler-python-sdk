# -*- coding: utf-8 -*-

import zscaler_python_sdk


gateway_options = {
	"authRequired" : True,
	"surrogateIP" : True,
	"displayTimeUnit": "HOUR",
	"idleTimeInMinutes" : 480,
	"surrogateIPEnforcedForKnownBrowsers" : True,
	"surrogateRefreshTimeInMinutes" : 240,
	"surrogateRefreshTimeUnit" : "MINUTE",
	"ofwEnabled" : True,
	"ipsControl" : True,
}


def main():

	location_name = 'sjc_sdwan_1 (San Jose, CA)'

	print("\n\n ##########  STARTING SDK ##########\n\n")
	z = zscaler_python_sdk.zscaler()
	z.get_zia_partner_creds_from_env(True)
	z.set_cloud('betacloud')
	z.authenticate_partner_api()

	# Get Locations 
	print("\n\n ##########  GET LOCATIONS (AFTER)  ##########\n\n")	

	location_resp = z.get_locations()

	# Get a Location ID from get_location() output. After, insert the
	# Location ID as the first parameter in z.update_location below.
	# the ID for Locations and Sub-Locations is globlally unique,
	# and is updated the using the same /locations/{ID} PUT Endpoint
 
	print("\n\n ##########  GET LOCATION ID (TO UPDATE)  ##########\n\n")	

	location_id = int()
	for item in location_resp.json():
		if location_name == item['name']:
			print("\n\n ##########  FOUND LOCATION  NAME  ##########\n\n")
			location_id = z.extract_id_from_response(item)
			loc_obj = item
	if not location_id:
		print("\n\n *****  ERROR - LOCATION NOT FOUND  *****n\n")
		exit()


	# Update the location object with the changes, in this case Gateway Options.
	update_body = {**loc_obj, **gateway_options}

	# Update the location
	z.update_location_by_id(
		location_id,
		update_body
	)

	# Activate change
	print("\n\n ##########  ACTIVATE CHANGES  ##########\n\n")	
	z.activate()

	# Get Locations 
	print("\n\n ##########  GET LOCATION (AFTER)  ##########\n\n")	
	z.get_locations_by_id(location_id)


if __name__ == '__main__':
	main()
