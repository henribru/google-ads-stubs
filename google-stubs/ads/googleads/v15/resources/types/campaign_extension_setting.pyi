from collections.abc import Mapping, MutableSequence
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v15.enums.types.extension_setting_device import (
    ExtensionSettingDeviceEnum,
)
from google.ads.googleads.v15.enums.types.extension_type import ExtensionTypeEnum

_M = TypeVar("_M")

class CampaignExtensionSetting(proto.Message):
    resource_name: str
    extension_type: ExtensionTypeEnum.ExtensionType
    campaign: str
    extension_feed_items: MutableSequence[str]
    device: ExtensionSettingDeviceEnum.ExtensionSettingDevice
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        extension_type: ExtensionTypeEnum.ExtensionType = ...,
        campaign: str = ...,
        extension_feed_items: MutableSequence[str] = ...,
        device: ExtensionSettingDeviceEnum.ExtensionSettingDevice = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "resource_name",
            "extension_type",
            "campaign",
            "extension_feed_items",
            "device",
        ],
    ) -> bool: ...
