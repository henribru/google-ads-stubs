from typing import Any

import proto

from google.ads.googleads.v9.common.types import bidding as bidding
from google.ads.googleads.v9.enums.types import (
    bidding_strategy_status as bidding_strategy_status,
    bidding_strategy_type as bidding_strategy_type,
)

__protobuf__: Any

class BiddingStrategy(proto.Message):
    resource_name: Any
    id: Any
    name: Any
    status: Any
    type_: Any
    currency_code: Any
    effective_currency_code: Any
    campaign_count: Any
    non_removed_campaign_count: Any
    enhanced_cpc: Any
    maximize_conversion_value: Any
    maximize_conversions: Any
    target_cpa: Any
    target_impression_share: Any
    target_roas: Any
    target_spend: Any
