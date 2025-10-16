from collections.abc import Mapping, MutableSequence
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v19.common.types.custom_parameter import CustomParameter
from google.ads.googleads.v19.common.types.targeting_setting import TargetingSetting
from google.ads.googleads.v19.enums.types.ad_group_ad_rotation_mode import (
    AdGroupAdRotationModeEnum,
)
from google.ads.googleads.v19.enums.types.ad_group_primary_status import (
    AdGroupPrimaryStatusEnum,
)
from google.ads.googleads.v19.enums.types.ad_group_primary_status_reason import (
    AdGroupPrimaryStatusReasonEnum,
)
from google.ads.googleads.v19.enums.types.ad_group_status import AdGroupStatusEnum
from google.ads.googleads.v19.enums.types.ad_group_type import AdGroupTypeEnum
from google.ads.googleads.v19.enums.types.asset_field_type import AssetFieldTypeEnum
from google.ads.googleads.v19.enums.types.asset_set_type import AssetSetTypeEnum
from google.ads.googleads.v19.enums.types.bidding_source import BiddingSourceEnum
from google.ads.googleads.v19.enums.types.demand_gen_channel_config import (
    DemandGenChannelConfigEnum,
)
from google.ads.googleads.v19.enums.types.demand_gen_channel_strategy import (
    DemandGenChannelStrategyEnum,
)
from google.ads.googleads.v19.enums.types.targeting_dimension import (
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

    class DemandGenAdGroupSettings(proto.Message):
        class DemandGenChannelControls(proto.Message):
            class DemandGenSelectedChannels(proto.Message):
                youtube_in_stream: bool
                youtube_in_feed: bool
                youtube_shorts: bool
                discover: bool
                gmail: bool
                display: bool
                def __init__(
                    self: _M,
                    mapping: _M
                    | Mapping
                    | google.protobuf.message.Message
                    | None = None,
                    *,
                    ignore_unknown_fields: bool = False,
                    youtube_in_stream: bool = ...,
                    youtube_in_feed: bool = ...,
                    youtube_shorts: bool = ...,
                    discover: bool = ...,
                    gmail: bool = ...,
                    display: bool = ...,
                ) -> None: ...
                def __contains__(  # type: ignore[override]
                    self,
                    key: Literal[
                        "youtube_in_stream",
                        "youtube_in_feed",
                        "youtube_shorts",
                        "discover",
                        "gmail",
                        "display",
                    ],
                ) -> bool: ...

            channel_config: DemandGenChannelConfigEnum.DemandGenChannelConfig
            channel_strategy: DemandGenChannelStrategyEnum.DemandGenChannelStrategy
            selected_channels: AdGroup.DemandGenAdGroupSettings.DemandGenChannelControls.DemandGenSelectedChannels
            def __init__(
                self: _M,
                mapping: _M | Mapping | google.protobuf.message.Message | None = None,
                *,
                ignore_unknown_fields: bool = False,
                channel_config: DemandGenChannelConfigEnum.DemandGenChannelConfig = ...,
                channel_strategy: DemandGenChannelStrategyEnum.DemandGenChannelStrategy = ...,
                selected_channels: AdGroup.DemandGenAdGroupSettings.DemandGenChannelControls.DemandGenSelectedChannels = ...,
            ) -> None: ...
            def __contains__(  # type: ignore[override]
                self,
                key: Literal["channel_config", "channel_strategy", "selected_channels"],
            ) -> bool: ...

        channel_controls: AdGroup.DemandGenAdGroupSettings.DemandGenChannelControls
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
            channel_controls: AdGroup.DemandGenAdGroupSettings.DemandGenChannelControls = ...,
        ) -> None: ...
        def __contains__(  # type: ignore[override]
            self, key: Literal["channel_controls"]
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
    fixed_cpm_micros: int
    target_cpv_micros: int
    optimized_targeting_enabled: bool
    exclude_demographic_expansion: bool
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
    demand_gen_ad_group_settings: AdGroup.DemandGenAdGroupSettings
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
        fixed_cpm_micros: int = ...,
        target_cpv_micros: int = ...,
        optimized_targeting_enabled: bool = ...,
        exclude_demographic_expansion: bool = ...,
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
        demand_gen_ad_group_settings: AdGroup.DemandGenAdGroupSettings = ...,
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
            "fixed_cpm_micros",
            "target_cpv_micros",
            "optimized_targeting_enabled",
            "exclude_demographic_expansion",
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
            "demand_gen_ad_group_settings",
        ],
    ) -> bool: ...
