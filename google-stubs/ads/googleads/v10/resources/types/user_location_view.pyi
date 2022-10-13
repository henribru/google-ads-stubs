from typing import Any

import proto

class UserLocationView(proto.Message):
    resource_name: str
    country_criterion_id: int
    targeting_location: bool
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        country_criterion_id: int = ...,
        targeting_location: bool = ...
    ) -> None: ...
