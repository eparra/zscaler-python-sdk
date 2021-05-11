
import logging
from .Defaults import *


class Sandbox(object):

    def _do_get_sanbox_report_md5(self, md5hash, report_type):

        uri = '{}api/v1/sandbox/report/{}'.format(
            self.api_url,
            str(md5hash)
            )

        if report_type == 'FULL':
            uri += '?details=full'
        else:
            uri += '?details=summary'

        res = self._perform_get_request(
            uri,
            self._set_header(self.jsessionid)
        )

        if 'Retry-After' in res.json():
            if self.debug:
                logging.error("Zscaler RATE LIMIT REACHED")
                return None
        else:
            return res.json()


    def get_sanbox_report_md5(self, md5hash):

        res = self._do_get_sanbox_report_md5(md5hash, 'FULL')
        return res


    def get_sanbox_report_md5_summary(self, md5hash):

        res = self._do_get_sanbox_report_md5(md5hash, 'SUMMARY')
        return res


    def get_sanbox_report_sha1(self):
        pass


    def get_sanbox_report_sha256(self):
        pass


    def is_md5hash_suspicious(self, report):

        extrated = (self.extract_values(report, 'Type'))
        if 'SUSPICIOUS' in extrated:
            return True
        else:
            return False
        

    def is_md5hash_malicious(self, report):

        extrated = (self.extract_values(report, 'Type'))
        if 'MALICIOUS' in extrated:
            return True
        else:
            return False
