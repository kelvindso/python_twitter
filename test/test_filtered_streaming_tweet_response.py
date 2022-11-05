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
from twitter.models.filtered_streaming_tweet_response import FilteredStreamingTweetResponse  # noqa: E501
from twitter.rest import ApiException

class TestFilteredStreamingTweetResponse(unittest.TestCase):
    """FilteredStreamingTweetResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test FilteredStreamingTweetResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = twitter.models.filtered_streaming_tweet_response.FilteredStreamingTweetResponse()  # noqa: E501
        if include_optional :
            return FilteredStreamingTweetResponse(
                data = {"author_id":"2244994945","created_at":"Wed Jan 06 18:40:40 +0000 2021","id":"1346889436626259968","text":"Learn how to use the user Tweet timeline and user mention timeline endpoints in the Twitter API v2 to explore Tweet\\u2026 https:\\/\\/t.co\\/56a0vZUx7i"}, 
                errors = [
                    twitter.models.problem.Problem(
                        detail = '', 
                        status = 56, 
                        title = '', 
                        type = '', )
                    ], 
                includes = twitter.models.expansions.Expansions(
                    media = [
                        twitter.models.media.Media(
                            height = 0, 
                            media_key = '4_072888001528021798096225500850762068629', 
                            type = '', 
                            width = 0, )
                        ], 
                    places = [
                        twitter.models.place.Place(
                            contained_within = [
                                'f7eb2fa2fea288b1'
                                ], 
                            country = 'United States', 
                            country_code = 'US', 
                            full_name = 'Lakewood, CO', 
                            geo = twitter.models.geo.Geo(
                                bbox = [-105.193475,39.60973,-105.053164,39.761974], 
                                geometry = twitter.models.point.Point(
                                    coordinates = [-105.18816086351444,40.247749999999996], 
                                    type = 'Point', ), 
                                properties = twitter.models.properties.properties(), 
                                type = 'Feature', ), 
                            id = 'f7eb2fa2fea288b1', 
                            name = 'Lakewood', 
                            place_type = 'city', )
                        ], 
                    polls = [
                        twitter.models.poll.Poll(
                            duration_minutes = 5, 
                            end_datetime = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            id = '1365059861688410112', 
                            options = [
                                twitter.models.poll_option.PollOption(
                                    label = '0', 
                                    position = 56, 
                                    votes = 56, )
                                ], 
                            voting_status = 'open', )
                        ], 
                    topics = [
                        twitter.models.topic.Topic(
                            description = 'All about technology', 
                            id = '', 
                            name = 'Technology', )
                        ], 
                    tweets = [
                        {"author_id":"2244994945","created_at":"Wed Jan 06 18:40:40 +0000 2021","id":"1346889436626259968","text":"Learn how to use the user Tweet timeline and user mention timeline endpoints in the Twitter API v2 to explore Tweet\\u2026 https:\\/\\/t.co\\/56a0vZUx7i"}
                        ], 
                    users = [
                        {"created_at":"2013-12-14T04:35:55Z","id":"2244994945","name":"Twitter Dev","protected":false,"username":"TwitterDev"}
                        ], ), 
                matching_rules = [
                    twitter.models.filtered_streaming_tweet_response_matching_rules_inner.FilteredStreamingTweetResponse_matching_rules_inner(
                        id = '120897978112909812', 
                        tag = 'Non-retweeted coffee Tweets', )
                    ]
            )
        else :
            return FilteredStreamingTweetResponse(
        )

    def testFilteredStreamingTweetResponse(self):
        """Test FilteredStreamingTweetResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
