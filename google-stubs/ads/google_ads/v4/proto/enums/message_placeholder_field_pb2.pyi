# @generated by mypy-protobuf.  Do not edit manually!
import sys
from typing import NewType as typing___NewType, cast as typing___cast

from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    EnumDescriptor as google___protobuf___descriptor___EnumDescriptor,
    FileDescriptor as google___protobuf___descriptor___FileDescriptor,
)
from google.protobuf.internal.enum_type_wrapper import (
    _EnumTypeWrapper as google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper,
)
from google.protobuf.message import Message as google___protobuf___message___Message

builtin___int = int

DESCRIPTOR: google___protobuf___descriptor___FileDescriptor = ...

class MessagePlaceholderFieldEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    MessagePlaceholderFieldValue = typing___NewType(
        "MessagePlaceholderFieldValue", builtin___int
    )
    type___MessagePlaceholderFieldValue = MessagePlaceholderFieldValue
    MessagePlaceholderField: _MessagePlaceholderField
    class _MessagePlaceholderField(
        google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[
            MessagePlaceholderFieldEnum.MessagePlaceholderFieldValue
        ]
    ):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        UNSPECIFIED = typing___cast(
            MessagePlaceholderFieldEnum.MessagePlaceholderFieldValue, 0
        )
        UNKNOWN = typing___cast(
            MessagePlaceholderFieldEnum.MessagePlaceholderFieldValue, 1
        )
        BUSINESS_NAME = typing___cast(
            MessagePlaceholderFieldEnum.MessagePlaceholderFieldValue, 2
        )
        COUNTRY_CODE = typing___cast(
            MessagePlaceholderFieldEnum.MessagePlaceholderFieldValue, 3
        )
        PHONE_NUMBER = typing___cast(
            MessagePlaceholderFieldEnum.MessagePlaceholderFieldValue, 4
        )
        MESSAGE_EXTENSION_TEXT = typing___cast(
            MessagePlaceholderFieldEnum.MessagePlaceholderFieldValue, 5
        )
        MESSAGE_TEXT = typing___cast(
            MessagePlaceholderFieldEnum.MessagePlaceholderFieldValue, 6
        )
    UNSPECIFIED = typing___cast(
        MessagePlaceholderFieldEnum.MessagePlaceholderFieldValue, 0
    )
    UNKNOWN = typing___cast(MessagePlaceholderFieldEnum.MessagePlaceholderFieldValue, 1)
    BUSINESS_NAME = typing___cast(
        MessagePlaceholderFieldEnum.MessagePlaceholderFieldValue, 2
    )
    COUNTRY_CODE = typing___cast(
        MessagePlaceholderFieldEnum.MessagePlaceholderFieldValue, 3
    )
    PHONE_NUMBER = typing___cast(
        MessagePlaceholderFieldEnum.MessagePlaceholderFieldValue, 4
    )
    MESSAGE_EXTENSION_TEXT = typing___cast(
        MessagePlaceholderFieldEnum.MessagePlaceholderFieldValue, 5
    )
    MESSAGE_TEXT = typing___cast(
        MessagePlaceholderFieldEnum.MessagePlaceholderFieldValue, 6
    )
    type___MessagePlaceholderField = MessagePlaceholderField
    def __init__(self,) -> None: ...

type___MessagePlaceholderFieldEnum = MessagePlaceholderFieldEnum
