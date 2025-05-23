# -*- coding: utf-8 -*-

"""Example script used for manual testing.

The file name starts with ``test_`` so pytest tries to collect it. We skip it
during automated test runs.
"""

import pytest

pytest.skip("example only", allow_module_level=True)

import zscaler_python_sdk


def main():


	print("\n\n ##########  STARTING SDK ##########\n\n")
	z = zscaler_python_sdk.zscaler()
	z.get_zia_partner_creds_from_env(True)
	z.set_cloud('betacloud')
	z.authenticate_partner_api()

	
if __name__ == '__main__':
	main()
