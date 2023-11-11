from collections.abc import Mapping, MutableSequence
from typing import Any, TypeVar

import google.protobuf.message
import proto

from google.ads.googleads.v14.enums.types.extension_setting_device import (
    ExtensionSettingDeviceEnum,
)
from google.ads.googleads.v14.enums.types.extension_type import ExtensionTypeEnum

_M = TypeVar("_M")

class CustomerExtensionSetting(proto.Message):
    resource_name: str
    extension_type: ExtensionTypeEnum.ExtensionType
    extension_feed_items: MutableSequence[str]
    device: ExtensionSettingDeviceEnum.ExtensionSettingDevice
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        extension_type: ExtensionTypeEnum.ExtensionType = ...,
        extension_feed_items: MutableSequence[str] = ...,
        device: ExtensionSettingDeviceEnum.ExtensionSettingDevice = ...
    ) -> None: ...
