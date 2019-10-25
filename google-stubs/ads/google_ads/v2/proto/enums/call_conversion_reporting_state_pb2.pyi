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


class CallConversionReportingStateEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class CallConversionReportingState(int):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        @classmethod
        def Name(cls, number: int) -> str: ...
        @classmethod
        def Value(cls, name: str) -> CallConversionReportingStateEnum.CallConversionReportingState: ...
        @classmethod
        def keys(cls) -> typing___List[str]: ...
        @classmethod
        def values(cls) -> typing___List[CallConversionReportingStateEnum.CallConversionReportingState]: ...
        @classmethod
        def items(cls) -> typing___List[typing___Tuple[str, CallConversionReportingStateEnum.CallConversionReportingState]]: ...
        UNSPECIFIED = typing___cast(CallConversionReportingStateEnum.CallConversionReportingState, 0)
        UNKNOWN = typing___cast(CallConversionReportingStateEnum.CallConversionReportingState, 1)
        DISABLED = typing___cast(CallConversionReportingStateEnum.CallConversionReportingState, 2)
        USE_ACCOUNT_LEVEL_CALL_CONVERSION_ACTION = typing___cast(CallConversionReportingStateEnum.CallConversionReportingState, 3)
        USE_RESOURCE_LEVEL_CALL_CONVERSION_ACTION = typing___cast(CallConversionReportingStateEnum.CallConversionReportingState, 4)
    UNSPECIFIED = typing___cast(CallConversionReportingStateEnum.CallConversionReportingState, 0)
    UNKNOWN = typing___cast(CallConversionReportingStateEnum.CallConversionReportingState, 1)
    DISABLED = typing___cast(CallConversionReportingStateEnum.CallConversionReportingState, 2)
    USE_ACCOUNT_LEVEL_CALL_CONVERSION_ACTION = typing___cast(CallConversionReportingStateEnum.CallConversionReportingState, 3)
    USE_RESOURCE_LEVEL_CALL_CONVERSION_ACTION = typing___cast(CallConversionReportingStateEnum.CallConversionReportingState, 4)


    def __init__(self,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> CallConversionReportingStateEnum: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
