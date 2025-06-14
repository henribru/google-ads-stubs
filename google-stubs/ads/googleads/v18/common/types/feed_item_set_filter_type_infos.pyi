import proto
from _typeshed import Incomplete
from google.ads.googleads.v18.enums.types import feed_item_set_string_filter_type
from typing import MutableSequence

__protobuf__: Incomplete

class DynamicLocationSetFilter(proto.Message):
    labels: MutableSequence[str]
    business_name_filter: BusinessNameFilter

class BusinessNameFilter(proto.Message):
    business_name: str
    filter_type: feed_item_set_string_filter_type.FeedItemSetStringFilterTypeEnum.FeedItemSetStringFilterType

class DynamicAffiliateLocationSetFilter(proto.Message):
    chain_ids: MutableSequence[int]
