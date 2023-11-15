from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

_M = TypeVar("_M")

class Value(proto.Message):
    boolean_value: bool
    int64_value: int
    float_value: float
    double_value: float
    string_value: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        boolean_value: bool = ...,
        int64_value: int = ...,
        float_value: float = ...,
        double_value: float = ...,
        string_value: str = ...
    ) -> None: ...
