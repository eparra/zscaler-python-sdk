# Zscaler Python SDK 

This is a Python SDK for Zscaler Internet Access (ZIA).  This client library is designed to support the ZIA [API](https://help.zscaler.com/zia/zia-api) and ZIA [Partner API](https://help.zscaler.com/zia/sd-wan-api-integration) (aka "SD-WAN" API) in ZIA 6.1 or newer.  All ZIA API references can be found here [[LINK](https://help.zscaler.com/zia/zia-api)].  **PLEASE READ THE DOCUMENTATION BEFORE CONTACTING ZSCALER**

This SDK has been tested with Python 3.13.3 and is compatible with Python 3.8 and newer.

**NOTE:** This repository will experience frequent updates.  To minimize breakage, public method names will not change.  If you run into any defects, please open issues [[HERE.](https://github.com/eparra/zscaler-python-sdk/issues)]   

## Quick Start 

1) If you have not verified your credentials, we suggest starting [[HERE](https://help.zscaler.com/zia/configuring-postman-rest-api-client)], unless you are already familar with this API.

2) Set Environment Variables   
 
```
$ <text-editor> ~/.bash_profile 
export ZIA_USERNAME="<ZIA-ADMIN-USER-ID>"
export ZIA_PASSWORD="<ZIA-ADMIN-USER-PASSWORD>"
export ZIA_API="<ZIA-API-KEY>" 

export ZIA_PARTNER_USERNAME="<ZIA-PARTNER-ADMIN-USER-ID>"
export ZIA_PARTNER_PASSWORD="<ZIA-PARTNER-ADMIN-USER-PASSWORD>"
export ZIA_PARTNER_API="<ZIA-PARTNER-API-KEY>"
```

3) Setup Virtual Environment (optional)

```
python3 -m venv zscaler-sdk
cd zscaler-sdk 
source bin/activate
```
        
4) Clone Repository (OS must have git installed)

```
$ git clone https://github.com/eparra/zscaler-python-sdk.git
$ cd zscaler-python-sdk/
```

5) Install SDK

```
$ pip install .
...
```

6) Check out examples

```
$ ls examples/
...
```

## API Support

### SD-WAN (Partner) API

* **Locations**
* **VPN Credentials**
* **Static IP**
* **GRE Tunnels**


## Licensing

This work is released under the MIT license. A copy of the license is provided in the [LICENSE](https://github.com/eparra/zscaler-python-sdk/blob/master/LICENSE) file.

## Reporting Issues

If you have bugs or other issues specifically pertaining to this library, file them [here](https://github.com/eparra/zscaler-python-sdk/issues).

## References

* https://help.zscaler.com/zia/zia-api
* https://help.zscaler.com/zia/zia-api/api-developer-reference-guide
* https://help.zscaler.com/zia/sd-wan-api-integration

## Acknowledgments

Thanks to:

* [Sofian Halim](https://www.linkedin.com/in/sofian-halim-9237b25/)
* [Lidor Pergament](https://www.linkedin.com/in/lidorp/)
* [Paul Abbott](https://www.linkedin.com/in/paul-abbott-4b014/)

## Async Client (v2)

A new asynchronous client is provided under `zscaler_python_sdk.v2`. It uses `httpx` and dataclasses for configuration.

Example:
```python
from zscaler_python_sdk.v2 import ZscalerConfig, ZscalerAsyncClient

config = ZscalerConfig(username="user", password="pass", api_key="apikey")
client = ZscalerAsyncClient(config)
# await client.get("api/v1/some/resource")
```

