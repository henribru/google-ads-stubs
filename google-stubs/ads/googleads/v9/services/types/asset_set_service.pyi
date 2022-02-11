from typing import Any

import proto
from google.protobuf import field_mask_pb2 as field_mask_pb2
from google.rpc import status_pb2 as status_pb2

__protobuf__: Any

class MutateAssetSetsRequest(proto.Message):
    customer_id: Any
    operations: Any
    partial_failure: Any
    validate_only: Any
    response_content_type: Any

class AssetSetOperation(proto.Message):
    update_mask: Any
    create: Any
    update: Any
    remove: Any

class MutateAssetSetsResponse(proto.Message):
    results: Any
    partial_failure_error: Any

class MutateAssetSetResult(proto.Message):
    resource_name: Any
    asset_set: Any
