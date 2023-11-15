from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

_M = TypeVar("_M")

class FeedItemSetLink(proto.Message):
    resource_name: str
    feed_item: str
    feed_item_set: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        feed_item: str = ...,
        feed_item_set: str = ...
    ) -> None: ...
