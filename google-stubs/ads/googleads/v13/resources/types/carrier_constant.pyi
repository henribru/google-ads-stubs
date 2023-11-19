from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class CarrierConstant(proto.Message):
    resource_name: str
    id: int
    name: str
    country_code: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        id: int = ...,
        name: str = ...,
        country_code: str = ...
    ) -> None: ...
    def __contains__(self, key: Literal["resource_name", "id", "name", "country_code"]) -> bool: ...  # type: ignore[override]
