from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

_M = TypeVar("_M")

class LifecycleGoalValueSettings(proto.Message):
    value: float
    high_lifetime_value: float
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        value: float = ...,
        high_lifetime_value: float = ...
    ) -> None: ...
