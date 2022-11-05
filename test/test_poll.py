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
from twitter.models.poll import Poll  # noqa: E501
from twitter.rest import ApiException

class TestPoll(unittest.TestCase):
    """Poll unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Poll
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = twitter.models.poll.Poll()  # noqa: E501
        if include_optional :
            return Poll(
                duration_minutes = 5, 
                end_datetime = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                id = '1365059861688410112', 
                options = [
                    twitter.models.poll_option.PollOption(
                        label = '0', 
                        position = 56, 
                        votes = 56, )
                    ], 
                voting_status = 'open'
            )
        else :
            return Poll(
                id = '1365059861688410112',
                options = [
                    twitter.models.poll_option.PollOption(
                        label = '0', 
                        position = 56, 
                        votes = 56, )
                    ],
        )

    def testPoll(self):
        """Test Poll"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
