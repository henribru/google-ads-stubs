from google.ads.googleads.v18.common.types.criteria import AdScheduleInfo
from google.ads.googleads.v18.enums.types.feed_item_target_device import FeedItemTargetDeviceEnum
from google.ads.googleads.v18.common.types.criteria import KeywordInfo
from google.ads.googleads.v18.enums.types.feed_item_target_status import FeedItemTargetStatusEnum
from google.ads.googleads.v18.enums.types.feed_item_target_type import FeedItemTargetTypeEnum
import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class FeedItemTarget(proto.Message):
    resource_name: str
    feed_item: str
    feed_item_target_type: FeedItemTargetTypeEnum.FeedItemTargetType
    feed_item_target_id: int
    status: FeedItemTargetStatusEnum.FeedItemTargetStatus
    campaign: str
    ad_group: str
    keyword: KeywordInfo
    geo_target_constant: str
    device: FeedItemTargetDeviceEnum.FeedItemTargetDevice
    ad_schedule: AdScheduleInfo
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, resource_name: str = ..., feed_item: str = ..., feed_item_target_type: FeedItemTargetTypeEnum.FeedItemTargetType = ..., feed_item_target_id: int = ..., status: FeedItemTargetStatusEnum.FeedItemTargetStatus = ..., campaign: str = ..., ad_group: str = ..., keyword: KeywordInfo = ..., geo_target_constant: str = ..., device: FeedItemTargetDeviceEnum.FeedItemTargetDevice = ..., ad_schedule: AdScheduleInfo = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["resource_name", "feed_item", "feed_item_target_type", "feed_item_target_id", "status", "campaign", "ad_group", "keyword", "geo_target_constant", "device", "ad_schedule"]) -> bool: ...
