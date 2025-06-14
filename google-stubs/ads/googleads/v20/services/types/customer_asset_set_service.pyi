import proto
from _typeshed import Incomplete
from google.ads.googleads.v20.enums.types import response_content_type as gage_response_content_type
from google.ads.googleads.v20.resources.types import customer_asset_set as gagr_customer_asset_set
from google.rpc import status_pb2
from typing import MutableSequence

__protobuf__: Incomplete

class MutateCustomerAssetSetsRequest(proto.Message):
    customer_id: str
    operations: MutableSequence['CustomerAssetSetOperation']
    partial_failure: bool
    validate_only: bool
    response_content_type: gage_response_content_type.ResponseContentTypeEnum.ResponseContentType

class CustomerAssetSetOperation(proto.Message):
    create: gagr_customer_asset_set.CustomerAssetSet
    remove: str

class MutateCustomerAssetSetsResponse(proto.Message):
    results: MutableSequence['MutateCustomerAssetSetResult']
    partial_failure_error: status_pb2.Status

class MutateCustomerAssetSetResult(proto.Message):
    resource_name: str
    customer_asset_set: gagr_customer_asset_set.CustomerAssetSet
