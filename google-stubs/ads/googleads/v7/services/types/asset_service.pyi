from typing import Any

import proto

__protobuf__: Any

class GetAssetRequest(proto.Message):
    resource_name: Any

class MutateAssetsRequest(proto.Message):
    customer_id: Any
    operations: Any
    partial_failure: Any
    response_content_type: Any
    validate_only: Any

class AssetOperation(proto.Message):
    update_mask: Any
    create: Any
    update: Any

class MutateAssetsResponse(proto.Message):
    partial_failure_error: Any
    results: Any

class MutateAssetResult(proto.Message):
    resource_name: Any
    asset: Any
