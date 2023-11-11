from typing import Any

import proto

class Money(proto.Message):
    currency_code: str
    amount_micros: int
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        currency_code: str = ...,
        amount_micros: int = ...
    ) -> None: ...
