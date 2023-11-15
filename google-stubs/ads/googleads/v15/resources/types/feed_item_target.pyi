from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

from google.ads.googleads.v15.common.types.criteria import AdScheduleInfo, KeywordInfo
from google.ads.googleads.v15.enums.types.feed_item_target_device import (
    FeedItemTargetDeviceEnum,
)
from google.ads.googleads.v15.enums.types.feed_item_target_status import (
    FeedItemTargetStatusEnum,
)
from google.ads.googleads.v15.enums.types.feed_item_target_type import (
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
        ad_schedule: AdScheduleInfo = ...
    ) -> None: ...
