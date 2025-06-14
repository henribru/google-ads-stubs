import proto
from _typeshed import Incomplete
from google.ads.googleads.v18.common.types import criteria
from google.ads.googleads.v18.enums.types import criterion_type

__protobuf__: Incomplete

class SharedCriterion(proto.Message):
    resource_name: str
    shared_set: str
    criterion_id: int
    type_: criterion_type.CriterionTypeEnum.CriterionType
    keyword: criteria.KeywordInfo
    youtube_video: criteria.YouTubeVideoInfo
    youtube_channel: criteria.YouTubeChannelInfo
    placement: criteria.PlacementInfo
    mobile_app_category: criteria.MobileAppCategoryInfo
    mobile_application: criteria.MobileApplicationInfo
    brand: criteria.BrandInfo
