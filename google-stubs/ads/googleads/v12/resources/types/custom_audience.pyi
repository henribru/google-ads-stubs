from collections.abc import MutableSequence
from typing import Any

import proto

from google.ads.googleads.v12.enums.types.custom_audience_member_type import (
    CustomAudienceMemberTypeEnum,
)
from google.ads.googleads.v12.enums.types.custom_audience_status import (
    CustomAudienceStatusEnum,
)
from google.ads.googleads.v12.enums.types.custom_audience_type import (
    CustomAudienceTypeEnum,
)

class CustomAudience(proto.Message):
    resource_name: str
    id: int
    status: CustomAudienceStatusEnum.CustomAudienceStatus
    name: str
    type_: CustomAudienceTypeEnum.CustomAudienceType
    description: str
    members: MutableSequence[CustomAudienceMember]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        id: int = ...,
        status: CustomAudienceStatusEnum.CustomAudienceStatus = ...,
        name: str = ...,
        type_: CustomAudienceTypeEnum.CustomAudienceType = ...,
        description: str = ...,
        members: MutableSequence[CustomAudienceMember] = ...
    ) -> None: ...

class CustomAudienceMember(proto.Message):
    member_type: CustomAudienceMemberTypeEnum.CustomAudienceMemberType
    keyword: str
    url: str
    place_category: int
    app: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        member_type: CustomAudienceMemberTypeEnum.CustomAudienceMemberType = ...,
        keyword: str = ...,
        url: str = ...,
        place_category: int = ...,
        app: str = ...
    ) -> None: ...
