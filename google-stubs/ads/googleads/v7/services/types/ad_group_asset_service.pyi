from typing import Any

import proto

from google.ads.googleads.v7.resources.types import ad_group_asset as ad_group_asset

__protobuf__: Any

class GetAdGroupAssetRequest(proto.Message):
    resource_name: Any

class MutateAdGroupAssetsRequest(proto.Message):
    customer_id: Any
    operations: Any
    partial_failure: Any
    validate_only: Any

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
