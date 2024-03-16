from collections.abc import Mapping, MutableSequence
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v16.common.types.custom_parameter import CustomParameter
from google.ads.googleads.v16.common.types.targeting_setting import TargetingSetting
from google.ads.googleads.v16.enums.types.ad_group_ad_rotation_mode import (
    AdGroupAdRotationModeEnum,
)
from google.ads.googleads.v16.enums.types.ad_group_primary_status import (
    AdGroupPrimaryStatusEnum,
)
from google.ads.googleads.v16.enums.types.ad_group_primary_status_reason import (
    AdGroupPrimaryStatusReasonEnum,
)
from google.ads.googleads.v16.enums.types.ad_group_status import AdGroupStatusEnum
from google.ads.googleads.v16.enums.types.ad_group_type import AdGroupTypeEnum
from google.ads.googleads.v16.enums.types.asset_field_type import AssetFieldTypeEnum
from google.ads.googleads.v16.enums.types.asset_set_type import AssetSetTypeEnum
from google.ads.googleads.v16.enums.types.bidding_source import BiddingSourceEnum
from google.ads.googleads.v16.enums.types.targeting_dimension import (
    TargetingDimensionEnum,
)

_M = TypeVar("_M")

class AdGroup(proto.Message):
    class AudienceSetting(proto.Message):
        use_audience_grouped: bool
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
            use_audience_grouped: bool = ...,
        ) -> None: ...
        def __contains__(  # type: ignore[override]
            self, key: Literal["use_audience_grouped"]
        ) -> bool: ...

    resource_name: str
    id: int
    name: str
    status: AdGroupStatusEnum.AdGroupStatus
    type_: AdGroupTypeEnum.AdGroupType
    ad_rotation_mode: AdGroupAdRotationModeEnum.AdGroupAdRotationMode
    base_ad_group: str
    tracking_url_template: str
    url_custom_parameters: MutableSequence[CustomParameter]
    campaign: str
    cpc_bid_micros: int
    effective_cpc_bid_micros: int
    cpm_bid_micros: int
    target_cpa_micros: int
    cpv_bid_micros: int
    target_cpm_micros: int
    target_roas: float
    percent_cpc_bid_micros: int
    optimized_targeting_enabled: bool
    display_custom_bid_dimension: TargetingDimensionEnum.TargetingDimension
    final_url_suffix: str
    targeting_setting: TargetingSetting
    audience_setting: AdGroup.AudienceSetting
    effective_target_cpa_micros: int
    effective_target_cpa_source: BiddingSourceEnum.BiddingSource
    effective_target_roas: float
    effective_target_roas_source: BiddingSourceEnum.BiddingSource
    labels: MutableSequence[str]
    excluded_parent_asset_field_types: MutableSequence[
        AssetFieldTypeEnum.AssetFieldType
    ]
    excluded_parent_asset_set_types: MutableSequence[AssetSetTypeEnum.AssetSetType]
    primary_status: AdGroupPrimaryStatusEnum.AdGroupPrimaryStatus
    primary_status_reasons: MutableSequence[
        AdGroupPrimaryStatusReasonEnum.AdGroupPrimaryStatusReason
    ]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        id: int = ...,
        name: str = ...,
        status: AdGroupStatusEnum.AdGroupStatus = ...,
        type_: AdGroupTypeEnum.AdGroupType = ...,
        ad_rotation_mode: AdGroupAdRotationModeEnum.AdGroupAdRotationMode = ...,
        base_ad_group: str = ...,
        tracking_url_template: str = ...,
        url_custom_parameters: MutableSequence[CustomParameter] = ...,
        campaign: str = ...,
        cpc_bid_micros: int = ...,
        effective_cpc_bid_micros: int = ...,
        cpm_bid_micros: int = ...,
        target_cpa_micros: int = ...,
        cpv_bid_micros: int = ...,
        target_cpm_micros: int = ...,
        target_roas: float = ...,
        percent_cpc_bid_micros: int = ...,
        optimized_targeting_enabled: bool = ...,
        display_custom_bid_dimension: TargetingDimensionEnum.TargetingDimension = ...,
        final_url_suffix: str = ...,
        targeting_setting: TargetingSetting = ...,
        audience_setting: AdGroup.AudienceSetting = ...,
        effective_target_cpa_micros: int = ...,
        effective_target_cpa_source: BiddingSourceEnum.BiddingSource = ...,
        effective_target_roas: float = ...,
        effective_target_roas_source: BiddingSourceEnum.BiddingSource = ...,
        labels: MutableSequence[str] = ...,
        excluded_parent_asset_field_types: MutableSequence[
            AssetFieldTypeEnum.AssetFieldType
        ] = ...,
        excluded_parent_asset_set_types: MutableSequence[
            AssetSetTypeEnum.AssetSetType
        ] = ...,
        primary_status: AdGroupPrimaryStatusEnum.AdGroupPrimaryStatus = ...,
        primary_status_reasons: MutableSequence[
            AdGroupPrimaryStatusReasonEnum.AdGroupPrimaryStatusReason
        ] = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "resource_name",
            "id",
            "name",
            "status",
            "type_",
            "ad_rotation_mode",
            "base_ad_group",
            "tracking_url_template",
            "url_custom_parameters",
            "campaign",
            "cpc_bid_micros",
            "effective_cpc_bid_micros",
            "cpm_bid_micros",
            "target_cpa_micros",
            "cpv_bid_micros",
            "target_cpm_micros",
            "target_roas",
            "percent_cpc_bid_micros",
            "optimized_targeting_enabled",
            "display_custom_bid_dimension",
            "final_url_suffix",
            "targeting_setting",
            "audience_setting",
            "effective_target_cpa_micros",
            "effective_target_cpa_source",
            "effective_target_roas",
            "effective_target_roas_source",
            "labels",
            "excluded_parent_asset_field_types",
            "excluded_parent_asset_set_types",
            "primary_status",
            "primary_status_reasons",
        ],
    ) -> bool: ...
