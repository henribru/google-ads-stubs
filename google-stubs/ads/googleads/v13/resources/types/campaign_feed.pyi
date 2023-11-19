from collections.abc import Mapping, MutableSequence
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v13.common.types.matching_function import MatchingFunction
from google.ads.googleads.v13.enums.types.feed_link_status import FeedLinkStatusEnum
from google.ads.googleads.v13.enums.types.placeholder_type import PlaceholderTypeEnum

_M = TypeVar("_M")

class CampaignFeed(proto.Message):
    resource_name: str
    feed: str
    campaign: str
    placeholder_types: MutableSequence[PlaceholderTypeEnum.PlaceholderType]
    matching_function: MatchingFunction
    status: FeedLinkStatusEnum.FeedLinkStatus
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        feed: str = ...,
        campaign: str = ...,
        placeholder_types: MutableSequence[PlaceholderTypeEnum.PlaceholderType] = ...,
        matching_function: MatchingFunction = ...,
        status: FeedLinkStatusEnum.FeedLinkStatus = ...
    ) -> None: ...
    def __contains__(self, key: Literal["resource_name", "feed", "campaign", "placeholder_types", "matching_function", "status"]) -> bool: ...  # type: ignore[override]
