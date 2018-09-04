# Zscaler Python SDK 

This is a Python SDK for Zscaler Internet Access.  This client library is designed to support the Zscaler Internet Access (ZIA) [API](https://help.zscaler.com/zia/about-api) and [SD-WAN API](https://help.zscaler.com/zia/sd-wan-api-integration) (aka "Partner API").  All API referecnes can be found here [[LINK](https://help.zscaler.com/zia/api)].  

This SDK has been developed mainly using Python 3.5.x on Mac OSX and Ubuntu 18.04.1 LTS (Bionic Beaver).  

**NOTE:** This repository will experience frequent updates.  To minimize breakage, public method names will not change.  If you run into any defects, please open issues [[HERE.](https://github.com/eparra/zscaler-python-sdk/issues)]   

## Quick Start 

1) Set Environment Variables.   
 
```$ <text-editor> ~/.bash_profile 
export ZIA_USERNAME="<ZIA-ADMIN-USER-ID>"
export ZIA_PASSWORD="<ZIA-ADMIN-USER-PASSWORD>"
export ZIA_API="<ZIA-API-KEY>" 

export PARTNER_USERNAME="<ZIA-PARTNER-ADMIN-USER-ID>"
export PARTNER_PASSWORD="<ZIA-PARTNER-ADMIN-USER-PASSWORD>"
export PARTNER_API="<PARTNER-API-KEY>"
```
        
2) Clone Repository (OS must have git installed).

```
$ git clone https://github.com/eparra/zscaler-python-sdk.git
$ cd zscaler-python-sdk/
```

3) Install SDK requirements

```
$ pip3 install -r requirements.txt
...
```

4) Install SDK

```
$ python3 setup.py install
...
```

5) Check out examples

```
$ ls examples/
...
```

## API Support

### ZIA API

#### Supported

* **Security Policy Settings**
* **Activate**

#### Future Release

* _Admin Audit Logs_
* _User Management_
* _SSL Inspection Settings_
* _URL Categories_
* _Sandbox Report_

### SD-WAN (Partner) API

* **VPN Credentials**
* **Locations**
* **Activate**


## Licensing

This work is released under the MIT license. A copy of the license is provided in the [LICENSE](https://github.com/eparra/zscaler-python-sdk/blob/master/LICENSE) file.

## Reporting Issues

If you have bugs or other issues specifically pertaining to this library, file them [here](https://github.com/eparra/zscaler-python-sdk/issues).

## References

* https://help.zscaler.com/zia/api
* https://help.zscaler.com/zia/zscaler-api-developer-guide
* https://help.zscaler.com/zia/sd-wan-api-integration
