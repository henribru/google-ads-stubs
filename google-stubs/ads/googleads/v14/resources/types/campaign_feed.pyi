from collections.abc import MutableSequence
from typing import Any

import proto

from google.ads.googleads.v14.common.types.matching_function import MatchingFunction
from google.ads.googleads.v14.enums.types.feed_link_status import FeedLinkStatusEnum
from google.ads.googleads.v14.enums.types.placeholder_type import PlaceholderTypeEnum

class CampaignFeed(proto.Message):
    resource_name: str
    feed: str
    campaign: str
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
        campaign: str = ...,
        placeholder_types: MutableSequence[PlaceholderTypeEnum.PlaceholderType] = ...,
        matching_function: MatchingFunction = ...,
        status: FeedLinkStatusEnum.FeedLinkStatus = ...
    ) -> None: ...
