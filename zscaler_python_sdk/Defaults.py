global Z_CLOUDS, DEBUG_DEFAULT, MAX_FQDN_LEN, MAX_PSK_LEN, REQUEST_TIMEOUTS

DEBUG_DEFAULT    = False
MAX_FQDN_LEN     = 255
MAX_PSK_LEN      = 64
REQUEST_TIMEOUTS = (5, 25)

Z_CLOUDS = {
	'zscaler'      : 'https://admin.zscaler.net/',
	'zscloud'      : 'https://admin.zscloud.net/',
	'zscalerone'   : 'https://admin.zscalerone.net/',
	'zscalertwo'   : 'https://admin.zscalertwo.net/',
	'zscalerthree' : 'https://admin.zscalerthree.net/',
	'betacloud'    : 'https://admin.zscalerbeta.net/'	
}
