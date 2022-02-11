from typing import Any

import proto
from google.rpc import status_pb2 as status_pb2

__protobuf__: Any

class MutateAssetSetAssetsRequest(proto.Message):
    customer_id: Any
    operations: Any
    partial_failure: Any
    validate_only: Any
    response_content_type: Any

class AssetSetAssetOperation(proto.Message):
    create: Any
    remove: Any

class MutateAssetSetAssetsResponse(proto.Message):
    results: Any
    partial_failure_error: Any

class MutateAssetSetAssetResult(proto.Message):
    resource_name: Any
    asset_set_asset: Any
