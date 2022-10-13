from typing import Any

import proto

from google.ads.googleads.v11.enums.types.custom_interest_member_type import (
    CustomInterestMemberTypeEnum,
)
from google.ads.googleads.v11.enums.types.custom_interest_status import (
    CustomInterestStatusEnum,
)
from google.ads.googleads.v11.enums.types.custom_interest_type import (
    CustomInterestTypeEnum,
)

class CustomInterest(proto.Message):
    resource_name: str
    id: int
    status: CustomInterestStatusEnum.CustomInterestStatus
    name: str
    type_: CustomInterestTypeEnum.CustomInterestType
    description: str
    members: list[CustomInterestMember]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        id: int = ...,
        status: CustomInterestStatusEnum.CustomInterestStatus = ...,
        name: str = ...,
        type_: CustomInterestTypeEnum.CustomInterestType = ...,
        description: str = ...,
        members: list[CustomInterestMember] = ...
    ) -> None: ...

class CustomInterestMember(proto.Message):
    member_type: CustomInterestMemberTypeEnum.CustomInterestMemberType
    parameter: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        member_type: CustomInterestMemberTypeEnum.CustomInterestMemberType = ...,
        parameter: str = ...
    ) -> None: ...
