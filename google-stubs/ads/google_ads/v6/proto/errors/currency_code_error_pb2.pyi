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

class CurrencyCodeErrorEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    CurrencyCodeErrorValue = typing___NewType("CurrencyCodeErrorValue", builtin___int)
    type___CurrencyCodeErrorValue = CurrencyCodeErrorValue
    CurrencyCodeError: _CurrencyCodeError
    class _CurrencyCodeError(
        google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[
            CurrencyCodeErrorEnum.CurrencyCodeErrorValue
        ]
    ):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        UNSPECIFIED = typing___cast(CurrencyCodeErrorEnum.CurrencyCodeErrorValue, 0)
        UNKNOWN = typing___cast(CurrencyCodeErrorEnum.CurrencyCodeErrorValue, 1)
        UNSUPPORTED = typing___cast(CurrencyCodeErrorEnum.CurrencyCodeErrorValue, 2)
    UNSPECIFIED = typing___cast(CurrencyCodeErrorEnum.CurrencyCodeErrorValue, 0)
    UNKNOWN = typing___cast(CurrencyCodeErrorEnum.CurrencyCodeErrorValue, 1)
    UNSUPPORTED = typing___cast(CurrencyCodeErrorEnum.CurrencyCodeErrorValue, 2)
    type___CurrencyCodeError = CurrencyCodeError
    def __init__(self,) -> None: ...

type___CurrencyCodeErrorEnum = CurrencyCodeErrorEnum
