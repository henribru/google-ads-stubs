from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

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
        region: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["city", "country", "metro", "most_specific", "region"]
    ) -> bool: ...
