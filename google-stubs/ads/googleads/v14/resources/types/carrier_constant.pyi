from typing import Any

import proto

class CarrierConstant(proto.Message):
    resource_name: str
    id: int
    name: str
    country_code: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        id: int = ...,
        name: str = ...,
        country_code: str = ...
    ) -> None: ...
