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
	sub_location_name = 'Guest Wifi'

	print("\n\n ##########  STARTING SDK ##########\n\n")
	z = zscaler_python_sdk.zscaler()
	z.get_zia_partner_creds_from_env(True)
	z.set_cloud('betacloud')
	z.authenticate_partner_api()

	# Get Locations 
	print("\n\n ##########  GET LOCATIONS ##########\n\n")	

	location_resp = z.get_locations()

	# Get a Location ID from get_locations() output. After, use the
	# Location ID to get the sub-location ID.
	print("\n\n ##########  GET LOCATION ID (NEEDED TO DETERMINE SUB-LOCATION ID)  ##########\n\n")	

	location_id = int()
	for item in location_resp.json():
		if location_name == item['name']:
			print("\n\n ##########  FOUND LOCATION NAME  ##########\n\n")
			location_id = z.extract_id_from_response(item)
	if not location_id:
		print("\n\n *****  ERROR - LOCATION NOT FOUND  *****n\n")
		exit()

	print("\n\n ##########  GET SUB-LOCATION LIST FOR PARENT LOCATION  ##########\n\n")	

	# Get the list of sub-locations for the Parent location
	sub_location_resp = z.get_location_all_sub_locations(location_id)
 
	# Get the sub-location ID
	for sub_loc in sub_location_resp.json():
		if sub_location_name == sub_loc['name']:
			print("\n\n ##########  FOUND SUB-LOCATION ID  ##########\n\n")
			sub_location_id = z.extract_id_from_response(sub_loc)
			sub_loc_obj = sub_loc


 
 	# Update the location object with the changes, in this case Gateway Options.
	update_body = {**sub_loc_obj, **gateway_options}

	print("\n\n ##########  UPDATE SUB-LOCATION  ##########\n\n")	
 
	# The ID for Locations and Sub-Locations is globlally unique,
	# and is updated the using the same /locations/{ID} PUT Endpoint
 
 	# Update Sub-Location
	z.update_location_by_id(
 		sub_location_id,
		update_body
	)

	# Activate change
	print("\n\n ##########  ACTIVATE CHANGES  ##########\n\n")	
	z.activate()

	# Get Locations 
	print("\n\n ##########  GET LOCATION (AFTER)  ##########\n\n")	
	z.get_locations_by_id(sub_location_id)


if __name__ == '__main__':
	main()
