from google.ads.googleads.v23.enums.types.search_term_targeting_status import SearchTermTargetingStatusEnum
import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class SearchTermView(proto.Message):
    resource_name: str
    search_term: str
    ad_group: str
    status: SearchTermTargetingStatusEnum.SearchTermTargetingStatus
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, resource_name: str = ..., search_term: str = ..., ad_group: str = ..., status: SearchTermTargetingStatusEnum.SearchTermTargetingStatus = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["resource_name", "search_term", "ad_group", "status"]) -> bool: ...
