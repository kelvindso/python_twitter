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
from twitter.models.invalid_request_problem_all_of import InvalidRequestProblemAllOf  # noqa: E501
from twitter.rest import ApiException

class TestInvalidRequestProblemAllOf(unittest.TestCase):
    """InvalidRequestProblemAllOf unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test InvalidRequestProblemAllOf
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = twitter.models.invalid_request_problem_all_of.InvalidRequestProblemAllOf()  # noqa: E501
        if include_optional :
            return InvalidRequestProblemAllOf(
                errors = [
                    twitter.models.invalid_request_problem_all_of_errors.InvalidRequestProblem_allOf_errors(
                        message = '', 
                        parameters = {
                            'key' : [
                                ''
                                ]
                            }, )
                    ]
            )
        else :
            return InvalidRequestProblemAllOf(
        )

    def testInvalidRequestProblemAllOf(self):
        """Test InvalidRequestProblemAllOf"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
