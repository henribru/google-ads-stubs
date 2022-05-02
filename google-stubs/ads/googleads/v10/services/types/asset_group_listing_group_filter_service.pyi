import proto
from _typeshed import Incomplete
from google.protobuf import field_mask_pb2 as field_mask_pb2

__protobuf__: Incomplete

class MutateAssetGroupListingGroupFiltersRequest(proto.Message):
    customer_id: Incomplete
    operations: Incomplete
    validate_only: Incomplete
    response_content_type: Incomplete

class AssetGroupListingGroupFilterOperation(proto.Message):
    update_mask: Incomplete
    create: Incomplete
    update: Incomplete
    remove: Incomplete

class MutateAssetGroupListingGroupFiltersResponse(proto.Message):
    results: Incomplete

class MutateAssetGroupListingGroupFilterResult(proto.Message):
    resource_name: Incomplete
    asset_group_listing_group_filter: Incomplete
