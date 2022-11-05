# TweetCreateRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**direct_message_deep_link** | **str** | Link to take the conversation from the public timeline to a private Direct Message. | [optional] 
**for_super_followers_only** | **bool** | Exclusive Tweet for super followers. | [optional] [default to False]
**geo** | [**TweetCreateRequestGeo**](TweetCreateRequestGeo.md) |  | [optional] 
**media** | [**TweetCreateRequestMedia**](TweetCreateRequestMedia.md) |  | [optional] 
**poll** | [**TweetCreateRequestPoll**](TweetCreateRequestPoll.md) |  | [optional] 
**quote_tweet_id** | **str** | Unique identifier of this Tweet. This is returned as a string in order to avoid complications with languages and tools that cannot handle large integers. | [optional] 
**reply** | [**TweetCreateRequestReply**](TweetCreateRequestReply.md) |  | [optional] 
**reply_settings** | **str** | Settings to indicate who can reply to the Tweet. | [optional] 
**text** | **str** | The content of the Tweet. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


