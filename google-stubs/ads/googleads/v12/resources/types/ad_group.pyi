from collections.abc import MutableSequence
from typing import Any

import proto

from google.ads.googleads.v12.common.types.custom_parameter import CustomParameter
from google.ads.googleads.v12.common.types.explorer_auto_optimizer_setting import (
    ExplorerAutoOptimizerSetting,
)
from google.ads.googleads.v12.common.types.targeting_setting import TargetingSetting
from google.ads.googleads.v12.enums.types.ad_group_ad_rotation_mode import (
    AdGroupAdRotationModeEnum,
)
from google.ads.googleads.v12.enums.types.ad_group_status import AdGroupStatusEnum
from google.ads.googleads.v12.enums.types.ad_group_type import AdGroupTypeEnum
from google.ads.googleads.v12.enums.types.asset_field_type import AssetFieldTypeEnum
from google.ads.googleads.v12.enums.types.asset_set_type import AssetSetTypeEnum
from google.ads.googleads.v12.enums.types.bidding_source import BiddingSourceEnum
from google.ads.googleads.v12.enums.types.targeting_dimension import (
    TargetingDimensionEnum,
)

class AdGroup(proto.Message):
    class AudienceSetting(proto.Message):
        use_audience_grouped: bool
        def __init__(
            self,
            mapping: Any | None = ...,
            *,
            ignore_unknown_fields: bool = ...,
            use_audience_grouped: bool = ...
        ) -> None: ...
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
    explorer_auto_optimizer_setting: ExplorerAutoOptimizerSetting
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
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
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
        explorer_auto_optimizer_setting: ExplorerAutoOptimizerSetting = ...,
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
        ] = ...
    ) -> None: ...
