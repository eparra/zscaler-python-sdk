# -*- coding: utf-8 -*-

import json
import time
import zscaler_python_sdk


def main():

	print("\n\n ##########  STARTING SDK  ##########\n\n")
	z = zscaler_python_sdk.zscaler()
	z.get_zia_creds_from_env(True)
	z.set_cloud('zscalerthree')
	z.authenticate_zia_api()

        # Query Known Benign MD5 hash
	print("\n\n ##########  Query Known Benign MD5 hash  ##########\n\n")
	query = z.get_sanbox_report_md5('d732eef37d941722c8b23221bf173161')

	# Query Known Malicious MD5 hash
	print("\n\n ##########  Query Known Malicious MD5 hash  ##########\n\n")
	query = z.get_sanbox_report_md5('1acd57deafcbc29617a15708f45c31f0')


if __name__ == '__main__':
	main()
