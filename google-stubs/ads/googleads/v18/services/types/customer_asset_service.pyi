import proto
from _typeshed import Incomplete
from google.ads.googleads.v18.enums.types import response_content_type as gage_response_content_type
from google.ads.googleads.v18.resources.types import customer_asset as gagr_customer_asset
from google.protobuf import field_mask_pb2
from google.rpc import status_pb2
from typing import MutableSequence

__protobuf__: Incomplete

class MutateCustomerAssetsRequest(proto.Message):
    customer_id: str
    operations: MutableSequence['CustomerAssetOperation']
    partial_failure: bool
    validate_only: bool
    response_content_type: gage_response_content_type.ResponseContentTypeEnum.ResponseContentType

class CustomerAssetOperation(proto.Message):
    update_mask: field_mask_pb2.FieldMask
    create: gagr_customer_asset.CustomerAsset
    update: gagr_customer_asset.CustomerAsset
    remove: str

class MutateCustomerAssetsResponse(proto.Message):
    partial_failure_error: status_pb2.Status
    results: MutableSequence['MutateCustomerAssetResult']

class MutateCustomerAssetResult(proto.Message):
    resource_name: str
    customer_asset: gagr_customer_asset.CustomerAsset
