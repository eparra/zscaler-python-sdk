
import requests
import platform
import logging
import time


__version_tuple__ = (0,0,4)
__version__       = '.'.join(map(str, __version_tuple__))
__email__         = 'NO EMAIL'
__author__        = "Eddie Parra <{0}>".format(__email__)
__copyright__     = "{0}, {1}".format(time.strftime('%Y'), __author__)
__maintainer__    = __author__
__license__       = "BSD"
__status__        = "Alpha"


from .Session import Session
from .Auth import Auth
from .VpnCredentials import VpnCredentials
from .Locations import Locations
from .User import User
from .Security import Security
from .Ssl import Ssl
from .Activation import Activation
from .Sandbox import Sandbox
from .Helpers import Helpers


logging.basicConfig(level=logging.DEBUG, 
	format='%(asctime)s - %(message)s',
	datefmt='%m/%d/%Y %I:%M:%S %p'
	) 


class zscaler(Session, Auth, Locations, VpnCredentials, User, Security, Ssl, Activation, Sandbox, Helpers): 

	def __init__(self):

		self.session = requests.Session()

		self.user_agent = 'ZscalerSDK/%s Python/%s %s/%s' % (
			__version__,
			platform.python_version(),
			platform.system(),
			platform.release()
		)
