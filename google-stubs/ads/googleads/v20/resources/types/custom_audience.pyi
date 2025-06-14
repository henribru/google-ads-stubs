from google.ads.googleads.v20.enums.types.custom_audience_member_type import CustomAudienceMemberTypeEnum
from collections.abc import MutableSequence
from google.ads.googleads.v20.enums.types.custom_audience_type import CustomAudienceTypeEnum
from google.ads.googleads.v20.enums.types.custom_audience_status import CustomAudienceStatusEnum
import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class CustomAudience(proto.Message):
    resource_name: str
    id: int
    status: CustomAudienceStatusEnum.CustomAudienceStatus
    name: str
    type_: CustomAudienceTypeEnum.CustomAudienceType
    description: str
    members: MutableSequence[CustomAudienceMember]
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., resource_name: str = ..., id: int = ..., status: CustomAudienceStatusEnum.CustomAudienceStatus = ..., name: str = ..., type_: CustomAudienceTypeEnum.CustomAudienceType = ..., description: str = ..., members: MutableSequence[CustomAudienceMember] = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["resource_name", "id", "status", "name", "type_", "description", "members"]) -> bool: ...
class CustomAudienceMember(proto.Message):
    member_type: CustomAudienceMemberTypeEnum.CustomAudienceMemberType
    keyword: str
    url: str
    place_category: int
    app: str
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., member_type: CustomAudienceMemberTypeEnum.CustomAudienceMemberType = ..., keyword: str = ..., url: str = ..., place_category: int = ..., app: str = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["member_type", "keyword", "url", "place_category", "app"]) -> bool: ...
