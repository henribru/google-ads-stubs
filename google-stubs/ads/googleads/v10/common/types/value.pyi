from typing import Any

import proto

class Value(proto.Message):
    boolean_value: bool
    int64_value: int
    float_value: float
    double_value: float
    string_value: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        boolean_value: bool = ...,
        int64_value: int = ...,
        float_value: float = ...,
        double_value: float = ...,
        string_value: str = ...
    ) -> None: ...
