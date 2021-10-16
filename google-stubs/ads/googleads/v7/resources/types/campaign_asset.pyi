from typing import Any

import proto

from google.ads.googleads.v7.enums.types import (
    asset_field_type as asset_field_type,
    asset_link_status as asset_link_status,
)

__protobuf__: Any

class CampaignAsset(proto.Message):
    resource_name: Any
    campaign: Any
    asset: Any
    field_type: Any
    status: Any
