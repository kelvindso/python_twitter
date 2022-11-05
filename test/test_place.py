# coding: utf-8

"""
    Twitter API v2

    Twitter API v2 available endpoints  # noqa: E501

    The version of the OpenAPI document: 2.49
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import twitter
from twitter.models.place import Place  # noqa: E501
from twitter.rest import ApiException

class TestPlace(unittest.TestCase):
    """Place unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Place
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = twitter.models.place.Place()  # noqa: E501
        if include_optional :
            return Place(
                contained_within = [
                    'f7eb2fa2fea288b1'
                    ], 
                country = 'United States', 
                country_code = 'US', 
                full_name = 'Lakewood, CO', 
                geo = twitter.models.geo.Geo(
                    bbox = [-105.193475,39.60973,-105.053164,39.761974], 
                    geometry = twitter.models.point.Point(
                        coordinates = [-105.18816086351444,40.247749999999996], 
                        type = 'Point', ), 
                    properties = twitter.models.properties.properties(), 
                    type = 'Feature', ), 
                id = 'f7eb2fa2fea288b1', 
                name = 'Lakewood', 
                place_type = 'city'
            )
        else :
            return Place(
                full_name = 'Lakewood, CO',
                id = 'f7eb2fa2fea288b1',
        )

    def testPlace(self):
        """Test Place"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
