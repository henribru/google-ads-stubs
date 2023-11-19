from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v13.common.types.policy_summary import PolicySummary
from google.ads.googleads.v13.enums.types.asset_field_type import AssetFieldTypeEnum
from google.ads.googleads.v13.enums.types.asset_link_status import AssetLinkStatusEnum
from google.ads.googleads.v13.enums.types.asset_performance_label import (
    AssetPerformanceLabelEnum,
)

_M = TypeVar("_M")

class AssetGroupAsset(proto.Message):
    resource_name: str
    asset_group: str
    asset: str
    field_type: AssetFieldTypeEnum.AssetFieldType
    status: AssetLinkStatusEnum.AssetLinkStatus
    performance_label: AssetPerformanceLabelEnum.AssetPerformanceLabel
    policy_summary: PolicySummary
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        asset_group: str = ...,
        asset: str = ...,
        field_type: AssetFieldTypeEnum.AssetFieldType = ...,
        status: AssetLinkStatusEnum.AssetLinkStatus = ...,
        performance_label: AssetPerformanceLabelEnum.AssetPerformanceLabel = ...,
        policy_summary: PolicySummary = ...
    ) -> None: ...
    def __contains__(self, key: Literal["resource_name", "asset_group", "asset", "field_type", "status", "performance_label", "policy_summary"]) -> bool: ...  # type: ignore[override]
