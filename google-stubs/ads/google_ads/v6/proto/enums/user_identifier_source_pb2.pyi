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

class UserIdentifierSourceEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    UserIdentifierSourceValue = typing___NewType(
        "UserIdentifierSourceValue", builtin___int
    )
    type___UserIdentifierSourceValue = UserIdentifierSourceValue
    UserIdentifierSource: _UserIdentifierSource
    class _UserIdentifierSource(
        google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[
            UserIdentifierSourceEnum.UserIdentifierSourceValue
        ]
    ):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        UNSPECIFIED = typing___cast(
            UserIdentifierSourceEnum.UserIdentifierSourceValue, 0
        )
        UNKNOWN = typing___cast(UserIdentifierSourceEnum.UserIdentifierSourceValue, 1)
        FIRST_PARTY = typing___cast(
            UserIdentifierSourceEnum.UserIdentifierSourceValue, 2
        )
        THIRD_PARTY = typing___cast(
            UserIdentifierSourceEnum.UserIdentifierSourceValue, 3
        )
    UNSPECIFIED = typing___cast(UserIdentifierSourceEnum.UserIdentifierSourceValue, 0)
    UNKNOWN = typing___cast(UserIdentifierSourceEnum.UserIdentifierSourceValue, 1)
    FIRST_PARTY = typing___cast(UserIdentifierSourceEnum.UserIdentifierSourceValue, 2)
    THIRD_PARTY = typing___cast(UserIdentifierSourceEnum.UserIdentifierSourceValue, 3)
    type___UserIdentifierSource = UserIdentifierSource
    def __init__(self,) -> None: ...

type___UserIdentifierSourceEnum = UserIdentifierSourceEnum
