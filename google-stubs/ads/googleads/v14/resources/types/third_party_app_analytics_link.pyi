from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

_M = TypeVar("_M")

class ThirdPartyAppAnalyticsLink(proto.Message):
    resource_name: str
    shareable_link_id: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        shareable_link_id: str = ...
    ) -> None: ...
