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
from twitter.models.tweet_public_metrics import TweetPublicMetrics  # noqa: E501
from twitter.rest import ApiException

class TestTweetPublicMetrics(unittest.TestCase):
    """TweetPublicMetrics unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test TweetPublicMetrics
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = twitter.models.tweet_public_metrics.TweetPublicMetrics()  # noqa: E501
        if include_optional :
            return TweetPublicMetrics(
                like_count = 56, 
                quote_count = 56, 
                reply_count = 56, 
                retweet_count = 56
            )
        else :
            return TweetPublicMetrics(
                like_count = 56,
                reply_count = 56,
                retweet_count = 56,
        )

    def testTweetPublicMetrics(self):
        """Test TweetPublicMetrics"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
