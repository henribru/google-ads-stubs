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

class UserListNumberRuleItemOperatorEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    UserListNumberRuleItemOperatorValue = typing___NewType(
        "UserListNumberRuleItemOperatorValue", builtin___int
    )
    type___UserListNumberRuleItemOperatorValue = UserListNumberRuleItemOperatorValue
    UserListNumberRuleItemOperator: _UserListNumberRuleItemOperator
    class _UserListNumberRuleItemOperator(
        google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[
            UserListNumberRuleItemOperatorEnum.UserListNumberRuleItemOperatorValue
        ]
    ):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        UNSPECIFIED = typing___cast(
            UserListNumberRuleItemOperatorEnum.UserListNumberRuleItemOperatorValue, 0
        )
        UNKNOWN = typing___cast(
            UserListNumberRuleItemOperatorEnum.UserListNumberRuleItemOperatorValue, 1
        )
        GREATER_THAN = typing___cast(
            UserListNumberRuleItemOperatorEnum.UserListNumberRuleItemOperatorValue, 2
        )
        GREATER_THAN_OR_EQUAL = typing___cast(
            UserListNumberRuleItemOperatorEnum.UserListNumberRuleItemOperatorValue, 3
        )
        EQUALS = typing___cast(
            UserListNumberRuleItemOperatorEnum.UserListNumberRuleItemOperatorValue, 4
        )
        NOT_EQUALS = typing___cast(
            UserListNumberRuleItemOperatorEnum.UserListNumberRuleItemOperatorValue, 5
        )
        LESS_THAN = typing___cast(
            UserListNumberRuleItemOperatorEnum.UserListNumberRuleItemOperatorValue, 6
        )
        LESS_THAN_OR_EQUAL = typing___cast(
            UserListNumberRuleItemOperatorEnum.UserListNumberRuleItemOperatorValue, 7
        )
    UNSPECIFIED = typing___cast(
        UserListNumberRuleItemOperatorEnum.UserListNumberRuleItemOperatorValue, 0
    )
    UNKNOWN = typing___cast(
        UserListNumberRuleItemOperatorEnum.UserListNumberRuleItemOperatorValue, 1
    )
    GREATER_THAN = typing___cast(
        UserListNumberRuleItemOperatorEnum.UserListNumberRuleItemOperatorValue, 2
    )
    GREATER_THAN_OR_EQUAL = typing___cast(
        UserListNumberRuleItemOperatorEnum.UserListNumberRuleItemOperatorValue, 3
    )
    EQUALS = typing___cast(
        UserListNumberRuleItemOperatorEnum.UserListNumberRuleItemOperatorValue, 4
    )
    NOT_EQUALS = typing___cast(
        UserListNumberRuleItemOperatorEnum.UserListNumberRuleItemOperatorValue, 5
    )
    LESS_THAN = typing___cast(
        UserListNumberRuleItemOperatorEnum.UserListNumberRuleItemOperatorValue, 6
    )
    LESS_THAN_OR_EQUAL = typing___cast(
        UserListNumberRuleItemOperatorEnum.UserListNumberRuleItemOperatorValue, 7
    )
    type___UserListNumberRuleItemOperator = UserListNumberRuleItemOperator
    def __init__(self,) -> None: ...

type___UserListNumberRuleItemOperatorEnum = UserListNumberRuleItemOperatorEnum
