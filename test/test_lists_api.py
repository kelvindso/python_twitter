# coding: utf-8

"""
    Twitter API v2

    Twitter API v2 available endpoints  # noqa: E501

    The version of the OpenAPI document: 2.49
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import twitter
from twitter.api.lists_api import ListsApi  # noqa: E501
from twitter.rest import ApiException


class TestListsApi(unittest.TestCase):
    """ListsApi unit test stubs"""

    def setUp(self):
        self.api = twitter.api.lists_api.ListsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_user_list_memberships(self):
        """Test case for get_user_list_memberships

        Get a User's List Memberships  # noqa: E501
        """
        pass

    def test_list_add_member(self):
        """Test case for list_add_member

        Add a List member  # noqa: E501
        """
        pass

    def test_list_id_create(self):
        """Test case for list_id_create

        Create List  # noqa: E501
        """
        pass

    def test_list_id_delete(self):
        """Test case for list_id_delete

        Delete List  # noqa: E501
        """
        pass

    def test_list_id_get(self):
        """Test case for list_id_get

        List lookup by List ID.  # noqa: E501
        """
        pass

    def test_list_id_update(self):
        """Test case for list_id_update

        Update List.  # noqa: E501
        """
        pass

    def test_list_remove_member(self):
        """Test case for list_remove_member

        Remove a List member  # noqa: E501
        """
        pass

    def test_list_user_follow(self):
        """Test case for list_user_follow

        Follow a List  # noqa: E501
        """
        pass

    def test_list_user_owned_lists(self):
        """Test case for list_user_owned_lists

        Get a User's Owned Lists.  # noqa: E501
        """
        pass

    def test_list_user_pin(self):
        """Test case for list_user_pin

        Pin a List  # noqa: E501
        """
        pass

    def test_list_user_pinned_lists(self):
        """Test case for list_user_pinned_lists

        Get a User's Pinned Lists  # noqa: E501
        """
        pass

    def test_list_user_unfollow(self):
        """Test case for list_user_unfollow

        Unfollow a List  # noqa: E501
        """
        pass

    def test_list_user_unpin(self):
        """Test case for list_user_unpin

        Unpin a List  # noqa: E501
        """
        pass

    def test_user_followed_lists(self):
        """Test case for user_followed_lists

        Get User's Followed Lists  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
