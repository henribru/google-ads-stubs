from google.ads.googleads.v18.enums.types.custom_interest_member_type import CustomInterestMemberTypeEnum
from collections.abc import MutableSequence
from google.ads.googleads.v18.enums.types.custom_interest_type import CustomInterestTypeEnum
from google.ads.googleads.v18.enums.types.custom_interest_status import CustomInterestStatusEnum
import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class CustomInterest(proto.Message):
    resource_name: str
    id: int
    status: CustomInterestStatusEnum.CustomInterestStatus
    name: str
    type_: CustomInterestTypeEnum.CustomInterestType
    description: str
    members: MutableSequence[CustomInterestMember]
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., resource_name: str = ..., id: int = ..., status: CustomInterestStatusEnum.CustomInterestStatus = ..., name: str = ..., type_: CustomInterestTypeEnum.CustomInterestType = ..., description: str = ..., members: MutableSequence[CustomInterestMember] = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["resource_name", "id", "status", "name", "type_", "description", "members"]) -> bool: ...
class CustomInterestMember(proto.Message):
    member_type: CustomInterestMemberTypeEnum.CustomInterestMemberType
    parameter: str
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., member_type: CustomInterestMemberTypeEnum.CustomInterestMemberType = ..., parameter: str = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["member_type", "parameter"]) -> bool: ...
