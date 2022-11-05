# User

The Twitter User object.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** | Creation time of this User. | [optional] 
**description** | **str** | The text of this User&#39;s profile description (also known as bio), if the User provided one. | [optional] 
**entities** | [**UserEntities**](UserEntities.md) |  | [optional] 
**id** | **str** | Unique identifier of this User. This is returned as a string in order to avoid complications with languages and tools that cannot handle large integers. | 
**location** | **str** | The location specified in the User&#39;s profile, if the User provided one. As this is a freeform value, it may not indicate a valid location, but it may be fuzzily evaluated when performing searches with location queries. | [optional] 
**name** | **str** | The friendly name of this User, as shown on their profile. | 
**pinned_tweet_id** | **str** | Unique identifier of this Tweet. This is returned as a string in order to avoid complications with languages and tools that cannot handle large integers. | [optional] 
**profile_image_url** | **str** | The URL to the profile image for this User. | [optional] 
**protected** | **bool** | Indicates if this User has chosen to protect their Tweets (in other words, if this User&#39;s Tweets are private). | [optional] 
**public_metrics** | [**UserPublicMetrics**](UserPublicMetrics.md) |  | [optional] 
**url** | **str** | The URL specified in the User&#39;s profile. | [optional] 
**username** | **str** | The Twitter handle (screen name) of this user. | 
**verified** | **bool** | Indicate if this User is a verified Twitter User. | [optional] 
**withheld** | [**UserWithheld**](UserWithheld.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


