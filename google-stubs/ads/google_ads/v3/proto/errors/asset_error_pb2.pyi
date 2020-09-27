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

class AssetErrorEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    AssetErrorValue = typing___NewType("AssetErrorValue", builtin___int)
    type___AssetErrorValue = AssetErrorValue
    AssetError: _AssetError
    class _AssetError(
        google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[
            AssetErrorEnum.AssetErrorValue
        ]
    ):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        UNSPECIFIED = typing___cast(AssetErrorEnum.AssetErrorValue, 0)
        UNKNOWN = typing___cast(AssetErrorEnum.AssetErrorValue, 1)
        CUSTOMER_NOT_WHITELISTED_FOR_ASSET_TYPE = typing___cast(
            AssetErrorEnum.AssetErrorValue, 2
        )
        DUPLICATE_ASSET = typing___cast(AssetErrorEnum.AssetErrorValue, 3)
        DUPLICATE_ASSET_NAME = typing___cast(AssetErrorEnum.AssetErrorValue, 4)
        ASSET_DATA_IS_MISSING = typing___cast(AssetErrorEnum.AssetErrorValue, 5)
        CANNOT_MODIFY_ASSET_NAME = typing___cast(AssetErrorEnum.AssetErrorValue, 6)
    UNSPECIFIED = typing___cast(AssetErrorEnum.AssetErrorValue, 0)
    UNKNOWN = typing___cast(AssetErrorEnum.AssetErrorValue, 1)
    CUSTOMER_NOT_WHITELISTED_FOR_ASSET_TYPE = typing___cast(
        AssetErrorEnum.AssetErrorValue, 2
    )
    DUPLICATE_ASSET = typing___cast(AssetErrorEnum.AssetErrorValue, 3)
    DUPLICATE_ASSET_NAME = typing___cast(AssetErrorEnum.AssetErrorValue, 4)
    ASSET_DATA_IS_MISSING = typing___cast(AssetErrorEnum.AssetErrorValue, 5)
    CANNOT_MODIFY_ASSET_NAME = typing___cast(AssetErrorEnum.AssetErrorValue, 6)
    type___AssetError = AssetError
    def __init__(self,) -> None: ...

type___AssetErrorEnum = AssetErrorEnum
