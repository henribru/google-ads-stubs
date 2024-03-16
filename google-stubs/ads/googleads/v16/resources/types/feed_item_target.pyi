from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v16.common.types.criteria import AdScheduleInfo, KeywordInfo
from google.ads.googleads.v16.enums.types.feed_item_target_device import (
    FeedItemTargetDeviceEnum,
)
from google.ads.googleads.v16.enums.types.feed_item_target_status import (
    FeedItemTargetStatusEnum,
)
from google.ads.googleads.v16.enums.types.feed_item_target_type import (
    FeedItemTargetTypeEnum,
)

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
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        feed_item: str = ...,
        feed_item_target_type: FeedItemTargetTypeEnum.FeedItemTargetType = ...,
        feed_item_target_id: int = ...,
        status: FeedItemTargetStatusEnum.FeedItemTargetStatus = ...,
        campaign: str = ...,
        ad_group: str = ...,
        keyword: KeywordInfo = ...,
        geo_target_constant: str = ...,
        device: FeedItemTargetDeviceEnum.FeedItemTargetDevice = ...,
        ad_schedule: AdScheduleInfo = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "resource_name",
            "feed_item",
            "feed_item_target_type",
            "feed_item_target_id",
            "status",
            "campaign",
            "ad_group",
            "keyword",
            "geo_target_constant",
            "device",
            "ad_schedule",
        ],
    ) -> bool: ...
