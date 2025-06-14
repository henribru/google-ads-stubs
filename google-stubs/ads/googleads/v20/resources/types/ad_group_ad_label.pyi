import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class AdGroupAdLabel(proto.Message):
    resource_name: str
    ad_group_ad: str
    label: str
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., resource_name: str = ..., ad_group_ad: str = ..., label: str = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["resource_name", "ad_group_ad", "label"]) -> bool: ...
