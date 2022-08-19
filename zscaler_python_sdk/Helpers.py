
import logging
import json
from .Defaults import *


class Helpers(object):


    def extract_values(self, obj, key):

        arr = []

        def extract(obj, arr, key):

            if isinstance(obj, dict):
                for k, v in obj.items():
                    if isinstance(v, (dict, list)):
                        extract(v, arr, key)
                    elif k == key:
                        arr.append(v)
            elif isinstance(obj, list):
                for item in obj:
                    extract(item, arr, key)
            return arr

        results = extract(obj, arr, key)
        return results


    def extract_id_from_response(self, json_response):

        try:
            data = json.loads(json_response)
            if self.debug:
                logging.debug("Extractd ID: {}".format(data['id']))
            return data['id']
        except:
            logging.debug("Unable To Extract ID - EXITING\n\n")        
            exit()


    def extract_gre_vip_id_from_response(self, vip_priority, vips_data):
        
        try:
            data = json.loads(vips_data)
            if vip_priority == 'primary':
                vip_id = data[0]['greVips'][0]['id']
                if self.debug:
                    json_response = json.dumps(data[0], indent=4, separators=(',', ': '))
                    logging.debug("Extracted primary GRE VIP ID {}\nFrom Data Center:\n{}".format(
                        vip_id,
                        json_response)
                    )
            if vip_priority == 'secondary':
                vip_id = data[1]['greVips'][0]['id']
                if self.debug:
                    json_response = json.dumps(data[1], indent=4, separators=(',', ': '))
                    logging.debug("Extracted secondary GRE VIP ID {}\nFrom Data Center:\n{}".format(
                        vip_id,
                        json_response)
                    )
            return vip_id
        except:
            logging.debug("Unable To Extract GRE VIP ID - EXITING\n\n") 