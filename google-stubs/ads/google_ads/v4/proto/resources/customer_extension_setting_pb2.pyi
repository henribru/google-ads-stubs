# @generated by mypy-protobuf.  Do not edit manually!
import sys
from typing import (
    Iterable as typing___Iterable,
    Optional as typing___Optional,
    Text as typing___Text,
)

from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    FileDescriptor as google___protobuf___descriptor___FileDescriptor,
)
from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
)
from google.protobuf.message import Message as google___protobuf___message___Message
from google.protobuf.wrappers_pb2 import (
    StringValue as google___protobuf___wrappers_pb2___StringValue,
)
from typing_extensions import Literal as typing_extensions___Literal

from google.ads.google_ads.v4.proto.enums.extension_setting_device_pb2 import (
    ExtensionSettingDeviceEnum as google___ads___googleads___v4___enums___extension_setting_device_pb2___ExtensionSettingDeviceEnum,
)
from google.ads.google_ads.v4.proto.enums.extension_type_pb2 import (
    ExtensionTypeEnum as google___ads___googleads___v4___enums___extension_type_pb2___ExtensionTypeEnum,
)

builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int

DESCRIPTOR: google___protobuf___descriptor___FileDescriptor = ...

class CustomerExtensionSetting(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    resource_name: typing___Text = ...
    extension_type: google___ads___googleads___v4___enums___extension_type_pb2___ExtensionTypeEnum.ExtensionTypeValue = ...
    device: google___ads___googleads___v4___enums___extension_setting_device_pb2___ExtensionSettingDeviceEnum.ExtensionSettingDeviceValue = ...
    @property
    def extension_feed_items(
        self,
    ) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[
        google___protobuf___wrappers_pb2___StringValue
    ]: ...
    def __init__(
        self,
        *,
        resource_name: typing___Optional[typing___Text] = None,
        extension_type: typing___Optional[
            google___ads___googleads___v4___enums___extension_type_pb2___ExtensionTypeEnum.ExtensionTypeValue
        ] = None,
        extension_feed_items: typing___Optional[
            typing___Iterable[google___protobuf___wrappers_pb2___StringValue]
        ] = None,
        device: typing___Optional[
            google___ads___googleads___v4___enums___extension_setting_device_pb2___ExtensionSettingDeviceEnum.ExtensionSettingDeviceValue
        ] = None,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "device",
            b"device",
            "extension_feed_items",
            b"extension_feed_items",
            "extension_type",
            b"extension_type",
            "resource_name",
            b"resource_name",
        ],
    ) -> None: ...

type___CustomerExtensionSetting = CustomerExtensionSetting
