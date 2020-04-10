# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    EnumDescriptor as google___protobuf___descriptor___EnumDescriptor,
)

from google.protobuf.message import Message as google___protobuf___message___Message

from typing import (
    List as typing___List,
    Tuple as typing___Tuple,
    Union as typing___Union,
    cast as typing___cast,
)

builtin___bytes = bytes
builtin___int = int
builtin___str = str
if sys.version_info < (3,):
    builtin___buffer = buffer
    builtin___unicode = unicode

class KeywordPlanErrorEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class KeywordPlanError(builtin___int):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        @classmethod
        def Name(cls, number: builtin___int) -> builtin___str: ...
        @classmethod
        def Value(
            cls, name: builtin___str
        ) -> "KeywordPlanErrorEnum.KeywordPlanError": ...
        @classmethod
        def keys(cls) -> typing___List[builtin___str]: ...
        @classmethod
        def values(cls) -> typing___List["KeywordPlanErrorEnum.KeywordPlanError"]: ...
        @classmethod
        def items(
            cls,
        ) -> typing___List[
            typing___Tuple[builtin___str, "KeywordPlanErrorEnum.KeywordPlanError"]
        ]: ...
        UNSPECIFIED = typing___cast("KeywordPlanErrorEnum.KeywordPlanError", 0)
        UNKNOWN = typing___cast("KeywordPlanErrorEnum.KeywordPlanError", 1)
        BID_MULTIPLIER_OUT_OF_RANGE = typing___cast(
            "KeywordPlanErrorEnum.KeywordPlanError", 2
        )
        BID_TOO_HIGH = typing___cast("KeywordPlanErrorEnum.KeywordPlanError", 3)
        BID_TOO_LOW = typing___cast("KeywordPlanErrorEnum.KeywordPlanError", 4)
        BID_TOO_MANY_FRACTIONAL_DIGITS = typing___cast(
            "KeywordPlanErrorEnum.KeywordPlanError", 5
        )
        DAILY_BUDGET_TOO_LOW = typing___cast("KeywordPlanErrorEnum.KeywordPlanError", 6)
        DAILY_BUDGET_TOO_MANY_FRACTIONAL_DIGITS = typing___cast(
            "KeywordPlanErrorEnum.KeywordPlanError", 7
        )
        INVALID_VALUE = typing___cast("KeywordPlanErrorEnum.KeywordPlanError", 8)
        KEYWORD_PLAN_HAS_NO_KEYWORDS = typing___cast(
            "KeywordPlanErrorEnum.KeywordPlanError", 9
        )
        KEYWORD_PLAN_NOT_ENABLED = typing___cast(
            "KeywordPlanErrorEnum.KeywordPlanError", 10
        )
        KEYWORD_PLAN_NOT_FOUND = typing___cast(
            "KeywordPlanErrorEnum.KeywordPlanError", 11
        )
        MISSING_BID = typing___cast("KeywordPlanErrorEnum.KeywordPlanError", 13)
        MISSING_FORECAST_PERIOD = typing___cast(
            "KeywordPlanErrorEnum.KeywordPlanError", 14
        )
        INVALID_FORECAST_DATE_RANGE = typing___cast(
            "KeywordPlanErrorEnum.KeywordPlanError", 15
        )
        INVALID_NAME = typing___cast("KeywordPlanErrorEnum.KeywordPlanError", 16)
    UNSPECIFIED = typing___cast("KeywordPlanErrorEnum.KeywordPlanError", 0)
    UNKNOWN = typing___cast("KeywordPlanErrorEnum.KeywordPlanError", 1)
    BID_MULTIPLIER_OUT_OF_RANGE = typing___cast(
        "KeywordPlanErrorEnum.KeywordPlanError", 2
    )
    BID_TOO_HIGH = typing___cast("KeywordPlanErrorEnum.KeywordPlanError", 3)
    BID_TOO_LOW = typing___cast("KeywordPlanErrorEnum.KeywordPlanError", 4)
    BID_TOO_MANY_FRACTIONAL_DIGITS = typing___cast(
        "KeywordPlanErrorEnum.KeywordPlanError", 5
    )
    DAILY_BUDGET_TOO_LOW = typing___cast("KeywordPlanErrorEnum.KeywordPlanError", 6)
    DAILY_BUDGET_TOO_MANY_FRACTIONAL_DIGITS = typing___cast(
        "KeywordPlanErrorEnum.KeywordPlanError", 7
    )
    INVALID_VALUE = typing___cast("KeywordPlanErrorEnum.KeywordPlanError", 8)
    KEYWORD_PLAN_HAS_NO_KEYWORDS = typing___cast(
        "KeywordPlanErrorEnum.KeywordPlanError", 9
    )
    KEYWORD_PLAN_NOT_ENABLED = typing___cast(
        "KeywordPlanErrorEnum.KeywordPlanError", 10
    )
    KEYWORD_PLAN_NOT_FOUND = typing___cast("KeywordPlanErrorEnum.KeywordPlanError", 11)
    MISSING_BID = typing___cast("KeywordPlanErrorEnum.KeywordPlanError", 13)
    MISSING_FORECAST_PERIOD = typing___cast("KeywordPlanErrorEnum.KeywordPlanError", 14)
    INVALID_FORECAST_DATE_RANGE = typing___cast(
        "KeywordPlanErrorEnum.KeywordPlanError", 15
    )
    INVALID_NAME = typing___cast("KeywordPlanErrorEnum.KeywordPlanError", 16)
    global___KeywordPlanError = KeywordPlanError
    def __init__(self,) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> KeywordPlanErrorEnum: ...
    else:
        @classmethod
        def FromString(
            cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]
        ) -> KeywordPlanErrorEnum: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...

global___KeywordPlanErrorEnum = KeywordPlanErrorEnum
