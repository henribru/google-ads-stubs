from typing import Any

import proto

from google.ads.googleads.v7.enums.types import (
    extension_setting_device as extension_setting_device,
)

__protobuf__: Any

class CampaignExtensionSetting(proto.Message):
    resource_name: Any
    extension_type: Any
    campaign: Any
    extension_feed_items: Any
    device: Any
