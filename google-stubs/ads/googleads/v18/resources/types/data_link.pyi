import proto
from _typeshed import Incomplete
from google.ads.googleads.v18.enums.types import data_link_status, data_link_type

__protobuf__: Incomplete

class DataLink(proto.Message):
    resource_name: str
    product_link_id: int
    data_link_id: int
    type_: data_link_type.DataLinkTypeEnum.DataLinkType
    status: data_link_status.DataLinkStatusEnum.DataLinkStatus
    youtube_video: YoutubeVideoIdentifier

class YoutubeVideoIdentifier(proto.Message):
    channel_id: str
    video_id: str
