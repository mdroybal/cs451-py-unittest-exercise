# geolocwrapper.py

from geopy.distance import distance
from geopy.geocoders import Nominatim
from geopy.exc import GeopyError


class GeoLocWrapper:
    """A class that wraps a limited set of utilities around a geopy Location object. Class provides an API for handling operations on a specific geopy.location.Location object.

    https://geopy.readthedocs.io/en/stable/    
    """

    def __init__(self, addr_str='',dest_addr_str=''):
        """Create a new GeoLocWrapper object that creates a connection to 
        Nominatum geo web service and initializes a geopy location object from
        an address string.

        Consider: What happens if the geolocator cannot locate geographic 
        location from addr_str? Raise a GeopyError exception!
        """        
        self.geolocator = Nominatim(user_agent="test-application") 
        self.location = self.geolocator.geocode(addr_str)
        self.locB = self.geolocator.geocode(dest_addr_str)

        if self.location == None:        
            raise GeopyError


        self.coordinates = (self.location.latitude,self.location.longitude)

        self.coorB = (self.locB.latitude,self.locB.longitude)
        
    def get_distance_miles(self):
        """Returns the geodisic distance in miles from location and 
        dest_addr_str.

        Consider: What happens if the geolocator cannot locate geographic 
        location from dest_addr_str?
        """
        return (distance(self.coordinates,self.coorB).miles)


    def get_distance_kilometers(self):
        """Returns the geodisic distance in kilometers from location and 
        dest_addr_str.
        
        Consider: What happens if the geolocator cannot locate geographic 
        location from dest_addr_str?
        """
        return (distance(self.coordinates,self.coorB).km)

