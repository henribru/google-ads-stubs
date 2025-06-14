import proto
from _typeshed import Incomplete
from google.ads.googleads.v20.resources.types import asset_group
from google.protobuf import field_mask_pb2
from google.rpc import status_pb2
from typing import MutableSequence

__protobuf__: Incomplete

class MutateAssetGroupsRequest(proto.Message):
    customer_id: str
    operations: MutableSequence['AssetGroupOperation']
    validate_only: bool

class AssetGroupOperation(proto.Message):
    update_mask: field_mask_pb2.FieldMask
    create: asset_group.AssetGroup
    update: asset_group.AssetGroup
    remove: str

class MutateAssetGroupsResponse(proto.Message):
    results: MutableSequence['MutateAssetGroupResult']
    partial_failure_error: status_pb2.Status

class MutateAssetGroupResult(proto.Message):
    resource_name: str
