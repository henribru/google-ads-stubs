from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class TextLabel(proto.Message):
    background_color: str
    description: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        background_color: str = ...,
        description: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["background_color", "description"]
    ) -> bool: ...
