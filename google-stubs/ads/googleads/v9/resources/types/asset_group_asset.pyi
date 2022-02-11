from typing import Any

import proto

from google.ads.googleads.v9.enums.types import (
    asset_field_type as asset_field_type,
    asset_link_status as asset_link_status,
    asset_performance_label as asset_performance_label,
)

__protobuf__: Any

class AssetGroupAsset(proto.Message):
    resource_name: Any
    asset_group: Any
    asset: Any
    field_type: Any
    status: Any
    performance_label: Any
    policy_summary: Any
