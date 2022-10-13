from typing import Any

import proto

from google.ads.googleads.v10.common.types.criteria import AdScheduleInfo, KeywordInfo
from google.ads.googleads.v10.enums.types.feed_item_target_device import (
    FeedItemTargetDeviceEnum,
)
from google.ads.googleads.v10.enums.types.feed_item_target_status import (
    FeedItemTargetStatusEnum,
)
from google.ads.googleads.v10.enums.types.feed_item_target_type import (
    FeedItemTargetTypeEnum,
)

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
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
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
