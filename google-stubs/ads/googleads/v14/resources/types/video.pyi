from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

_M = TypeVar("_M")

class Video(proto.Message):
    resource_name: str
    id: str
    channel_id: str
    duration_millis: int
    title: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        id: str = ...,
        channel_id: str = ...,
        duration_millis: int = ...,
        title: str = ...
    ) -> None: ...
