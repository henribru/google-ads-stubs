import proto
from _typeshed import Incomplete
from google.ads.googleads.v18.common.types import matching_function as gagc_matching_function
from google.ads.googleads.v18.enums.types import feed_link_status, placeholder_type
from typing import MutableSequence

__protobuf__: Incomplete

class AdGroupFeed(proto.Message):
    resource_name: str
    feed: str
    ad_group: str
    placeholder_types: MutableSequence[placeholder_type.PlaceholderTypeEnum.PlaceholderType]
    matching_function: gagc_matching_function.MatchingFunction
    status: feed_link_status.FeedLinkStatusEnum.FeedLinkStatus
