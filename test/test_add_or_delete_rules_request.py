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
from twitter.models.add_or_delete_rules_request import AddOrDeleteRulesRequest  # noqa: E501
from twitter.rest import ApiException

class TestAddOrDeleteRulesRequest(unittest.TestCase):
    """AddOrDeleteRulesRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test AddOrDeleteRulesRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = twitter.models.add_or_delete_rules_request.AddOrDeleteRulesRequest()  # noqa: E501
        if include_optional :
            return AddOrDeleteRulesRequest(
                add = [
                    twitter.models.rule_no_id.RuleNoId(
                        tag = 'Non-retweeted coffee Tweets', 
                        value = 'coffee -is:retweet', )
                    ], 
                delete = twitter.models.delete_rules_request_delete.DeleteRulesRequest_delete(
                    ids = [
                        '120897978112909812'
                        ], 
                    values = [
                        'coffee -is:retweet'
                        ], )
            )
        else :
            return AddOrDeleteRulesRequest(
                add = [
                    twitter.models.rule_no_id.RuleNoId(
                        tag = 'Non-retweeted coffee Tweets', 
                        value = 'coffee -is:retweet', )
                    ],
                delete = twitter.models.delete_rules_request_delete.DeleteRulesRequest_delete(
                    ids = [
                        '120897978112909812'
                        ], 
                    values = [
                        'coffee -is:retweet'
                        ], ),
        )

    def testAddOrDeleteRulesRequest(self):
        """Test AddOrDeleteRulesRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()