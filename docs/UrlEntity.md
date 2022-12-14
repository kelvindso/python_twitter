# UrlEntity

Represent the portion of text recognized as a URL, and its start and end position within the text.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end** | **int** | Index (zero-based) at which position this entity ends.  The index is exclusive. | 
**start** | **int** | Index (zero-based) at which position this entity starts.  The index is inclusive. | 
**description** | **str** | Description of the URL landing page. | [optional] 
**display_url** | **str** | The URL as displayed in the Twitter client. | [optional] 
**expanded_url** | **str** | A validly formatted URL. | [optional] 
**images** | [**List[UrlImage]**](UrlImage.md) |  | [optional] 
**media_key** | **str** | The Media Key identifier for this attachment. | [optional] 
**status** | **int** | HTTP Status Code. | [optional] 
**title** | **str** | Title of the page the URL points to. | [optional] 
**unwound_url** | **str** | Fully resolved url. | [optional] 
**url** | **str** | A validly formatted URL. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


