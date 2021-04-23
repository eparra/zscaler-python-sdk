global Z_CLOUDS, DEBUG_DEFAULT, MAX_FQDN_LEN, MAX_PSK_LEN, REQUEST_TIMEOUTS

DEBUG_DEFAULT    = False
MAX_FQDN_LEN     = 255
MAX_PSK_LEN      = 64
REQUEST_TIMEOUTS = (5, 25)

Z_CLOUDS = {
	'zscaler'      : 'https://zsapi.zscaler.net/',
	'zscloud'      : 'https://zsapi.zscloud.net/',
	'zscalerone'   : 'https://zsapi.zscalerone.net/',
	'zscalertwo'   : 'https://zsapi.zscalertwo.net/',
	'zscalerthree' : 'https://zsapi.zscalerthree.net/',
	'betacloud'    : 'https://zsapi.zscalerbeta.net/',	
	'govcloud'     : 'https://admin.zscalergov.net/'
}
