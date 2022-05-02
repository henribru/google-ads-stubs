import proto
from _typeshed import Incomplete
from google.protobuf import field_mask_pb2 as field_mask_pb2
from google.rpc import status_pb2 as status_pb2

__protobuf__: Incomplete

class MutateAdGroupAssetsRequest(proto.Message):
    customer_id: Incomplete
    operations: Incomplete
    partial_failure: Incomplete
    validate_only: Incomplete
    response_content_type: Incomplete

class AdGroupAssetOperation(proto.Message):
    update_mask: Incomplete
    create: Incomplete
    update: Incomplete
    remove: Incomplete

class MutateAdGroupAssetsResponse(proto.Message):
    partial_failure_error: Incomplete
    results: Incomplete

class MutateAdGroupAssetResult(proto.Message):
    resource_name: Incomplete
    ad_group_asset: Incomplete
