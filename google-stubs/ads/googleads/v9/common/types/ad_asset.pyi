from typing import Any

import proto

from google.ads.googleads.v9.common.types import asset_policy as asset_policy
from google.ads.googleads.v9.enums.types import (
    served_asset_field_type as served_asset_field_type,
)

__protobuf__: Any

class AdTextAsset(proto.Message):
    text: Any
    pinned_field: Any
    asset_performance_label: Any
    policy_summary_info: Any

class AdImageAsset(proto.Message):
    asset: Any

class AdVideoAsset(proto.Message):
    asset: Any

class AdMediaBundleAsset(proto.Message):
    asset: Any
