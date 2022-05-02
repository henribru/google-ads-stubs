import proto
from _typeshed import Incomplete

from google.ads.googleads.v10.common.types import custom_parameter as custom_parameter
from google.ads.googleads.v10.enums.types import (
    ad_group_ad_rotation_mode as ad_group_ad_rotation_mode,
    ad_group_status as ad_group_status,
    ad_group_type as ad_group_type,
    asset_field_type as asset_field_type,
    bidding_source as bidding_source,
    targeting_dimension as targeting_dimension,
)

__protobuf__: Incomplete

class AdGroup(proto.Message):
    class AudienceSetting(proto.Message):
        use_audience_grouped: Incomplete
    resource_name: Incomplete
    id: Incomplete
    name: Incomplete
    status: Incomplete
    type_: Incomplete
    ad_rotation_mode: Incomplete
    base_ad_group: Incomplete
    tracking_url_template: Incomplete
    url_custom_parameters: Incomplete
    campaign: Incomplete
    cpc_bid_micros: Incomplete
    effective_cpc_bid_micros: Incomplete
    cpm_bid_micros: Incomplete
    target_cpa_micros: Incomplete
    cpv_bid_micros: Incomplete
    target_cpm_micros: Incomplete
    target_roas: Incomplete
    percent_cpc_bid_micros: Incomplete
    explorer_auto_optimizer_setting: Incomplete
    display_custom_bid_dimension: Incomplete
    final_url_suffix: Incomplete
    targeting_setting: Incomplete
    audience_setting: Incomplete
    effective_target_cpa_micros: Incomplete
    effective_target_cpa_source: Incomplete
    effective_target_roas: Incomplete
    effective_target_roas_source: Incomplete
    labels: Incomplete
    excluded_parent_asset_field_types: Incomplete
