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
from twitter.models.tweet import Tweet  # noqa: E501
from twitter.rest import ApiException

class TestTweet(unittest.TestCase):
    """Tweet unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Tweet
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = twitter.models.tweet.Tweet()  # noqa: E501
        if include_optional :
            return Tweet(
                attachments = twitter.models.tweet_attachments.Tweet_attachments(
                    media_keys = [
                        '4_072888001528021798096225500850762068629'
                        ], 
                    poll_ids = [
                        '1365059861688410112'
                        ], ), 
                author_id = '2244994945', 
                context_annotations = [
                    twitter.models.context_annotation.ContextAnnotation(
                        domain = twitter.models.context_annotation_domain_fields.ContextAnnotationDomainFields(
                            description = '', 
                            id = '4807288800152802', 
                            name = '', ), 
                        entity = twitter.models.context_annotation_entity_fields.ContextAnnotationEntityFields(
                            description = '', 
                            id = '4807288800152802', 
                            name = '', ), )
                    ], 
                conversation_id = '1346889436626259968', 
                created_at = '2021-01-06T18:40:40Z', 
                entities = twitter.models.full_text_entities.FullTextEntities(
                    annotations = [
                        null
                        ], 
                    cashtags = [
                        null
                        ], 
                    hashtags = [
                        null
                        ], 
                    mentions = [
                        null
                        ], 
                    urls = [
                        null
                        ], ), 
                geo = twitter.models.tweet_geo.Tweet_geo(
                    coordinates = twitter.models.point.Point(
                        coordinates = [-105.18816086351444,40.247749999999996], 
                        type = 'Point', ), 
                    place_id = 'f7eb2fa2fea288b1', ), 
                id = '1346889436626259968', 
                in_reply_to_user_id = '2244994945', 
                lang = 'en', 
                non_public_metrics = twitter.models.tweet_non_public_metrics.Tweet_non_public_metrics(
                    impression_count = 56, ), 
                organic_metrics = twitter.models.tweet_organic_metrics.Tweet_organic_metrics(
                    impression_count = 56, 
                    like_count = 56, 
                    reply_count = 56, 
                    retweet_count = 56, ), 
                possibly_sensitive = False, 
                promoted_metrics = twitter.models.tweet_promoted_metrics.Tweet_promoted_metrics(
                    impression_count = 56, 
                    like_count = 56, 
                    reply_count = 56, 
                    retweet_count = 56, ), 
                public_metrics = twitter.models.tweet_public_metrics.Tweet_public_metrics(
                    like_count = 56, 
                    quote_count = 56, 
                    reply_count = 56, 
                    retweet_count = 56, ), 
                referenced_tweets = [
                    twitter.models.tweet_referenced_tweets_inner.Tweet_referenced_tweets_inner(
                        id = '1346889436626259968', 
                        type = 'retweeted', )
                    ], 
                reply_settings = 'everyone', 
                source = '', 
                text = 'Learn how to use the user Tweet timeline and user mention timeline endpoints in the Twitter API v2 to explore Tweet\u2026 https:\/\/t.co\/56a0vZUx7i', 
                withheld = twitter.models.tweet_withheld.TweetWithheld(
                    copyright = True, 
                    country_codes = [
                        'US'
                        ], 
                    scope = 'tweet', )
            )
        else :
            return Tweet(
                id = '1346889436626259968',
                text = 'Learn how to use the user Tweet timeline and user mention timeline endpoints in the Twitter API v2 to explore Tweet\u2026 https:\/\/t.co\/56a0vZUx7i',
        )

    def testTweet(self):
        """Test Tweet"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
