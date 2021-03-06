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

class KeywordPlanKeywordErrorEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    KeywordPlanKeywordErrorValue = typing___NewType(
        "KeywordPlanKeywordErrorValue", builtin___int
    )
    type___KeywordPlanKeywordErrorValue = KeywordPlanKeywordErrorValue
    KeywordPlanKeywordError: _KeywordPlanKeywordError
    class _KeywordPlanKeywordError(
        google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[
            KeywordPlanKeywordErrorEnum.KeywordPlanKeywordErrorValue
        ]
    ):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        UNSPECIFIED = typing___cast(
            KeywordPlanKeywordErrorEnum.KeywordPlanKeywordErrorValue, 0
        )
        UNKNOWN = typing___cast(
            KeywordPlanKeywordErrorEnum.KeywordPlanKeywordErrorValue, 1
        )
        INVALID_KEYWORD_MATCH_TYPE = typing___cast(
            KeywordPlanKeywordErrorEnum.KeywordPlanKeywordErrorValue, 2
        )
        DUPLICATE_KEYWORD = typing___cast(
            KeywordPlanKeywordErrorEnum.KeywordPlanKeywordErrorValue, 3
        )
        KEYWORD_TEXT_TOO_LONG = typing___cast(
            KeywordPlanKeywordErrorEnum.KeywordPlanKeywordErrorValue, 4
        )
        KEYWORD_HAS_INVALID_CHARS = typing___cast(
            KeywordPlanKeywordErrorEnum.KeywordPlanKeywordErrorValue, 5
        )
        KEYWORD_HAS_TOO_MANY_WORDS = typing___cast(
            KeywordPlanKeywordErrorEnum.KeywordPlanKeywordErrorValue, 6
        )
        INVALID_KEYWORD_TEXT = typing___cast(
            KeywordPlanKeywordErrorEnum.KeywordPlanKeywordErrorValue, 7
        )
    UNSPECIFIED = typing___cast(
        KeywordPlanKeywordErrorEnum.KeywordPlanKeywordErrorValue, 0
    )
    UNKNOWN = typing___cast(KeywordPlanKeywordErrorEnum.KeywordPlanKeywordErrorValue, 1)
    INVALID_KEYWORD_MATCH_TYPE = typing___cast(
        KeywordPlanKeywordErrorEnum.KeywordPlanKeywordErrorValue, 2
    )
    DUPLICATE_KEYWORD = typing___cast(
        KeywordPlanKeywordErrorEnum.KeywordPlanKeywordErrorValue, 3
    )
    KEYWORD_TEXT_TOO_LONG = typing___cast(
        KeywordPlanKeywordErrorEnum.KeywordPlanKeywordErrorValue, 4
    )
    KEYWORD_HAS_INVALID_CHARS = typing___cast(
        KeywordPlanKeywordErrorEnum.KeywordPlanKeywordErrorValue, 5
    )
    KEYWORD_HAS_TOO_MANY_WORDS = typing___cast(
        KeywordPlanKeywordErrorEnum.KeywordPlanKeywordErrorValue, 6
    )
    INVALID_KEYWORD_TEXT = typing___cast(
        KeywordPlanKeywordErrorEnum.KeywordPlanKeywordErrorValue, 7
    )
    type___KeywordPlanKeywordError = KeywordPlanKeywordError
    def __init__(self,) -> None: ...

type___KeywordPlanKeywordErrorEnum = KeywordPlanKeywordErrorEnum
