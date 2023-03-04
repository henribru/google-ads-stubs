from collections.abc import MutableSequence
from typing import Any

import proto

from google.ads.googleads.v12.common.types.matching_function import MatchingFunction
from google.ads.googleads.v12.enums.types.feed_link_status import FeedLinkStatusEnum
from google.ads.googleads.v12.enums.types.placeholder_type import PlaceholderTypeEnum

class AdGroupFeed(proto.Message):
    resource_name: str
    feed: str
    ad_group: str
    placeholder_types: MutableSequence[PlaceholderTypeEnum.PlaceholderType]
    matching_function: MatchingFunction
    status: FeedLinkStatusEnum.FeedLinkStatus
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        feed: str = ...,
        ad_group: str = ...,
        placeholder_types: MutableSequence[PlaceholderTypeEnum.PlaceholderType] = ...,
        matching_function: MatchingFunction = ...,
        status: FeedLinkStatusEnum.FeedLinkStatus = ...
    ) -> None: ...
