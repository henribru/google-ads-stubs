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


class NewResourceCreationErrorEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class NewResourceCreationError(int):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        @classmethod
        def Name(cls, number: int) -> str: ...
        @classmethod
        def Value(cls, name: str) -> NewResourceCreationErrorEnum.NewResourceCreationError: ...
        @classmethod
        def keys(cls) -> typing___List[str]: ...
        @classmethod
        def values(cls) -> typing___List[NewResourceCreationErrorEnum.NewResourceCreationError]: ...
        @classmethod
        def items(cls) -> typing___List[typing___Tuple[str, NewResourceCreationErrorEnum.NewResourceCreationError]]: ...
        UNSPECIFIED = typing___cast(NewResourceCreationErrorEnum.NewResourceCreationError, 0)
        UNKNOWN = typing___cast(NewResourceCreationErrorEnum.NewResourceCreationError, 1)
        CANNOT_SET_ID_FOR_CREATE = typing___cast(NewResourceCreationErrorEnum.NewResourceCreationError, 2)
        DUPLICATE_TEMP_IDS = typing___cast(NewResourceCreationErrorEnum.NewResourceCreationError, 3)
        TEMP_ID_RESOURCE_HAD_ERRORS = typing___cast(NewResourceCreationErrorEnum.NewResourceCreationError, 4)
    UNSPECIFIED = typing___cast(NewResourceCreationErrorEnum.NewResourceCreationError, 0)
    UNKNOWN = typing___cast(NewResourceCreationErrorEnum.NewResourceCreationError, 1)
    CANNOT_SET_ID_FOR_CREATE = typing___cast(NewResourceCreationErrorEnum.NewResourceCreationError, 2)
    DUPLICATE_TEMP_IDS = typing___cast(NewResourceCreationErrorEnum.NewResourceCreationError, 3)
    TEMP_ID_RESOURCE_HAD_ERRORS = typing___cast(NewResourceCreationErrorEnum.NewResourceCreationError, 4)


    def __init__(self,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> NewResourceCreationErrorEnum: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
