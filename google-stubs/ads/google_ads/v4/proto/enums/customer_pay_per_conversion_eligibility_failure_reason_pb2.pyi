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

class CustomerPayPerConversionEligibilityFailureReasonEnum(
    google___protobuf___message___Message
):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    CustomerPayPerConversionEligibilityFailureReasonValue = typing___NewType(
        "CustomerPayPerConversionEligibilityFailureReasonValue", builtin___int
    )
    type___CustomerPayPerConversionEligibilityFailureReasonValue = (
        CustomerPayPerConversionEligibilityFailureReasonValue
    )
    CustomerPayPerConversionEligibilityFailureReason: _CustomerPayPerConversionEligibilityFailureReason
    class _CustomerPayPerConversionEligibilityFailureReason(
        google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[
            CustomerPayPerConversionEligibilityFailureReasonEnum.CustomerPayPerConversionEligibilityFailureReasonValue
        ]
    ):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        UNSPECIFIED = typing___cast(
            CustomerPayPerConversionEligibilityFailureReasonEnum.CustomerPayPerConversionEligibilityFailureReasonValue,
            0,
        )
        UNKNOWN = typing___cast(
            CustomerPayPerConversionEligibilityFailureReasonEnum.CustomerPayPerConversionEligibilityFailureReasonValue,
            1,
        )
        NOT_ENOUGH_CONVERSIONS = typing___cast(
            CustomerPayPerConversionEligibilityFailureReasonEnum.CustomerPayPerConversionEligibilityFailureReasonValue,
            2,
        )
        CONVERSION_LAG_TOO_HIGH = typing___cast(
            CustomerPayPerConversionEligibilityFailureReasonEnum.CustomerPayPerConversionEligibilityFailureReasonValue,
            3,
        )
        HAS_CAMPAIGN_WITH_SHARED_BUDGET = typing___cast(
            CustomerPayPerConversionEligibilityFailureReasonEnum.CustomerPayPerConversionEligibilityFailureReasonValue,
            4,
        )
        HAS_UPLOAD_CLICKS_CONVERSION = typing___cast(
            CustomerPayPerConversionEligibilityFailureReasonEnum.CustomerPayPerConversionEligibilityFailureReasonValue,
            5,
        )
        AVERAGE_DAILY_SPEND_TOO_HIGH = typing___cast(
            CustomerPayPerConversionEligibilityFailureReasonEnum.CustomerPayPerConversionEligibilityFailureReasonValue,
            6,
        )
        ANALYSIS_NOT_COMPLETE = typing___cast(
            CustomerPayPerConversionEligibilityFailureReasonEnum.CustomerPayPerConversionEligibilityFailureReasonValue,
            7,
        )
        OTHER = typing___cast(
            CustomerPayPerConversionEligibilityFailureReasonEnum.CustomerPayPerConversionEligibilityFailureReasonValue,
            8,
        )
    UNSPECIFIED = typing___cast(
        CustomerPayPerConversionEligibilityFailureReasonEnum.CustomerPayPerConversionEligibilityFailureReasonValue,
        0,
    )
    UNKNOWN = typing___cast(
        CustomerPayPerConversionEligibilityFailureReasonEnum.CustomerPayPerConversionEligibilityFailureReasonValue,
        1,
    )
    NOT_ENOUGH_CONVERSIONS = typing___cast(
        CustomerPayPerConversionEligibilityFailureReasonEnum.CustomerPayPerConversionEligibilityFailureReasonValue,
        2,
    )
    CONVERSION_LAG_TOO_HIGH = typing___cast(
        CustomerPayPerConversionEligibilityFailureReasonEnum.CustomerPayPerConversionEligibilityFailureReasonValue,
        3,
    )
    HAS_CAMPAIGN_WITH_SHARED_BUDGET = typing___cast(
        CustomerPayPerConversionEligibilityFailureReasonEnum.CustomerPayPerConversionEligibilityFailureReasonValue,
        4,
    )
    HAS_UPLOAD_CLICKS_CONVERSION = typing___cast(
        CustomerPayPerConversionEligibilityFailureReasonEnum.CustomerPayPerConversionEligibilityFailureReasonValue,
        5,
    )
    AVERAGE_DAILY_SPEND_TOO_HIGH = typing___cast(
        CustomerPayPerConversionEligibilityFailureReasonEnum.CustomerPayPerConversionEligibilityFailureReasonValue,
        6,
    )
    ANALYSIS_NOT_COMPLETE = typing___cast(
        CustomerPayPerConversionEligibilityFailureReasonEnum.CustomerPayPerConversionEligibilityFailureReasonValue,
        7,
    )
    OTHER = typing___cast(
        CustomerPayPerConversionEligibilityFailureReasonEnum.CustomerPayPerConversionEligibilityFailureReasonValue,
        8,
    )
    type___CustomerPayPerConversionEligibilityFailureReason = (
        CustomerPayPerConversionEligibilityFailureReason
    )
    def __init__(self,) -> None: ...

type___CustomerPayPerConversionEligibilityFailureReasonEnum = (
    CustomerPayPerConversionEligibilityFailureReasonEnum
)
