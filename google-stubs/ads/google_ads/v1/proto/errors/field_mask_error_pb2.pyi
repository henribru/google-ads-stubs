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


class FieldMaskErrorEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class FieldMaskError(int):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        @classmethod
        def Name(cls, number: int) -> str: ...
        @classmethod
        def Value(cls, name: str) -> FieldMaskErrorEnum.FieldMaskError: ...
        @classmethod
        def keys(cls) -> typing___List[str]: ...
        @classmethod
        def values(cls) -> typing___List[FieldMaskErrorEnum.FieldMaskError]: ...
        @classmethod
        def items(cls) -> typing___List[typing___Tuple[str, FieldMaskErrorEnum.FieldMaskError]]: ...
        UNSPECIFIED = typing___cast(FieldMaskErrorEnum.FieldMaskError, 0)
        UNKNOWN = typing___cast(FieldMaskErrorEnum.FieldMaskError, 1)
        FIELD_MASK_MISSING = typing___cast(FieldMaskErrorEnum.FieldMaskError, 5)
        FIELD_MASK_NOT_ALLOWED = typing___cast(FieldMaskErrorEnum.FieldMaskError, 4)
        FIELD_NOT_FOUND = typing___cast(FieldMaskErrorEnum.FieldMaskError, 2)
        FIELD_HAS_SUBFIELDS = typing___cast(FieldMaskErrorEnum.FieldMaskError, 3)
    UNSPECIFIED = typing___cast(FieldMaskErrorEnum.FieldMaskError, 0)
    UNKNOWN = typing___cast(FieldMaskErrorEnum.FieldMaskError, 1)
    FIELD_MASK_MISSING = typing___cast(FieldMaskErrorEnum.FieldMaskError, 5)
    FIELD_MASK_NOT_ALLOWED = typing___cast(FieldMaskErrorEnum.FieldMaskError, 4)
    FIELD_NOT_FOUND = typing___cast(FieldMaskErrorEnum.FieldMaskError, 2)
    FIELD_HAS_SUBFIELDS = typing___cast(FieldMaskErrorEnum.FieldMaskError, 3)


    def __init__(self,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> FieldMaskErrorEnum: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
