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

class PaymentModeEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    PaymentModeValue = typing___NewType("PaymentModeValue", builtin___int)
    type___PaymentModeValue = PaymentModeValue
    PaymentMode: _PaymentMode
    class _PaymentMode(
        google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[
            PaymentModeEnum.PaymentModeValue
        ]
    ):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        UNSPECIFIED = typing___cast(PaymentModeEnum.PaymentModeValue, 0)
        UNKNOWN = typing___cast(PaymentModeEnum.PaymentModeValue, 1)
        CLICKS = typing___cast(PaymentModeEnum.PaymentModeValue, 4)
        CONVERSION_VALUE = typing___cast(PaymentModeEnum.PaymentModeValue, 5)
        CONVERSIONS = typing___cast(PaymentModeEnum.PaymentModeValue, 6)
    UNSPECIFIED = typing___cast(PaymentModeEnum.PaymentModeValue, 0)
    UNKNOWN = typing___cast(PaymentModeEnum.PaymentModeValue, 1)
    CLICKS = typing___cast(PaymentModeEnum.PaymentModeValue, 4)
    CONVERSION_VALUE = typing___cast(PaymentModeEnum.PaymentModeValue, 5)
    CONVERSIONS = typing___cast(PaymentModeEnum.PaymentModeValue, 6)
    type___PaymentMode = PaymentMode
    def __init__(self,) -> None: ...

type___PaymentModeEnum = PaymentModeEnum
