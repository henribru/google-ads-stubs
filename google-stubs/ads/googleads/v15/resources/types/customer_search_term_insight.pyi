from typing import Any

import proto

class CustomerSearchTermInsight(proto.Message):
    resource_name: str
    category_label: str
    id: int
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        category_label: str = ...,
        id: int = ...
    ) -> None: ...
