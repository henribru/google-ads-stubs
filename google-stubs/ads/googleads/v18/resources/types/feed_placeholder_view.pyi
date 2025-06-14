from google.ads.googleads.v18.enums.types.placeholder_type import PlaceholderTypeEnum
import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class FeedPlaceholderView(proto.Message):
    resource_name: str
    placeholder_type: PlaceholderTypeEnum.PlaceholderType
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, resource_name: str = ..., placeholder_type: PlaceholderTypeEnum.PlaceholderType = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["resource_name", "placeholder_type"]) -> bool: ...
