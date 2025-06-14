import proto
from _typeshed import Incomplete
from google.ads.googleads.v19.enums.types import campaign_group_status

__protobuf__: Incomplete

class CampaignGroup(proto.Message):
    resource_name: str
    id: int
    name: str
    status: campaign_group_status.CampaignGroupStatusEnum.CampaignGroupStatus
