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


class BudgetPeriodEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class BudgetPeriod(int):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        @classmethod
        def Name(cls, number: int) -> str: ...
        @classmethod
        def Value(cls, name: str) -> BudgetPeriodEnum.BudgetPeriod: ...
        @classmethod
        def keys(cls) -> typing___List[str]: ...
        @classmethod
        def values(cls) -> typing___List[BudgetPeriodEnum.BudgetPeriod]: ...
        @classmethod
        def items(cls) -> typing___List[typing___Tuple[str, BudgetPeriodEnum.BudgetPeriod]]: ...
        UNSPECIFIED = typing___cast(BudgetPeriodEnum.BudgetPeriod, 0)
        UNKNOWN = typing___cast(BudgetPeriodEnum.BudgetPeriod, 1)
        DAILY = typing___cast(BudgetPeriodEnum.BudgetPeriod, 2)
        CUSTOM = typing___cast(BudgetPeriodEnum.BudgetPeriod, 3)
        FIXED_DAILY = typing___cast(BudgetPeriodEnum.BudgetPeriod, 4)
    UNSPECIFIED = typing___cast(BudgetPeriodEnum.BudgetPeriod, 0)
    UNKNOWN = typing___cast(BudgetPeriodEnum.BudgetPeriod, 1)
    DAILY = typing___cast(BudgetPeriodEnum.BudgetPeriod, 2)
    CUSTOM = typing___cast(BudgetPeriodEnum.BudgetPeriod, 3)
    FIXED_DAILY = typing___cast(BudgetPeriodEnum.BudgetPeriod, 4)


    def __init__(self,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> BudgetPeriodEnum: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
