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


class PolicyViolationErrorEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class PolicyViolationError(int):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        @classmethod
        def Name(cls, number: int) -> str: ...
        @classmethod
        def Value(cls, name: str) -> PolicyViolationErrorEnum.PolicyViolationError: ...
        @classmethod
        def keys(cls) -> typing___List[str]: ...
        @classmethod
        def values(cls) -> typing___List[PolicyViolationErrorEnum.PolicyViolationError]: ...
        @classmethod
        def items(cls) -> typing___List[typing___Tuple[str, PolicyViolationErrorEnum.PolicyViolationError]]: ...
        UNSPECIFIED = typing___cast(PolicyViolationErrorEnum.PolicyViolationError, 0)
        UNKNOWN = typing___cast(PolicyViolationErrorEnum.PolicyViolationError, 1)
        POLICY_ERROR = typing___cast(PolicyViolationErrorEnum.PolicyViolationError, 2)
    UNSPECIFIED = typing___cast(PolicyViolationErrorEnum.PolicyViolationError, 0)
    UNKNOWN = typing___cast(PolicyViolationErrorEnum.PolicyViolationError, 1)
    POLICY_ERROR = typing___cast(PolicyViolationErrorEnum.PolicyViolationError, 2)


    def __init__(self,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> PolicyViolationErrorEnum: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
