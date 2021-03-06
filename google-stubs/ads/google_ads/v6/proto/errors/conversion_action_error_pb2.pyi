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

class ConversionActionErrorEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    ConversionActionErrorValue = typing___NewType(
        "ConversionActionErrorValue", builtin___int
    )
    type___ConversionActionErrorValue = ConversionActionErrorValue
    ConversionActionError: _ConversionActionError
    class _ConversionActionError(
        google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[
            ConversionActionErrorEnum.ConversionActionErrorValue
        ]
    ):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        UNSPECIFIED = typing___cast(
            ConversionActionErrorEnum.ConversionActionErrorValue, 0
        )
        UNKNOWN = typing___cast(ConversionActionErrorEnum.ConversionActionErrorValue, 1)
        DUPLICATE_NAME = typing___cast(
            ConversionActionErrorEnum.ConversionActionErrorValue, 2
        )
        DUPLICATE_APP_ID = typing___cast(
            ConversionActionErrorEnum.ConversionActionErrorValue, 3
        )
        TWO_CONVERSION_ACTIONS_BIDDING_ON_SAME_APP_DOWNLOAD = typing___cast(
            ConversionActionErrorEnum.ConversionActionErrorValue, 4
        )
        BIDDING_ON_SAME_APP_DOWNLOAD_AS_GLOBAL_ACTION = typing___cast(
            ConversionActionErrorEnum.ConversionActionErrorValue, 5
        )
        DATA_DRIVEN_MODEL_WAS_NEVER_GENERATED = typing___cast(
            ConversionActionErrorEnum.ConversionActionErrorValue, 6
        )
        DATA_DRIVEN_MODEL_EXPIRED = typing___cast(
            ConversionActionErrorEnum.ConversionActionErrorValue, 7
        )
        DATA_DRIVEN_MODEL_STALE = typing___cast(
            ConversionActionErrorEnum.ConversionActionErrorValue, 8
        )
        DATA_DRIVEN_MODEL_UNKNOWN = typing___cast(
            ConversionActionErrorEnum.ConversionActionErrorValue, 9
        )
        CREATION_NOT_SUPPORTED = typing___cast(
            ConversionActionErrorEnum.ConversionActionErrorValue, 10
        )
        UPDATE_NOT_SUPPORTED = typing___cast(
            ConversionActionErrorEnum.ConversionActionErrorValue, 11
        )
    UNSPECIFIED = typing___cast(ConversionActionErrorEnum.ConversionActionErrorValue, 0)
    UNKNOWN = typing___cast(ConversionActionErrorEnum.ConversionActionErrorValue, 1)
    DUPLICATE_NAME = typing___cast(
        ConversionActionErrorEnum.ConversionActionErrorValue, 2
    )
    DUPLICATE_APP_ID = typing___cast(
        ConversionActionErrorEnum.ConversionActionErrorValue, 3
    )
    TWO_CONVERSION_ACTIONS_BIDDING_ON_SAME_APP_DOWNLOAD = typing___cast(
        ConversionActionErrorEnum.ConversionActionErrorValue, 4
    )
    BIDDING_ON_SAME_APP_DOWNLOAD_AS_GLOBAL_ACTION = typing___cast(
        ConversionActionErrorEnum.ConversionActionErrorValue, 5
    )
    DATA_DRIVEN_MODEL_WAS_NEVER_GENERATED = typing___cast(
        ConversionActionErrorEnum.ConversionActionErrorValue, 6
    )
    DATA_DRIVEN_MODEL_EXPIRED = typing___cast(
        ConversionActionErrorEnum.ConversionActionErrorValue, 7
    )
    DATA_DRIVEN_MODEL_STALE = typing___cast(
        ConversionActionErrorEnum.ConversionActionErrorValue, 8
    )
    DATA_DRIVEN_MODEL_UNKNOWN = typing___cast(
        ConversionActionErrorEnum.ConversionActionErrorValue, 9
    )
    CREATION_NOT_SUPPORTED = typing___cast(
        ConversionActionErrorEnum.ConversionActionErrorValue, 10
    )
    UPDATE_NOT_SUPPORTED = typing___cast(
        ConversionActionErrorEnum.ConversionActionErrorValue, 11
    )
    type___ConversionActionError = ConversionActionError
    def __init__(self,) -> None: ...

type___ConversionActionErrorEnum = ConversionActionErrorEnum
