import proto
from _typeshed import Incomplete
from google.ads.googleads.v18.common.types import criteria
from google.ads.googleads.v18.enums.types import feed_item_target_device, feed_item_target_status, feed_item_target_type as gage_feed_item_target_type

__protobuf__: Incomplete

class FeedItemTarget(proto.Message):
    resource_name: str
    feed_item: str
    feed_item_target_type: gage_feed_item_target_type.FeedItemTargetTypeEnum.FeedItemTargetType
    feed_item_target_id: int
    status: feed_item_target_status.FeedItemTargetStatusEnum.FeedItemTargetStatus
    campaign: str
    ad_group: str
    keyword: criteria.KeywordInfo
    geo_target_constant: str
    device: feed_item_target_device.FeedItemTargetDeviceEnum.FeedItemTargetDevice
    ad_schedule: criteria.AdScheduleInfo
