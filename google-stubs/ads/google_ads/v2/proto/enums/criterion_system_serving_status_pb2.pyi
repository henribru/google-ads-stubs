# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    EnumDescriptor as google___protobuf___descriptor___EnumDescriptor,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from typing import (
    List as typing___List,
    Tuple as typing___Tuple,
    cast as typing___cast,
)


class CriterionSystemServingStatusEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class CriterionSystemServingStatus(int):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        @classmethod
        def Name(cls, number: int) -> str: ...
        @classmethod
        def Value(cls, name: str) -> CriterionSystemServingStatusEnum.CriterionSystemServingStatus: ...
        @classmethod
        def keys(cls) -> typing___List[str]: ...
        @classmethod
        def values(cls) -> typing___List[CriterionSystemServingStatusEnum.CriterionSystemServingStatus]: ...
        @classmethod
        def items(cls) -> typing___List[typing___Tuple[str, CriterionSystemServingStatusEnum.CriterionSystemServingStatus]]: ...
        UNSPECIFIED = typing___cast(CriterionSystemServingStatusEnum.CriterionSystemServingStatus, 0)
        UNKNOWN = typing___cast(CriterionSystemServingStatusEnum.CriterionSystemServingStatus, 1)
        ELIGIBLE = typing___cast(CriterionSystemServingStatusEnum.CriterionSystemServingStatus, 2)
        RARELY_SERVED = typing___cast(CriterionSystemServingStatusEnum.CriterionSystemServingStatus, 3)
    UNSPECIFIED = typing___cast(CriterionSystemServingStatusEnum.CriterionSystemServingStatus, 0)
    UNKNOWN = typing___cast(CriterionSystemServingStatusEnum.CriterionSystemServingStatus, 1)
    ELIGIBLE = typing___cast(CriterionSystemServingStatusEnum.CriterionSystemServingStatus, 2)
    RARELY_SERVED = typing___cast(CriterionSystemServingStatusEnum.CriterionSystemServingStatus, 3)


    def __init__(self,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> CriterionSystemServingStatusEnum: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
