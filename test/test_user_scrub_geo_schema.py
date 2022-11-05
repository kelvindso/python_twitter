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
from twitter.models.user_scrub_geo_schema import UserScrubGeoSchema  # noqa: E501
from twitter.rest import ApiException

class TestUserScrubGeoSchema(unittest.TestCase):
    """UserScrubGeoSchema unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test UserScrubGeoSchema
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = twitter.models.user_scrub_geo_schema.UserScrubGeoSchema()  # noqa: E501
        if include_optional :
            return UserScrubGeoSchema(
                scrub_geo = twitter.models.user_scrub_geo_object_schema.UserScrubGeoObjectSchema(
                    event_at = '2021-07-06T18:40:40Z', 
                    up_to_tweet_id = '1346889436626259968', 
                    user = twitter.models.user_compliance_schema_user.UserComplianceSchema_user(
                        id = '2244994945', ), )
            )
        else :
            return UserScrubGeoSchema(
                scrub_geo = twitter.models.user_scrub_geo_object_schema.UserScrubGeoObjectSchema(
                    event_at = '2021-07-06T18:40:40Z', 
                    up_to_tweet_id = '1346889436626259968', 
                    user = twitter.models.user_compliance_schema_user.UserComplianceSchema_user(
                        id = '2244994945', ), ),
        )

    def testUserScrubGeoSchema(self):
        """Test UserScrubGeoSchema"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()