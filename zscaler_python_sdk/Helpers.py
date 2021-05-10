
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
