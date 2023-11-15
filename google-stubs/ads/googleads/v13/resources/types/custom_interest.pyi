from collections.abc import Mapping, MutableSequence
from typing import Any, TypeVar

import google.protobuf.message
import proto

from google.ads.googleads.v13.enums.types.custom_interest_member_type import (
    CustomInterestMemberTypeEnum,
)
from google.ads.googleads.v13.enums.types.custom_interest_status import (
    CustomInterestStatusEnum,
)
from google.ads.googleads.v13.enums.types.custom_interest_type import (
    CustomInterestTypeEnum,
)

_M = TypeVar("_M")

class CustomInterest(proto.Message):
    resource_name: str
    id: int
    status: CustomInterestStatusEnum.CustomInterestStatus
    name: str
    type_: CustomInterestTypeEnum.CustomInterestType
    description: str
    members: MutableSequence[CustomInterestMember]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        id: int = ...,
        status: CustomInterestStatusEnum.CustomInterestStatus = ...,
        name: str = ...,
        type_: CustomInterestTypeEnum.CustomInterestType = ...,
        description: str = ...,
        members: MutableSequence[CustomInterestMember] = ...
    ) -> None: ...

class CustomInterestMember(proto.Message):
    member_type: CustomInterestMemberTypeEnum.CustomInterestMemberType
    parameter: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        member_type: CustomInterestMemberTypeEnum.CustomInterestMemberType = ...,
        parameter: str = ...
    ) -> None: ...
