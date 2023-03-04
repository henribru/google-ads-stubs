from collections.abc import MutableSequence
from typing import Any

import proto

from google.ads.googleads.v13.enums.types.extension_setting_device import (
    ExtensionSettingDeviceEnum,
)
from google.ads.googleads.v13.enums.types.extension_type import ExtensionTypeEnum

class CustomerExtensionSetting(proto.Message):
    resource_name: str
    extension_type: ExtensionTypeEnum.ExtensionType
    extension_feed_items: MutableSequence[str]
    device: ExtensionSettingDeviceEnum.ExtensionSettingDevice
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        extension_type: ExtensionTypeEnum.ExtensionType = ...,
        extension_feed_items: MutableSequence[str] = ...,
        device: ExtensionSettingDeviceEnum.ExtensionSettingDevice = ...
    ) -> None: ...
