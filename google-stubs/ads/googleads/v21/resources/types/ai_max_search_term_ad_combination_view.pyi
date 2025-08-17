import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class AiMaxSearchTermAdCombinationView(proto.Message):
    resource_name: str
    ad_group: str
    search_term: str
    landing_page: str
    headline: str
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, resource_name: str = ..., ad_group: str = ..., search_term: str = ..., landing_page: str = ..., headline: str = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["resource_name", "ad_group", "search_term", "landing_page", "headline"]) -> bool: ...
