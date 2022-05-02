import proto
from _typeshed import Incomplete

from google.ads.googleads.v10.enums.types import (
    feed_item_set_string_filter_type as feed_item_set_string_filter_type,
)

__protobuf__: Incomplete

class DynamicLocationSetFilter(proto.Message):
    labels: Incomplete
    business_name_filter: Incomplete

class BusinessNameFilter(proto.Message):
    business_name: Incomplete
    filter_type: Incomplete

class DynamicAffiliateLocationSetFilter(proto.Message):
    chain_ids: Incomplete
