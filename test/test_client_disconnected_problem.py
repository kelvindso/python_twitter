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
from twitter.models.client_disconnected_problem import ClientDisconnectedProblem  # noqa: E501
from twitter.rest import ApiException

class TestClientDisconnectedProblem(unittest.TestCase):
    """ClientDisconnectedProblem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ClientDisconnectedProblem
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = twitter.models.client_disconnected_problem.ClientDisconnectedProblem()  # noqa: E501
        if include_optional :
            return ClientDisconnectedProblem(
            )
        else :
            return ClientDisconnectedProblem(
        )

    def testClientDisconnectedProblem(self):
        """Test ClientDisconnectedProblem"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
