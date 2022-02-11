from typing import Any

import proto
from google.protobuf import field_mask_pb2 as field_mask_pb2
from google.rpc import status_pb2 as status_pb2

__protobuf__: Any

class GetAdGroupAssetRequest(proto.Message):
    resource_name: Any

class MutateAdGroupAssetsRequest(proto.Message):
    customer_id: Any
    operations: Any
    partial_failure: Any
    validate_only: Any
    response_content_type: Any

class AdGroupAssetOperation(proto.Message):
    update_mask: Any
    create: Any
    update: Any
    remove: Any

class MutateAdGroupAssetsResponse(proto.Message):
    partial_failure_error: Any
    results: Any

class MutateAdGroupAssetResult(proto.Message):
    resource_name: Any
    ad_group_asset: Any
