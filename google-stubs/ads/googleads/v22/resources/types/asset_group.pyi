from collections.abc import Mapping, MutableSequence
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v22.enums.types.ad_strength import AdStrengthEnum
from google.ads.googleads.v22.enums.types.ad_strength_action_item_type import (
    AdStrengthActionItemTypeEnum,
)
from google.ads.googleads.v22.enums.types.asset_coverage_video_aspect_ratio_requirement import (
    AssetCoverageVideoAspectRatioRequirementEnum,
)
from google.ads.googleads.v22.enums.types.asset_field_type import AssetFieldTypeEnum
from google.ads.googleads.v22.enums.types.asset_group_primary_status import (
    AssetGroupPrimaryStatusEnum,
)
from google.ads.googleads.v22.enums.types.asset_group_primary_status_reason import (
    AssetGroupPrimaryStatusReasonEnum,
)
from google.ads.googleads.v22.enums.types.asset_group_status import AssetGroupStatusEnum

_M = TypeVar("_M")

class AdStrengthActionItem(proto.Message):
    class AddAssetDetails(proto.Message):
        asset_field_type: AssetFieldTypeEnum.AssetFieldType
        asset_count: int
        video_aspect_ratio_requirement: AssetCoverageVideoAspectRatioRequirementEnum.AssetCoverageVideoAspectRatioRequirement
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
            asset_field_type: AssetFieldTypeEnum.AssetFieldType = ...,
            asset_count: int = ...,
            video_aspect_ratio_requirement: AssetCoverageVideoAspectRatioRequirementEnum.AssetCoverageVideoAspectRatioRequirement = ...,
        ) -> None: ...
        def __contains__(  # type: ignore[override]
            self,
            key: Literal[
                "asset_field_type", "asset_count", "video_aspect_ratio_requirement"
            ],
        ) -> bool: ...

    action_item_type: AdStrengthActionItemTypeEnum.AdStrengthActionItemType
    add_asset_details: AdStrengthActionItem.AddAssetDetails
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        action_item_type: AdStrengthActionItemTypeEnum.AdStrengthActionItemType = ...,
        add_asset_details: AdStrengthActionItem.AddAssetDetails = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["action_item_type", "add_asset_details"]
    ) -> bool: ...

class AssetCoverage(proto.Message):
    ad_strength_action_items: MutableSequence[AdStrengthActionItem]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        ad_strength_action_items: MutableSequence[AdStrengthActionItem] = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["ad_strength_action_items"]
    ) -> bool: ...

class AssetGroup(proto.Message):
    resource_name: str
    id: int
    campaign: str
    name: str
    final_urls: MutableSequence[str]
    final_mobile_urls: MutableSequence[str]
    status: AssetGroupStatusEnum.AssetGroupStatus
    primary_status: AssetGroupPrimaryStatusEnum.AssetGroupPrimaryStatus
    primary_status_reasons: MutableSequence[
        AssetGroupPrimaryStatusReasonEnum.AssetGroupPrimaryStatusReason
    ]
    path1: str
    path2: str
    ad_strength: AdStrengthEnum.AdStrength
    asset_coverage: AssetCoverage
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        id: int = ...,
        campaign: str = ...,
        name: str = ...,
        final_urls: MutableSequence[str] = ...,
        final_mobile_urls: MutableSequence[str] = ...,
        status: AssetGroupStatusEnum.AssetGroupStatus = ...,
        primary_status: AssetGroupPrimaryStatusEnum.AssetGroupPrimaryStatus = ...,
        primary_status_reasons: MutableSequence[
            AssetGroupPrimaryStatusReasonEnum.AssetGroupPrimaryStatusReason
        ] = ...,
        path1: str = ...,
        path2: str = ...,
        ad_strength: AdStrengthEnum.AdStrength = ...,
        asset_coverage: AssetCoverage = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "resource_name",
            "id",
            "campaign",
            "name",
            "final_urls",
            "final_mobile_urls",
            "status",
            "primary_status",
            "primary_status_reasons",
            "path1",
            "path2",
            "ad_strength",
            "asset_coverage",
        ],
    ) -> bool: ...
