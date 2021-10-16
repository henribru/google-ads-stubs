from typing import Any

import proto

from google.ads.googleads.v8.common.types import custom_parameter as custom_parameter
from google.ads.googleads.v8.enums.types import (
    ad_group_ad_rotation_mode as ad_group_ad_rotation_mode,
    ad_group_status as ad_group_status,
    ad_group_type as ad_group_type,
    asset_field_type as asset_field_type,
    bidding_source as bidding_source,
    targeting_dimension as targeting_dimension,
)

__protobuf__: Any

class AdGroup(proto.Message):
    resource_name: Any
    id: Any
    name: Any
    status: Any
    type_: Any
    ad_rotation_mode: Any
    base_ad_group: Any
    tracking_url_template: Any
    url_custom_parameters: Any
    campaign: Any
    cpc_bid_micros: Any
    cpm_bid_micros: Any
    target_cpa_micros: Any
    cpv_bid_micros: Any
    target_cpm_micros: Any
    target_roas: Any
    percent_cpc_bid_micros: Any
    explorer_auto_optimizer_setting: Any
    display_custom_bid_dimension: Any
    final_url_suffix: Any
    targeting_setting: Any
    effective_target_cpa_micros: Any
    effective_target_cpa_source: Any
    effective_target_roas: Any
    effective_target_roas_source: Any
    labels: Any
    excluded_parent_asset_field_types: Any
