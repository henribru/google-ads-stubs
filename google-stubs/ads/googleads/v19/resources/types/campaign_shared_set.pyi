import proto
from _typeshed import Incomplete
from google.ads.googleads.v19.enums.types import campaign_shared_set_status

__protobuf__: Incomplete

class CampaignSharedSet(proto.Message):
    resource_name: str
    campaign: str
    shared_set: str
    status: campaign_shared_set_status.CampaignSharedSetStatusEnum.CampaignSharedSetStatus
