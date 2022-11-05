# Tweet


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attachments** | [**TweetAttachments**](TweetAttachments.md) |  | [optional] 
**author_id** | **str** | Unique identifier of this User. This is returned as a string in order to avoid complications with languages and tools that cannot handle large integers. | [optional] 
**context_annotations** | [**List[ContextAnnotation]**](ContextAnnotation.md) |  | [optional] 
**conversation_id** | **str** | Unique identifier of this Tweet. This is returned as a string in order to avoid complications with languages and tools that cannot handle large integers. | [optional] 
**created_at** | **datetime** | Creation time of the Tweet. | [optional] 
**entities** | [**FullTextEntities**](FullTextEntities.md) |  | [optional] 
**geo** | [**TweetGeo**](TweetGeo.md) |  | [optional] 
**id** | **str** | Unique identifier of this Tweet. This is returned as a string in order to avoid complications with languages and tools that cannot handle large integers. | 
**in_reply_to_user_id** | **str** | Unique identifier of this User. This is returned as a string in order to avoid complications with languages and tools that cannot handle large integers. | [optional] 
**lang** | **str** | Language of the Tweet, if detected by Twitter. Returned as a BCP47 language tag. | [optional] 
**non_public_metrics** | [**TweetNonPublicMetrics**](TweetNonPublicMetrics.md) |  | [optional] 
**organic_metrics** | [**TweetOrganicMetrics**](TweetOrganicMetrics.md) |  | [optional] 
**possibly_sensitive** | **bool** | Indicates if this Tweet contains URLs marked as sensitive, for example content suitable for mature audiences. | [optional] 
**promoted_metrics** | [**TweetPromotedMetrics**](TweetPromotedMetrics.md) |  | [optional] 
**public_metrics** | [**TweetPublicMetrics**](TweetPublicMetrics.md) |  | [optional] 
**referenced_tweets** | [**List[TweetReferencedTweetsInner]**](TweetReferencedTweetsInner.md) | A list of Tweets this Tweet refers to. For example, if the parent Tweet is a Retweet, a Quoted Tweet or a Reply, it will include the related Tweet referenced to by its parent. | [optional] 
**reply_settings** | [**ReplySettings**](ReplySettings.md) |  | [optional] 
**source** | **str** | The name of the app the user Tweeted from. | [optional] 
**text** | **str** | The content of the Tweet. | 
**withheld** | [**TweetWithheld**](TweetWithheld.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


