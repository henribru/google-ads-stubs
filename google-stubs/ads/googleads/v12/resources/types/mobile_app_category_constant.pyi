from typing import Any

import proto

class MobileAppCategoryConstant(proto.Message):
    resource_name: str
    id: int
    name: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        id: int = ...,
        name: str = ...
    ) -> None: ...
