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
from twitter.models.tweet_promoted_metrics import TweetPromotedMetrics  # noqa: E501
from twitter.rest import ApiException

class TestTweetPromotedMetrics(unittest.TestCase):
    """TweetPromotedMetrics unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test TweetPromotedMetrics
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = twitter.models.tweet_promoted_metrics.TweetPromotedMetrics()  # noqa: E501
        if include_optional :
            return TweetPromotedMetrics(
                impression_count = 56, 
                like_count = 56, 
                reply_count = 56, 
                retweet_count = 56
            )
        else :
            return TweetPromotedMetrics(
        )

    def testTweetPromotedMetrics(self):
        """Test TweetPromotedMetrics"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()