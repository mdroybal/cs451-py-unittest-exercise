# test_geolocwrapper.py
import unittest

from geolocwrapper import GeoLocWrapper
from geopy.exc import GeopyError

class TestGeoLocWrapper(unittest.TestCase):
    """A collection of unit tests for the BabySet class. 
    Used to demonstrate and introduce unit testing in Python.
    Related docs: https://docs.python.org/3/library/unittest.html
    """
    def test_init(self):
        """Unit test for GeoLocWrapper constructor."""
        dist = GeoLocWrapper("1314 chavez st, las vegas, nm","1701 bryant st, denver, co")
        self.assertEqual(dist.location.latitude,35.5886169060276)

    def test_init_fail(self):
        with self.assertRaises(GeopyError):
        	dist = GeoLocWrapper()

    def test_get_distance_miles(self):
    	dist = GeoLocWrapper("1314 chavez st, las vegas, nm","1701 bryant st, denver, co")
    	self.assertEqual(dist.get_distance_miles(),286.80227495947776)

    def test_get_distance_kilometers(self):
    	dist = GeoLocWrapper("1314 chavez st, las vegas, nm","1701 bryant st, denver, co")
    	self.assertEqual(dist.get_distance_kilometers(),461.5635203923858 )

    # Begin adding your unit tests for the GeoLocWrapper module.

if __name__ == '__main__':
    unittest.main()