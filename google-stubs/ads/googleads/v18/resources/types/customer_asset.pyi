import proto
from _typeshed import Incomplete
from google.ads.googleads.v18.common.types import asset_policy
from google.ads.googleads.v18.enums.types import asset_field_type, asset_link_primary_status, asset_link_primary_status_reason, asset_link_status, asset_source
from typing import MutableSequence

__protobuf__: Incomplete

class CustomerAsset(proto.Message):
    resource_name: str
    asset: str
    field_type: asset_field_type.AssetFieldTypeEnum.AssetFieldType
    source: asset_source.AssetSourceEnum.AssetSource
    status: asset_link_status.AssetLinkStatusEnum.AssetLinkStatus
    primary_status: asset_link_primary_status.AssetLinkPrimaryStatusEnum.AssetLinkPrimaryStatus
    primary_status_details: MutableSequence[asset_policy.AssetLinkPrimaryStatusDetails]
    primary_status_reasons: MutableSequence[asset_link_primary_status_reason.AssetLinkPrimaryStatusReasonEnum.AssetLinkPrimaryStatusReason]
