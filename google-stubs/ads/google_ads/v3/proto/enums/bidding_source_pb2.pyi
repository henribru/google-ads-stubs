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

class BiddingSourceEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    BiddingSourceValue = typing___NewType("BiddingSourceValue", builtin___int)
    type___BiddingSourceValue = BiddingSourceValue
    BiddingSource: _BiddingSource
    class _BiddingSource(
        google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[
            BiddingSourceEnum.BiddingSourceValue
        ]
    ):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        UNSPECIFIED = typing___cast(BiddingSourceEnum.BiddingSourceValue, 0)
        UNKNOWN = typing___cast(BiddingSourceEnum.BiddingSourceValue, 1)
        CAMPAIGN_BIDDING_STRATEGY = typing___cast(
            BiddingSourceEnum.BiddingSourceValue, 5
        )
        AD_GROUP = typing___cast(BiddingSourceEnum.BiddingSourceValue, 6)
        AD_GROUP_CRITERION = typing___cast(BiddingSourceEnum.BiddingSourceValue, 7)
    UNSPECIFIED = typing___cast(BiddingSourceEnum.BiddingSourceValue, 0)
    UNKNOWN = typing___cast(BiddingSourceEnum.BiddingSourceValue, 1)
    CAMPAIGN_BIDDING_STRATEGY = typing___cast(BiddingSourceEnum.BiddingSourceValue, 5)
    AD_GROUP = typing___cast(BiddingSourceEnum.BiddingSourceValue, 6)
    AD_GROUP_CRITERION = typing___cast(BiddingSourceEnum.BiddingSourceValue, 7)
    type___BiddingSource = BiddingSource
    def __init__(self,) -> None: ...

type___BiddingSourceEnum = BiddingSourceEnum
