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

class KeywordPlanNetworkEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    KeywordPlanNetworkValue = typing___NewType("KeywordPlanNetworkValue", builtin___int)
    type___KeywordPlanNetworkValue = KeywordPlanNetworkValue
    KeywordPlanNetwork: _KeywordPlanNetwork
    class _KeywordPlanNetwork(
        google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[
            KeywordPlanNetworkEnum.KeywordPlanNetworkValue
        ]
    ):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        UNSPECIFIED = typing___cast(KeywordPlanNetworkEnum.KeywordPlanNetworkValue, 0)
        UNKNOWN = typing___cast(KeywordPlanNetworkEnum.KeywordPlanNetworkValue, 1)
        GOOGLE_SEARCH = typing___cast(KeywordPlanNetworkEnum.KeywordPlanNetworkValue, 2)
        GOOGLE_SEARCH_AND_PARTNERS = typing___cast(
            KeywordPlanNetworkEnum.KeywordPlanNetworkValue, 3
        )
    UNSPECIFIED = typing___cast(KeywordPlanNetworkEnum.KeywordPlanNetworkValue, 0)
    UNKNOWN = typing___cast(KeywordPlanNetworkEnum.KeywordPlanNetworkValue, 1)
    GOOGLE_SEARCH = typing___cast(KeywordPlanNetworkEnum.KeywordPlanNetworkValue, 2)
    GOOGLE_SEARCH_AND_PARTNERS = typing___cast(
        KeywordPlanNetworkEnum.KeywordPlanNetworkValue, 3
    )
    type___KeywordPlanNetwork = KeywordPlanNetwork
    def __init__(self,) -> None: ...

type___KeywordPlanNetworkEnum = KeywordPlanNetworkEnum
