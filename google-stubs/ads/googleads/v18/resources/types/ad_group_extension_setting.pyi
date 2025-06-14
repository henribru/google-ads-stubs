from google.ads.googleads.v18.enums.types.extension_setting_device import ExtensionSettingDeviceEnum
from collections.abc import MutableSequence
from google.ads.googleads.v18.enums.types.extension_type import ExtensionTypeEnum
import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class AdGroupExtensionSetting(proto.Message):
    resource_name: str
    extension_type: ExtensionTypeEnum.ExtensionType
    ad_group: str
    extension_feed_items: MutableSequence[str]
    device: ExtensionSettingDeviceEnum.ExtensionSettingDevice
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., resource_name: str = ..., extension_type: ExtensionTypeEnum.ExtensionType = ..., ad_group: str = ..., extension_feed_items: MutableSequence[str] = ..., device: ExtensionSettingDeviceEnum.ExtensionSettingDevice = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["resource_name", "extension_type", "ad_group", "extension_feed_items", "device"]) -> bool: ...
