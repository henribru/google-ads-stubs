from typing import Any

import proto

from google.ads.googleads.v10.common.types.policy_summary import PolicySummary
from google.ads.googleads.v10.enums.types.asset_field_type import AssetFieldTypeEnum
from google.ads.googleads.v10.enums.types.asset_link_status import AssetLinkStatusEnum
from google.ads.googleads.v10.enums.types.asset_performance_label import (
    AssetPerformanceLabelEnum,
)

class AssetGroupAsset(proto.Message):
    resource_name: str
    asset_group: str
    asset: str
    field_type: AssetFieldTypeEnum.AssetFieldType
    status: AssetLinkStatusEnum.AssetLinkStatus
    performance_label: AssetPerformanceLabelEnum.AssetPerformanceLabel
    policy_summary: PolicySummary
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        asset_group: str = ...,
        asset: str = ...,
        field_type: AssetFieldTypeEnum.AssetFieldType = ...,
        status: AssetLinkStatusEnum.AssetLinkStatus = ...,
        performance_label: AssetPerformanceLabelEnum.AssetPerformanceLabel = ...,
        policy_summary: PolicySummary = ...
    ) -> None: ...
