from typing import Any

import proto

from google.ads.googleads.v8.enums.types import (
    campaign_draft_status as campaign_draft_status,
)

__protobuf__: Any

class CampaignDraft(proto.Message):
    resource_name: Any
    draft_id: Any
    base_campaign: Any
    name: Any
    draft_campaign: Any
    status: Any
    has_experiment_running: Any
    long_running_operation: Any
