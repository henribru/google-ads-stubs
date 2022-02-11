from typing import Any

import proto

from google.ads.googleads.v9.enums.types import (
    feed_item_set_string_filter_type as feed_item_set_string_filter_type,
)

__protobuf__: Any

class DynamicLocationSetFilter(proto.Message):
    labels: Any
    business_name_filter: Any

class BusinessNameFilter(proto.Message):
    business_name: Any
    filter_type: Any

class DynamicAffiliateLocationSetFilter(proto.Message):
    chain_ids: Any
