from collections.abc import Mapping, MutableSequence
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v14.enums.types.custom_audience_member_type import (
    CustomAudienceMemberTypeEnum,
)
from google.ads.googleads.v14.enums.types.custom_audience_status import (
    CustomAudienceStatusEnum,
)
from google.ads.googleads.v14.enums.types.custom_audience_type import (
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
        members: MutableSequence[CustomAudienceMember] = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "resource_name", "id", "status", "name", "type_", "description", "members"
        ],
    ) -> bool: ...

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
        app: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["member_type", "keyword", "url", "place_category", "app"]
    ) -> bool: ...
