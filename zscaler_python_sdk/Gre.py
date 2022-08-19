
import logging
from .Defaults import *


class Gre(object):
    
    
    def get_all_gre_tunnels(self):

        uri = '{}api/v1/greTunnels'.format(
            self.api_url,
            )

        res = self._perform_get_request(
            uri,
            self._set_header(self.jsessionid)
        )
        return res
        

    def get_all_gre_vips(self):

        uri = '{}api/v1/staticIP?availableForGreTunnel=true'.format(
            self.api_url,
            )

        res = self._perform_get_request(
            uri,
            self._set_header(self.jsessionid)
        )
        return res

        
    def create_static_ip(self, static_ip, **data):
        
        latitude = data.get('latitude')
        longitude = data.get('longitude')
        geoOverride = data.get('geoOverride')
        
        uri = self.api_url + 'api/v1/staticIP'
    
        if not static_ip:
            if self.debug:
                logging.error("ERROR: {}".format("No IP Address Provided"))
                return 'No IP Address Provided'        

        # To manually set geolocation of static IP the geoOverride parameter must be passed
        # if not, then lat / long will be ignored.
        if geoOverride == True:
            if not latitude:
                if self.debug:
                    logging.error("ERROR: {}".format("No Latitude Provided"))
                return 'No Latitude Provided'   

            if not longitude:
                if self.debug:
                    logging.error("ERROR: {}".format("No Longitude Provided"))
                return 'No Longitude Provided'   
    
            body = {
                'ipAddress' : static_ip,
                'latitude'  : latitude, 
                'longitude' : longitude,
                'geoOverride': geoOverride
            }
        else:
            body = {
                'ipAddress' : static_ip
            }

        res = self._perform_post_request(
            uri,
            body,
            self._set_header(self.jsessionid)
        )
        return res
        
        
    def create_gre_tunnel(self, sourceIp, primaryVip, secondaryVip, comment = "", ipUnnumbered = True, domesticPreference = False):
        
        uri = '{}api/v1/greTunnels'.format(
            self.api_url,
            )
    
        if not sourceIp:
            if self.debug:
                logging.error("ERROR: {}".format("No IP Address Provided"))
            return 'No IP Address Provided'        

        if not primaryVip:
            if self.debug:
                logging.error("ERROR: {}".format("No Primary VIP Provided"))
            return 'No Primary VIP Provided'   

        if not secondaryVip:
            if self.debug:
                logging.error("ERROR: {}".format("No Secondary VIP Provided"))
            return 'No Secondary VIP Provided' 
    
        body = {
            'sourceIp'         : sourceIp,
            'primaryDestVip'   : {
                "id" : primaryVip
            },
            'secondaryDestVip' : {
                "id" : secondaryVip          
            },   
            'comment'       : comment,
            'ipUnnumbered'  : ipUnnumbered,
            'withinCountry' : domesticPreference,
        }

        res = self._perform_post_request(
            uri,
            body,
            self._set_header(self.jsessionid)
        )
        return res


    def get_gre_vips(self, source_ip, **data):

        latitude = data.get('latitude')
        longitude = data.get('longitude')

        if (latitude or longitude) and not (latitude and longitude):
            if self.debug:
                logging.error("ERROR: {}".format("Must include both Lat and Long for proximity lookup"))
                return 'Must include both Lat and Long for proximity lookup'        

        #When using geoOverride you must pass the coordinates in order to get the proper lookups for the closest DC's
        if (latitude and longitude):
            uri = '{}api/v1/vips/groupByDatacenter?sourceIp={}&latitude={}&longitude={}'.format(
                self.api_url,
                source_ip,
                latitude,
                longitude
                )
        
        else:
            uri = '{}api/v1/vips/groupByDatacenter?sourceIp={}'.format(
                self.api_url,
                source_ip
                )

        res = self._perform_get_request(
            uri,
            self._set_header(self.jsessionid)
        )
        return res           
        
