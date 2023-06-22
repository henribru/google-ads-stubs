from typing import Any

import proto

class CurrencyConstant(proto.Message):
    resource_name: str
    code: str
    name: str
    symbol: str
    billable_unit_micros: int
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        code: str = ...,
        name: str = ...,
        symbol: str = ...,
        billable_unit_micros: int = ...
    ) -> None: ...
