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

class CustomerPayPerConversionEligibilityFailureReasonEnum(
    google___protobuf___message___Message
):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class CustomerPayPerConversionEligibilityFailureReason(builtin___int):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        @classmethod
        def Name(cls, number: builtin___int) -> builtin___str: ...
        @classmethod
        def Value(
            cls, name: builtin___str
        ) -> "CustomerPayPerConversionEligibilityFailureReasonEnum.CustomerPayPerConversionEligibilityFailureReason": ...
        @classmethod
        def keys(cls) -> typing___List[builtin___str]: ...
        @classmethod
        def values(
            cls,
        ) -> typing___List[
            "CustomerPayPerConversionEligibilityFailureReasonEnum.CustomerPayPerConversionEligibilityFailureReason"
        ]: ...
        @classmethod
        def items(
            cls,
        ) -> typing___List[
            typing___Tuple[
                builtin___str,
                "CustomerPayPerConversionEligibilityFailureReasonEnum.CustomerPayPerConversionEligibilityFailureReason",
            ]
        ]: ...
        UNSPECIFIED = typing___cast(
            "CustomerPayPerConversionEligibilityFailureReasonEnum.CustomerPayPerConversionEligibilityFailureReason",
            0,
        )
        UNKNOWN = typing___cast(
            "CustomerPayPerConversionEligibilityFailureReasonEnum.CustomerPayPerConversionEligibilityFailureReason",
            1,
        )
        NOT_ENOUGH_CONVERSIONS = typing___cast(
            "CustomerPayPerConversionEligibilityFailureReasonEnum.CustomerPayPerConversionEligibilityFailureReason",
            2,
        )
        CONVERSION_LAG_TOO_HIGH = typing___cast(
            "CustomerPayPerConversionEligibilityFailureReasonEnum.CustomerPayPerConversionEligibilityFailureReason",
            3,
        )
        HAS_CAMPAIGN_WITH_SHARED_BUDGET = typing___cast(
            "CustomerPayPerConversionEligibilityFailureReasonEnum.CustomerPayPerConversionEligibilityFailureReason",
            4,
        )
        HAS_UPLOAD_CLICKS_CONVERSION = typing___cast(
            "CustomerPayPerConversionEligibilityFailureReasonEnum.CustomerPayPerConversionEligibilityFailureReason",
            5,
        )
        AVERAGE_DAILY_SPEND_TOO_HIGH = typing___cast(
            "CustomerPayPerConversionEligibilityFailureReasonEnum.CustomerPayPerConversionEligibilityFailureReason",
            6,
        )
        ANALYSIS_NOT_COMPLETE = typing___cast(
            "CustomerPayPerConversionEligibilityFailureReasonEnum.CustomerPayPerConversionEligibilityFailureReason",
            7,
        )
        OTHER = typing___cast(
            "CustomerPayPerConversionEligibilityFailureReasonEnum.CustomerPayPerConversionEligibilityFailureReason",
            8,
        )
    UNSPECIFIED = typing___cast(
        "CustomerPayPerConversionEligibilityFailureReasonEnum.CustomerPayPerConversionEligibilityFailureReason",
        0,
    )
    UNKNOWN = typing___cast(
        "CustomerPayPerConversionEligibilityFailureReasonEnum.CustomerPayPerConversionEligibilityFailureReason",
        1,
    )
    NOT_ENOUGH_CONVERSIONS = typing___cast(
        "CustomerPayPerConversionEligibilityFailureReasonEnum.CustomerPayPerConversionEligibilityFailureReason",
        2,
    )
    CONVERSION_LAG_TOO_HIGH = typing___cast(
        "CustomerPayPerConversionEligibilityFailureReasonEnum.CustomerPayPerConversionEligibilityFailureReason",
        3,
    )
    HAS_CAMPAIGN_WITH_SHARED_BUDGET = typing___cast(
        "CustomerPayPerConversionEligibilityFailureReasonEnum.CustomerPayPerConversionEligibilityFailureReason",
        4,
    )
    HAS_UPLOAD_CLICKS_CONVERSION = typing___cast(
        "CustomerPayPerConversionEligibilityFailureReasonEnum.CustomerPayPerConversionEligibilityFailureReason",
        5,
    )
    AVERAGE_DAILY_SPEND_TOO_HIGH = typing___cast(
        "CustomerPayPerConversionEligibilityFailureReasonEnum.CustomerPayPerConversionEligibilityFailureReason",
        6,
    )
    ANALYSIS_NOT_COMPLETE = typing___cast(
        "CustomerPayPerConversionEligibilityFailureReasonEnum.CustomerPayPerConversionEligibilityFailureReason",
        7,
    )
    OTHER = typing___cast(
        "CustomerPayPerConversionEligibilityFailureReasonEnum.CustomerPayPerConversionEligibilityFailureReason",
        8,
    )
    global___CustomerPayPerConversionEligibilityFailureReason = (
        CustomerPayPerConversionEligibilityFailureReason
    )
    def __init__(self,) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(
            cls, s: builtin___bytes
        ) -> CustomerPayPerConversionEligibilityFailureReasonEnum: ...
    else:
        @classmethod
        def FromString(
            cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]
        ) -> CustomerPayPerConversionEligibilityFailureReasonEnum: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...

global___CustomerPayPerConversionEligibilityFailureReasonEnum = (
    CustomerPayPerConversionEligibilityFailureReasonEnum
)
