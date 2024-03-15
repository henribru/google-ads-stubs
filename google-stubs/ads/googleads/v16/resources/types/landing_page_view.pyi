from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class LandingPageView(proto.Message):
    resource_name: str
    unexpanded_final_url: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        unexpanded_final_url: str = ...
    ) -> None: ...
    def __contains__(self, key: Literal["resource_name", "unexpanded_final_url"]) -> bool: ...  # type: ignore[override]
