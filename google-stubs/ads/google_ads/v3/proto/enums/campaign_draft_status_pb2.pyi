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

class CampaignDraftStatusEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    CampaignDraftStatusValue = typing___NewType(
        "CampaignDraftStatusValue", builtin___int
    )
    type___CampaignDraftStatusValue = CampaignDraftStatusValue
    CampaignDraftStatus: _CampaignDraftStatus
    class _CampaignDraftStatus(
        google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[
            CampaignDraftStatusEnum.CampaignDraftStatusValue
        ]
    ):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        UNSPECIFIED = typing___cast(CampaignDraftStatusEnum.CampaignDraftStatusValue, 0)
        UNKNOWN = typing___cast(CampaignDraftStatusEnum.CampaignDraftStatusValue, 1)
        PROPOSED = typing___cast(CampaignDraftStatusEnum.CampaignDraftStatusValue, 2)
        REMOVED = typing___cast(CampaignDraftStatusEnum.CampaignDraftStatusValue, 3)
        PROMOTING = typing___cast(CampaignDraftStatusEnum.CampaignDraftStatusValue, 5)
        PROMOTED = typing___cast(CampaignDraftStatusEnum.CampaignDraftStatusValue, 4)
        PROMOTE_FAILED = typing___cast(
            CampaignDraftStatusEnum.CampaignDraftStatusValue, 6
        )
    UNSPECIFIED = typing___cast(CampaignDraftStatusEnum.CampaignDraftStatusValue, 0)
    UNKNOWN = typing___cast(CampaignDraftStatusEnum.CampaignDraftStatusValue, 1)
    PROPOSED = typing___cast(CampaignDraftStatusEnum.CampaignDraftStatusValue, 2)
    REMOVED = typing___cast(CampaignDraftStatusEnum.CampaignDraftStatusValue, 3)
    PROMOTING = typing___cast(CampaignDraftStatusEnum.CampaignDraftStatusValue, 5)
    PROMOTED = typing___cast(CampaignDraftStatusEnum.CampaignDraftStatusValue, 4)
    PROMOTE_FAILED = typing___cast(CampaignDraftStatusEnum.CampaignDraftStatusValue, 6)
    type___CampaignDraftStatus = CampaignDraftStatus
    def __init__(self,) -> None: ...

type___CampaignDraftStatusEnum = CampaignDraftStatusEnum
