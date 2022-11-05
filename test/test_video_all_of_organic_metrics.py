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
from twitter.models.video_all_of_organic_metrics import VideoAllOfOrganicMetrics  # noqa: E501
from twitter.rest import ApiException

class TestVideoAllOfOrganicMetrics(unittest.TestCase):
    """VideoAllOfOrganicMetrics unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test VideoAllOfOrganicMetrics
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = twitter.models.video_all_of_organic_metrics.VideoAllOfOrganicMetrics()  # noqa: E501
        if include_optional :
            return VideoAllOfOrganicMetrics(
                playback_0_count = 56, 
                playback_100_count = 56, 
                playback_25_count = 56, 
                playback_50_count = 56, 
                playback_75_count = 56, 
                view_count = 56
            )
        else :
            return VideoAllOfOrganicMetrics(
        )

    def testVideoAllOfOrganicMetrics(self):
        """Test VideoAllOfOrganicMetrics"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()