
import requests
import platform
import logging
import time


__version_tuple__ = (0,0,6)
__version__       = '.'.join(map(str, __version_tuple__))
__email__         = 'NO EMAIL'
__author__        = "Eddie Parra <{0}>".format(__email__)
__copyright__     = "{0}, {1}".format(time.strftime('%Y'), __author__)
__maintainer__    = __author__
__license__       = "BSD"
__status__        = "Alpha"


from .Activation import Activation
from .Auth import Auth
from .Datacenters import Datacenters
from .Gre import Gre
from .Helpers import Helpers
from .Locations import Locations
from .Sandbox import Sandbox
from .Session import Session
from .Security import Security
from .Ssl import Ssl
from .User import User
from .VpnCredentials import VpnCredentials


logging.basicConfig(
	level   = logging.DEBUG, 
	format  = '%(asctime)s - %(message)s',
	datefmt = '%m/%d/%Y %I:%M:%S %p'
	) 


class zscaler(Activation, Auth, Datacenters, Gre, Helpers, Locations, Sandbox, Session, Security, Ssl, User, VpnCredentials):


	def __init__(self):

		self.session = requests.Session()

		self.user_agent = 'ZscalerSDK/%s Python/%s %s/%s' % (
			__version__,
			platform.python_version(),
			platform.system(),
			platform.release()
		)
