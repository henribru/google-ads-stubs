from typing import Any

import proto

from google.ads.googleads.v9.enums.types import (
    campaign_shared_set_status as campaign_shared_set_status,
)

__protobuf__: Any

class CampaignSharedSet(proto.Message):
    resource_name: Any
    campaign: Any
    shared_set: Any
    status: Any
