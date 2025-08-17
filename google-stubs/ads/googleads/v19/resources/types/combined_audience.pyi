from google.ads.googleads.v19.enums.types.combined_audience_status import CombinedAudienceStatusEnum
import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class CombinedAudience(proto.Message):
    resource_name: str
    id: int
    status: CombinedAudienceStatusEnum.CombinedAudienceStatus
    name: str
    description: str
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, resource_name: str = ..., id: int = ..., status: CombinedAudienceStatusEnum.CombinedAudienceStatus = ..., name: str = ..., description: str = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["resource_name", "id", "status", "name", "description"]) -> bool: ...
