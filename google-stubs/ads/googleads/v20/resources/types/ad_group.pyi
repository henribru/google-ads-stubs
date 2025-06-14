import proto
from _typeshed import Incomplete
from google.ads.googleads.v20.common.types import custom_parameter, targeting_setting as gagc_targeting_setting
from google.ads.googleads.v20.enums.types import ad_group_ad_rotation_mode, ad_group_primary_status, ad_group_primary_status_reason, ad_group_status, ad_group_type, asset_field_type, asset_set_type, bidding_source, demand_gen_channel_config, demand_gen_channel_strategy, targeting_dimension
from typing import MutableSequence

__protobuf__: Incomplete

class AdGroup(proto.Message):
    class AudienceSetting(proto.Message):
        use_audience_grouped: bool
    class DemandGenAdGroupSettings(proto.Message):
        class DemandGenChannelControls(proto.Message):
            class DemandGenSelectedChannels(proto.Message):
                youtube_in_stream: bool
                youtube_in_feed: bool
                youtube_shorts: bool
                discover: bool
                gmail: bool
                display: bool
            channel_config: demand_gen_channel_config.DemandGenChannelConfigEnum.DemandGenChannelConfig
            channel_strategy: demand_gen_channel_strategy.DemandGenChannelStrategyEnum.DemandGenChannelStrategy
            selected_channels: AdGroup.DemandGenAdGroupSettings.DemandGenChannelControls.DemandGenSelectedChannels
        channel_controls: AdGroup.DemandGenAdGroupSettings.DemandGenChannelControls
    resource_name: str
    id: int
    name: str
    status: ad_group_status.AdGroupStatusEnum.AdGroupStatus
    type_: ad_group_type.AdGroupTypeEnum.AdGroupType
    ad_rotation_mode: ad_group_ad_rotation_mode.AdGroupAdRotationModeEnum.AdGroupAdRotationMode
    base_ad_group: str
    tracking_url_template: str
    url_custom_parameters: MutableSequence[custom_parameter.CustomParameter]
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
    display_custom_bid_dimension: targeting_dimension.TargetingDimensionEnum.TargetingDimension
    final_url_suffix: str
    targeting_setting: gagc_targeting_setting.TargetingSetting
    audience_setting: AudienceSetting
    effective_target_cpa_micros: int
    effective_target_cpa_source: bidding_source.BiddingSourceEnum.BiddingSource
    effective_target_roas: float
    effective_target_roas_source: bidding_source.BiddingSourceEnum.BiddingSource
    labels: MutableSequence[str]
    excluded_parent_asset_field_types: MutableSequence[asset_field_type.AssetFieldTypeEnum.AssetFieldType]
    excluded_parent_asset_set_types: MutableSequence[asset_set_type.AssetSetTypeEnum.AssetSetType]
    primary_status: ad_group_primary_status.AdGroupPrimaryStatusEnum.AdGroupPrimaryStatus
    primary_status_reasons: MutableSequence[ad_group_primary_status_reason.AdGroupPrimaryStatusReasonEnum.AdGroupPrimaryStatusReason]
    demand_gen_ad_group_settings: DemandGenAdGroupSettings
