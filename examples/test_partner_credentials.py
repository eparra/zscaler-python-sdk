# -*- coding: utf-8 -*-

import zscaler_python_sdk


def main():


	print("\n\n ##########  STARTING SDK ##########\n\n")
	z = zscaler_python_sdk.zscaler()
	z.get_zia_partner_creds_from_env(True)
	z.set_cloud('betacloud')
	z.authenticate_partner_api()

	
if __name__ == '__main__':
	main()
