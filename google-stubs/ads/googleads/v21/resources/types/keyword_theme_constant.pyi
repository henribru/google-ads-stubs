from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class KeywordThemeConstant(proto.Message):
    resource_name: str
    country_code: str
    language_code: str
    display_name: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        country_code: str = ...,
        language_code: str = ...,
        display_name: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal["resource_name", "country_code", "language_code", "display_name"],
    ) -> bool: ...
