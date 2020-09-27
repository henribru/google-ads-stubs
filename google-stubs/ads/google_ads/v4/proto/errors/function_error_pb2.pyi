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

class FunctionErrorEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    FunctionErrorValue = typing___NewType("FunctionErrorValue", builtin___int)
    type___FunctionErrorValue = FunctionErrorValue
    FunctionError: _FunctionError
    class _FunctionError(
        google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[
            FunctionErrorEnum.FunctionErrorValue
        ]
    ):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        UNSPECIFIED = typing___cast(FunctionErrorEnum.FunctionErrorValue, 0)
        UNKNOWN = typing___cast(FunctionErrorEnum.FunctionErrorValue, 1)
        INVALID_FUNCTION_FORMAT = typing___cast(FunctionErrorEnum.FunctionErrorValue, 2)
        DATA_TYPE_MISMATCH = typing___cast(FunctionErrorEnum.FunctionErrorValue, 3)
        INVALID_CONJUNCTION_OPERANDS = typing___cast(
            FunctionErrorEnum.FunctionErrorValue, 4
        )
        INVALID_NUMBER_OF_OPERANDS = typing___cast(
            FunctionErrorEnum.FunctionErrorValue, 5
        )
        INVALID_OPERAND_TYPE = typing___cast(FunctionErrorEnum.FunctionErrorValue, 6)
        INVALID_OPERATOR = typing___cast(FunctionErrorEnum.FunctionErrorValue, 7)
        INVALID_REQUEST_CONTEXT_TYPE = typing___cast(
            FunctionErrorEnum.FunctionErrorValue, 8
        )
        INVALID_FUNCTION_FOR_CALL_PLACEHOLDER = typing___cast(
            FunctionErrorEnum.FunctionErrorValue, 9
        )
        INVALID_FUNCTION_FOR_PLACEHOLDER = typing___cast(
            FunctionErrorEnum.FunctionErrorValue, 10
        )
        INVALID_OPERAND = typing___cast(FunctionErrorEnum.FunctionErrorValue, 11)
        MISSING_CONSTANT_OPERAND_VALUE = typing___cast(
            FunctionErrorEnum.FunctionErrorValue, 12
        )
        INVALID_CONSTANT_OPERAND_VALUE = typing___cast(
            FunctionErrorEnum.FunctionErrorValue, 13
        )
        INVALID_NESTING = typing___cast(FunctionErrorEnum.FunctionErrorValue, 14)
        MULTIPLE_FEED_IDS_NOT_SUPPORTED = typing___cast(
            FunctionErrorEnum.FunctionErrorValue, 15
        )
        INVALID_FUNCTION_FOR_FEED_WITH_FIXED_SCHEMA = typing___cast(
            FunctionErrorEnum.FunctionErrorValue, 16
        )
        INVALID_ATTRIBUTE_NAME = typing___cast(FunctionErrorEnum.FunctionErrorValue, 17)
    UNSPECIFIED = typing___cast(FunctionErrorEnum.FunctionErrorValue, 0)
    UNKNOWN = typing___cast(FunctionErrorEnum.FunctionErrorValue, 1)
    INVALID_FUNCTION_FORMAT = typing___cast(FunctionErrorEnum.FunctionErrorValue, 2)
    DATA_TYPE_MISMATCH = typing___cast(FunctionErrorEnum.FunctionErrorValue, 3)
    INVALID_CONJUNCTION_OPERANDS = typing___cast(
        FunctionErrorEnum.FunctionErrorValue, 4
    )
    INVALID_NUMBER_OF_OPERANDS = typing___cast(FunctionErrorEnum.FunctionErrorValue, 5)
    INVALID_OPERAND_TYPE = typing___cast(FunctionErrorEnum.FunctionErrorValue, 6)
    INVALID_OPERATOR = typing___cast(FunctionErrorEnum.FunctionErrorValue, 7)
    INVALID_REQUEST_CONTEXT_TYPE = typing___cast(
        FunctionErrorEnum.FunctionErrorValue, 8
    )
    INVALID_FUNCTION_FOR_CALL_PLACEHOLDER = typing___cast(
        FunctionErrorEnum.FunctionErrorValue, 9
    )
    INVALID_FUNCTION_FOR_PLACEHOLDER = typing___cast(
        FunctionErrorEnum.FunctionErrorValue, 10
    )
    INVALID_OPERAND = typing___cast(FunctionErrorEnum.FunctionErrorValue, 11)
    MISSING_CONSTANT_OPERAND_VALUE = typing___cast(
        FunctionErrorEnum.FunctionErrorValue, 12
    )
    INVALID_CONSTANT_OPERAND_VALUE = typing___cast(
        FunctionErrorEnum.FunctionErrorValue, 13
    )
    INVALID_NESTING = typing___cast(FunctionErrorEnum.FunctionErrorValue, 14)
    MULTIPLE_FEED_IDS_NOT_SUPPORTED = typing___cast(
        FunctionErrorEnum.FunctionErrorValue, 15
    )
    INVALID_FUNCTION_FOR_FEED_WITH_FIXED_SCHEMA = typing___cast(
        FunctionErrorEnum.FunctionErrorValue, 16
    )
    INVALID_ATTRIBUTE_NAME = typing___cast(FunctionErrorEnum.FunctionErrorValue, 17)
    type___FunctionError = FunctionError
    def __init__(self,) -> None: ...

type___FunctionErrorEnum = FunctionErrorEnum
