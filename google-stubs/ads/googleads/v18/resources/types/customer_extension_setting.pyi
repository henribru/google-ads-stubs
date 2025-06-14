import proto
from _typeshed import Incomplete
from google.ads.googleads.v18.enums.types import extension_setting_device, extension_type as gage_extension_type
from typing import MutableSequence

__protobuf__: Incomplete

class CustomerExtensionSetting(proto.Message):
    resource_name: str
    extension_type: gage_extension_type.ExtensionTypeEnum.ExtensionType
    extension_feed_items: MutableSequence[str]
    device: extension_setting_device.ExtensionSettingDeviceEnum.ExtensionSettingDevice
