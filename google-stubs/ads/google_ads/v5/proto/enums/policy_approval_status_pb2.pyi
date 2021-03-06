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

class PolicyApprovalStatusEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    PolicyApprovalStatusValue = typing___NewType(
        "PolicyApprovalStatusValue", builtin___int
    )
    type___PolicyApprovalStatusValue = PolicyApprovalStatusValue
    PolicyApprovalStatus: _PolicyApprovalStatus
    class _PolicyApprovalStatus(
        google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[
            PolicyApprovalStatusEnum.PolicyApprovalStatusValue
        ]
    ):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        UNSPECIFIED = typing___cast(
            PolicyApprovalStatusEnum.PolicyApprovalStatusValue, 0
        )
        UNKNOWN = typing___cast(PolicyApprovalStatusEnum.PolicyApprovalStatusValue, 1)
        DISAPPROVED = typing___cast(
            PolicyApprovalStatusEnum.PolicyApprovalStatusValue, 2
        )
        APPROVED_LIMITED = typing___cast(
            PolicyApprovalStatusEnum.PolicyApprovalStatusValue, 3
        )
        APPROVED = typing___cast(PolicyApprovalStatusEnum.PolicyApprovalStatusValue, 4)
        AREA_OF_INTEREST_ONLY = typing___cast(
            PolicyApprovalStatusEnum.PolicyApprovalStatusValue, 5
        )
    UNSPECIFIED = typing___cast(PolicyApprovalStatusEnum.PolicyApprovalStatusValue, 0)
    UNKNOWN = typing___cast(PolicyApprovalStatusEnum.PolicyApprovalStatusValue, 1)
    DISAPPROVED = typing___cast(PolicyApprovalStatusEnum.PolicyApprovalStatusValue, 2)
    APPROVED_LIMITED = typing___cast(
        PolicyApprovalStatusEnum.PolicyApprovalStatusValue, 3
    )
    APPROVED = typing___cast(PolicyApprovalStatusEnum.PolicyApprovalStatusValue, 4)
    AREA_OF_INTEREST_ONLY = typing___cast(
        PolicyApprovalStatusEnum.PolicyApprovalStatusValue, 5
    )
    type___PolicyApprovalStatus = PolicyApprovalStatus
    def __init__(self,) -> None: ...

type___PolicyApprovalStatusEnum = PolicyApprovalStatusEnum
