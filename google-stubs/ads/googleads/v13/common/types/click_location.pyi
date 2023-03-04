from typing import Any

import proto

class ClickLocation(proto.Message):
    city: str
    country: str
    metro: str
    most_specific: str
    region: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        city: str = ...,
        country: str = ...,
        metro: str = ...,
        most_specific: str = ...,
        region: str = ...
    ) -> None: ...
