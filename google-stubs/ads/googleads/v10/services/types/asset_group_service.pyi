import proto
from _typeshed import Incomplete
from google.protobuf import field_mask_pb2 as field_mask_pb2
from google.rpc import status_pb2 as status_pb2

from google.ads.googleads.v10.resources.types import asset_group as asset_group

__protobuf__: Incomplete

class MutateAssetGroupsRequest(proto.Message):
    customer_id: Incomplete
    operations: Incomplete
    validate_only: Incomplete

class AssetGroupOperation(proto.Message):
    update_mask: Incomplete
    create: Incomplete
    update: Incomplete
    remove: Incomplete

class MutateAssetGroupsResponse(proto.Message):
    results: Incomplete
    partial_failure_error: Incomplete

class MutateAssetGroupResult(proto.Message):
    resource_name: Incomplete
