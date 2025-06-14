import proto
from _typeshed import Incomplete
from google.ads.googleads.v20.common.types import criteria
from google.ads.googleads.v20.enums.types import criterion_type

__protobuf__: Incomplete

class CustomerNegativeCriterion(proto.Message):
    resource_name: str
    id: int
    type_: criterion_type.CriterionTypeEnum.CriterionType
    content_label: criteria.ContentLabelInfo
    mobile_application: criteria.MobileApplicationInfo
    mobile_app_category: criteria.MobileAppCategoryInfo
    placement: criteria.PlacementInfo
    youtube_video: criteria.YouTubeVideoInfo
    youtube_channel: criteria.YouTubeChannelInfo
    negative_keyword_list: criteria.NegativeKeywordListInfo
    ip_block: criteria.IpBlockInfo
