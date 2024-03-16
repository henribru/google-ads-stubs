from collections.abc import Mapping, MutableSequence
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v16.common.types.asset_policy import (
    AssetLinkPrimaryStatusDetails,
)
from google.ads.googleads.v16.common.types.policy_summary import PolicySummary
from google.ads.googleads.v16.enums.types.asset_field_type import AssetFieldTypeEnum
from google.ads.googleads.v16.enums.types.asset_link_primary_status import (
    AssetLinkPrimaryStatusEnum,
)
from google.ads.googleads.v16.enums.types.asset_link_primary_status_reason import (
    AssetLinkPrimaryStatusReasonEnum,
)
from google.ads.googleads.v16.enums.types.asset_link_status import AssetLinkStatusEnum
from google.ads.googleads.v16.enums.types.asset_performance_label import (
    AssetPerformanceLabelEnum,
)
from google.ads.googleads.v16.enums.types.asset_source import AssetSourceEnum

_M = TypeVar("_M")

class AssetGroupAsset(proto.Message):
    resource_name: str
    asset_group: str
    asset: str
    field_type: AssetFieldTypeEnum.AssetFieldType
    status: AssetLinkStatusEnum.AssetLinkStatus
    primary_status: AssetLinkPrimaryStatusEnum.AssetLinkPrimaryStatus
    primary_status_reasons: MutableSequence[
        AssetLinkPrimaryStatusReasonEnum.AssetLinkPrimaryStatusReason
    ]
    primary_status_details: MutableSequence[AssetLinkPrimaryStatusDetails]
    performance_label: AssetPerformanceLabelEnum.AssetPerformanceLabel
    policy_summary: PolicySummary
    source: AssetSourceEnum.AssetSource
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
        primary_status: AssetLinkPrimaryStatusEnum.AssetLinkPrimaryStatus = ...,
        primary_status_reasons: MutableSequence[
            AssetLinkPrimaryStatusReasonEnum.AssetLinkPrimaryStatusReason
        ] = ...,
        primary_status_details: MutableSequence[AssetLinkPrimaryStatusDetails] = ...,
        performance_label: AssetPerformanceLabelEnum.AssetPerformanceLabel = ...,
        policy_summary: PolicySummary = ...,
        source: AssetSourceEnum.AssetSource = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "resource_name",
            "asset_group",
            "asset",
            "field_type",
            "status",
            "primary_status",
            "primary_status_reasons",
            "primary_status_details",
            "performance_label",
            "policy_summary",
            "source",
        ],
    ) -> bool: ...
