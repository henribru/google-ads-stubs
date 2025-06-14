import proto
from _typeshed import Incomplete
from google.ads.googleads.v20.enums.types import response_content_type as gage_response_content_type
from google.ads.googleads.v20.resources.types import ad_group_asset_set as gagr_ad_group_asset_set
from google.rpc import status_pb2
from typing import MutableSequence

__protobuf__: Incomplete

class MutateAdGroupAssetSetsRequest(proto.Message):
    customer_id: str
    operations: MutableSequence['AdGroupAssetSetOperation']
    partial_failure: bool
    validate_only: bool
    response_content_type: gage_response_content_type.ResponseContentTypeEnum.ResponseContentType

class AdGroupAssetSetOperation(proto.Message):
    create: gagr_ad_group_asset_set.AdGroupAssetSet
    remove: str

class MutateAdGroupAssetSetsResponse(proto.Message):
    results: MutableSequence['MutateAdGroupAssetSetResult']
    partial_failure_error: status_pb2.Status

class MutateAdGroupAssetSetResult(proto.Message):
    resource_name: str
    ad_group_asset_set: gagr_ad_group_asset_set.AdGroupAssetSet
