from typing import Any

import proto
from google.protobuf import field_mask_pb2 as field_mask_pb2

__protobuf__: Any

class MutateAssetGroupListingGroupFiltersRequest(proto.Message):
    customer_id: Any
    operations: Any
    validate_only: Any
    response_content_type: Any

class AssetGroupListingGroupFilterOperation(proto.Message):
    update_mask: Any
    create: Any
    update: Any
    remove: Any

class MutateAssetGroupListingGroupFiltersResponse(proto.Message):
    results: Any

class MutateAssetGroupListingGroupFilterResult(proto.Message):
    resource_name: Any
    asset_group_listing_group_filter: Any
