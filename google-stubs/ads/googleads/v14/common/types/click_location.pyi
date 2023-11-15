from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

_M = TypeVar("_M")

class ClickLocation(proto.Message):
    city: str
    country: str
    metro: str
    most_specific: str
    region: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        city: str = ...,
        country: str = ...,
        metro: str = ...,
        most_specific: str = ...,
        region: str = ...
    ) -> None: ...
