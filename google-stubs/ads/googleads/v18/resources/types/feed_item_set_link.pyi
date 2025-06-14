import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class FeedItemSetLink(proto.Message):
    resource_name: str
    feed_item: str
    feed_item_set: str
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, resource_name: str = ..., feed_item: str = ..., feed_item_set: str = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["resource_name", "feed_item", "feed_item_set"]) -> bool: ...
