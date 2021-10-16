from typing import Any

import proto

from google.ads.googleads.v7.enums.types import (
    extension_setting_device as extension_setting_device,
)

__protobuf__: Any

class CustomerExtensionSetting(proto.Message):
    resource_name: Any
    extension_type: Any
    extension_feed_items: Any
    device: Any
