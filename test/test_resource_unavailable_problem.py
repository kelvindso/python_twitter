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
from twitter.models.resource_unavailable_problem import ResourceUnavailableProblem  # noqa: E501
from twitter.rest import ApiException

class TestResourceUnavailableProblem(unittest.TestCase):
    """ResourceUnavailableProblem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ResourceUnavailableProblem
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = twitter.models.resource_unavailable_problem.ResourceUnavailableProblem()  # noqa: E501
        if include_optional :
            return ResourceUnavailableProblem(
                parameter = '0', 
                resource_id = '', 
                resource_type = 'user'
            )
        else :
            return ResourceUnavailableProblem(
                parameter = '0',
                resource_id = '',
                resource_type = 'user',
        )

    def testResourceUnavailableProblem(self):
        """Test ResourceUnavailableProblem"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
