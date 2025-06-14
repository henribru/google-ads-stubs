import proto
from _typeshed import Incomplete
from google.ads.googleads.v20.enums.types import combined_audience_status

__protobuf__: Incomplete

class CombinedAudience(proto.Message):
    resource_name: str
    id: int
    status: combined_audience_status.CombinedAudienceStatusEnum.CombinedAudienceStatus
    name: str
    description: str
