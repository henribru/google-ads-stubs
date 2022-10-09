import proto
from _typeshed import Incomplete

from google.ads.googleads.v11.common.types import bidding as bidding
from google.ads.googleads.v11.enums.types import (
    bidding_strategy_status as bidding_strategy_status,
    bidding_strategy_type as bidding_strategy_type,
)

__protobuf__: Incomplete

class BiddingStrategy(proto.Message):
    resource_name: Incomplete
    id: Incomplete
    name: Incomplete
    status: Incomplete
    type_: Incomplete
    currency_code: Incomplete
    effective_currency_code: Incomplete
    campaign_count: Incomplete
    non_removed_campaign_count: Incomplete
    enhanced_cpc: Incomplete
    maximize_conversion_value: Incomplete
    maximize_conversions: Incomplete
    target_cpa: Incomplete
    target_impression_share: Incomplete
    target_roas: Incomplete
    target_spend: Incomplete
