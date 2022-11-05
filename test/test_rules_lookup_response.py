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
from twitter.models.rules_lookup_response import RulesLookupResponse  # noqa: E501
from twitter.rest import ApiException

class TestRulesLookupResponse(unittest.TestCase):
    """RulesLookupResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test RulesLookupResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = twitter.models.rules_lookup_response.RulesLookupResponse()  # noqa: E501
        if include_optional :
            return RulesLookupResponse(
                data = [
                    twitter.models.rule.Rule(
                        id = '120897978112909812', 
                        tag = 'Non-retweeted coffee Tweets', 
                        value = 'coffee -is:retweet', )
                    ], 
                meta = twitter.models.rules_response_metadata.RulesResponseMetadata(
                    next_token = '0', 
                    result_count = 56, 
                    sent = '', 
                    summary = null, )
            )
        else :
            return RulesLookupResponse(
                meta = twitter.models.rules_response_metadata.RulesResponseMetadata(
                    next_token = '0', 
                    result_count = 56, 
                    sent = '', 
                    summary = null, ),
        )

    def testRulesLookupResponse(self):
        """Test RulesLookupResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
