import proto
from _typeshed import Incomplete
from google.ads.googleads.v20.enums.types import custom_interest_member_type, custom_interest_status, custom_interest_type
from typing import MutableSequence

__protobuf__: Incomplete

class CustomInterest(proto.Message):
    resource_name: str
    id: int
    status: custom_interest_status.CustomInterestStatusEnum.CustomInterestStatus
    name: str
    type_: custom_interest_type.CustomInterestTypeEnum.CustomInterestType
    description: str
    members: MutableSequence['CustomInterestMember']

class CustomInterestMember(proto.Message):
    member_type: custom_interest_member_type.CustomInterestMemberTypeEnum.CustomInterestMemberType
    parameter: str
