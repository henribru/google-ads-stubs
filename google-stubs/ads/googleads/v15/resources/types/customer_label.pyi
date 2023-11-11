from typing import Any

import proto

class CustomerLabel(proto.Message):
    resource_name: str
    customer: str
    label: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        customer: str = ...,
        label: str = ...
    ) -> None: ...
