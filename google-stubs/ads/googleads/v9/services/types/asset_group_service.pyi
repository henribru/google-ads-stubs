from typing import Any

import proto
from google.protobuf import field_mask_pb2 as field_mask_pb2
from google.rpc import status_pb2 as status_pb2

from google.ads.googleads.v9.resources.types import asset_group as asset_group

__protobuf__: Any

class GetAssetGroupRequest(proto.Message):
    resource_name: Any

class MutateAssetGroupsRequest(proto.Message):
    customer_id: Any
    operations: Any
    validate_only: Any

class AssetGroupOperation(proto.Message):
    update_mask: Any
    create: Any
    update: Any
    remove: Any

class MutateAssetGroupsResponse(proto.Message):
    results: Any
    partial_failure_error: Any

class MutateAssetGroupResult(proto.Message):
    resource_name: Any
