from google.ads.googleads.v18.enums.types.feed_link_status import FeedLinkStatusEnum
from google.ads.googleads.v18.common.types.matching_function import MatchingFunction
from collections.abc import MutableSequence
from google.ads.googleads.v18.enums.types.placeholder_type import PlaceholderTypeEnum
import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class CustomerFeed(proto.Message):
    resource_name: str
    feed: str
    placeholder_types: MutableSequence[PlaceholderTypeEnum.PlaceholderType]
    matching_function: MatchingFunction
    status: FeedLinkStatusEnum.FeedLinkStatus
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, resource_name: str = ..., feed: str = ..., placeholder_types: MutableSequence[PlaceholderTypeEnum.PlaceholderType] = ..., matching_function: MatchingFunction = ..., status: FeedLinkStatusEnum.FeedLinkStatus = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["resource_name", "feed", "placeholder_types", "matching_function", "status"]) -> bool: ...
