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
from twitter.models.users_following_delete_response import UsersFollowingDeleteResponse  # noqa: E501
from twitter.rest import ApiException

class TestUsersFollowingDeleteResponse(unittest.TestCase):
    """UsersFollowingDeleteResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test UsersFollowingDeleteResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = twitter.models.users_following_delete_response.UsersFollowingDeleteResponse()  # noqa: E501
        if include_optional :
            return UsersFollowingDeleteResponse(
                data = twitter.models.list_followed_response_data.ListFollowedResponse_data(
                    following = True, ), 
                errors = [
                    twitter.models.problem.Problem(
                        detail = '', 
                        status = 56, 
                        title = '', 
                        type = '', )
                    ]
            )
        else :
            return UsersFollowingDeleteResponse(
        )

    def testUsersFollowingDeleteResponse(self):
        """Test UsersFollowingDeleteResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()