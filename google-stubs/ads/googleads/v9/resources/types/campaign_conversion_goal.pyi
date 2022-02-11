from typing import Any

import proto

from google.ads.googleads.v9.enums.types import (
    conversion_action_category as conversion_action_category,
    conversion_origin as conversion_origin,
)

__protobuf__: Any

class CampaignConversionGoal(proto.Message):
    resource_name: Any
    campaign: Any
    category: Any
    origin: Any
    biddable: Any
