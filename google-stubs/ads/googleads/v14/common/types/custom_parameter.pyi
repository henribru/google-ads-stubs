from typing import Any

import proto

class CustomParameter(proto.Message):
    key: str
    value: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        key: str = ...,
        value: str = ...
    ) -> None: ...
