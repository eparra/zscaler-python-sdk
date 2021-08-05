global Z_CLOUDS, DEBUG_DEFAULT, MAX_FQDN_LEN, MAX_PSK_LEN, REQUEST_TIMEOUTS

DEBUG_DEFAULT               = False
MAX_FQDN_LENGTH             = 255
MAX_PSK_LENGTH              = 64
MIN_API_KEY_LENGTH          = 12
REQUEST_TIMEOUTS            = (5, 25)
LOCATION_DESCRIPTION_LENGTH = 1024

Z_CLOUDS = {
	'zscaler'      : 'https://zsapi.zscaler.net/',
	'zscloud'      : 'https://zsapi.zscloud.net/',
	'zscalerone'   : 'https://zsapi.zscalerone.net/',
	'zscalertwo'   : 'https://zsapi.zscalertwo.net/',
	'zscalerthree' : 'https://zsapi.zscalerthree.net/',	
	'govcloud'     : 'https://admin.zscalergov.net/',
	'betacloud'    : 'https://zsapi.zscalerbeta.net/',
	'zsdevel'      : 'https://zsapi.zsdevel.net/',	
	'zspreview'    : 'https://zsapi.zspreview.net/'	
}
