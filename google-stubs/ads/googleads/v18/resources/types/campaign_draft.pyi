import proto
from _typeshed import Incomplete
from google.ads.googleads.v18.enums.types import campaign_draft_status

__protobuf__: Incomplete

class CampaignDraft(proto.Message):
    resource_name: str
    draft_id: int
    base_campaign: str
    name: str
    draft_campaign: str
    status: campaign_draft_status.CampaignDraftStatusEnum.CampaignDraftStatus
    has_experiment_running: bool
    long_running_operation: str
