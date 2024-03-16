from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

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
        string_value: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "boolean_value",
            "int64_value",
            "float_value",
            "double_value",
            "string_value",
        ],
    ) -> bool: ...
