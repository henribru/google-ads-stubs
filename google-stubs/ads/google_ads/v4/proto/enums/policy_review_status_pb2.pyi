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

class PolicyReviewStatusEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    PolicyReviewStatusValue = typing___NewType("PolicyReviewStatusValue", builtin___int)
    type___PolicyReviewStatusValue = PolicyReviewStatusValue
    PolicyReviewStatus: _PolicyReviewStatus
    class _PolicyReviewStatus(
        google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[
            PolicyReviewStatusEnum.PolicyReviewStatusValue
        ]
    ):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        UNSPECIFIED = typing___cast(PolicyReviewStatusEnum.PolicyReviewStatusValue, 0)
        UNKNOWN = typing___cast(PolicyReviewStatusEnum.PolicyReviewStatusValue, 1)
        REVIEW_IN_PROGRESS = typing___cast(
            PolicyReviewStatusEnum.PolicyReviewStatusValue, 2
        )
        REVIEWED = typing___cast(PolicyReviewStatusEnum.PolicyReviewStatusValue, 3)
        UNDER_APPEAL = typing___cast(PolicyReviewStatusEnum.PolicyReviewStatusValue, 4)
        ELIGIBLE_MAY_SERVE = typing___cast(
            PolicyReviewStatusEnum.PolicyReviewStatusValue, 5
        )
    UNSPECIFIED = typing___cast(PolicyReviewStatusEnum.PolicyReviewStatusValue, 0)
    UNKNOWN = typing___cast(PolicyReviewStatusEnum.PolicyReviewStatusValue, 1)
    REVIEW_IN_PROGRESS = typing___cast(
        PolicyReviewStatusEnum.PolicyReviewStatusValue, 2
    )
    REVIEWED = typing___cast(PolicyReviewStatusEnum.PolicyReviewStatusValue, 3)
    UNDER_APPEAL = typing___cast(PolicyReviewStatusEnum.PolicyReviewStatusValue, 4)
    ELIGIBLE_MAY_SERVE = typing___cast(
        PolicyReviewStatusEnum.PolicyReviewStatusValue, 5
    )
    type___PolicyReviewStatus = PolicyReviewStatus
    def __init__(self,) -> None: ...

type___PolicyReviewStatusEnum = PolicyReviewStatusEnum
