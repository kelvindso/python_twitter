# ComplianceJob


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** | Creation time of the compliance job. | 
**download_expires_at** | **datetime** | Expiration time of the download URL. | 
**download_url** | **str** | URL from which the user will retrieve their compliance results. | 
**id** | **str** | Compliance Job ID. | 
**name** | **str** | User-provided name for a compliance job. | [optional] 
**status** | [**ComplianceJobStatus**](ComplianceJobStatus.md) |  | 
**type** | [**ComplianceJobType**](ComplianceJobType.md) |  | 
**upload_expires_at** | **datetime** | Expiration time of the upload URL. | 
**upload_url** | **str** | URL to which the user will upload their Tweet or user IDs. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


