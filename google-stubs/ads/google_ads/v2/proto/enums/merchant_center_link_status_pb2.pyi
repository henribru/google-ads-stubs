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

class MerchantCenterLinkStatusEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    MerchantCenterLinkStatusValue = typing___NewType(
        "MerchantCenterLinkStatusValue", builtin___int
    )
    type___MerchantCenterLinkStatusValue = MerchantCenterLinkStatusValue
    MerchantCenterLinkStatus: _MerchantCenterLinkStatus
    class _MerchantCenterLinkStatus(
        google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[
            MerchantCenterLinkStatusEnum.MerchantCenterLinkStatusValue
        ]
    ):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        UNSPECIFIED = typing___cast(
            MerchantCenterLinkStatusEnum.MerchantCenterLinkStatusValue, 0
        )
        UNKNOWN = typing___cast(
            MerchantCenterLinkStatusEnum.MerchantCenterLinkStatusValue, 1
        )
        ENABLED = typing___cast(
            MerchantCenterLinkStatusEnum.MerchantCenterLinkStatusValue, 2
        )
        PENDING = typing___cast(
            MerchantCenterLinkStatusEnum.MerchantCenterLinkStatusValue, 3
        )
    UNSPECIFIED = typing___cast(
        MerchantCenterLinkStatusEnum.MerchantCenterLinkStatusValue, 0
    )
    UNKNOWN = typing___cast(
        MerchantCenterLinkStatusEnum.MerchantCenterLinkStatusValue, 1
    )
    ENABLED = typing___cast(
        MerchantCenterLinkStatusEnum.MerchantCenterLinkStatusValue, 2
    )
    PENDING = typing___cast(
        MerchantCenterLinkStatusEnum.MerchantCenterLinkStatusValue, 3
    )
    type___MerchantCenterLinkStatus = MerchantCenterLinkStatus
    def __init__(self,) -> None: ...

type___MerchantCenterLinkStatusEnum = MerchantCenterLinkStatusEnum
