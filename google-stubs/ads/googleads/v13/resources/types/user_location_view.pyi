from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

_M = TypeVar("_M")

class UserLocationView(proto.Message):
    resource_name: str
    country_criterion_id: int
    targeting_location: bool
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        country_criterion_id: int = ...,
        targeting_location: bool = ...
    ) -> None: ...
