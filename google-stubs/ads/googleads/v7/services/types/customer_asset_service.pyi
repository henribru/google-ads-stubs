from typing import Any

import proto

from google.ads.googleads.v7.resources.types import customer_asset as customer_asset

__protobuf__: Any

class GetCustomerAssetRequest(proto.Message):
    resource_name: Any

class MutateCustomerAssetsRequest(proto.Message):
    customer_id: Any
    operations: Any
    partial_failure: Any
    validate_only: Any

class CustomerAssetOperation(proto.Message):
    update_mask: Any
    create: Any
    update: Any
    remove: Any

class MutateCustomerAssetsResponse(proto.Message):
    partial_failure_error: Any
    results: Any

class MutateCustomerAssetResult(proto.Message):
    resource_name: Any
