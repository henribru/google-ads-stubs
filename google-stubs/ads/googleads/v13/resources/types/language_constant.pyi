from typing import Any

import proto

class LanguageConstant(proto.Message):
    resource_name: str
    id: int
    code: str
    name: str
    targetable: bool
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        id: int = ...,
        code: str = ...,
        name: str = ...,
        targetable: bool = ...
    ) -> None: ...
