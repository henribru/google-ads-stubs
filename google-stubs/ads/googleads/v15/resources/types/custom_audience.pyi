from collections.abc import Mapping, MutableSequence
from typing import Any, TypeVar

import google.protobuf.message
import proto

from google.ads.googleads.v15.enums.types.custom_audience_member_type import (
    CustomAudienceMemberTypeEnum,
)
from google.ads.googleads.v15.enums.types.custom_audience_status import (
    CustomAudienceStatusEnum,
)
from google.ads.googleads.v15.enums.types.custom_audience_type import (
    CustomAudienceTypeEnum,
)

_M = TypeVar("_M")

class CustomAudience(proto.Message):
    resource_name: str
    id: int
    status: CustomAudienceStatusEnum.CustomAudienceStatus
    name: str
    type_: CustomAudienceTypeEnum.CustomAudienceType
    description: str
    members: MutableSequence[CustomAudienceMember]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
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
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        member_type: CustomAudienceMemberTypeEnum.CustomAudienceMemberType = ...,
        keyword: str = ...,
        url: str = ...,
        place_category: int = ...,
        app: str = ...
    ) -> None: ...
