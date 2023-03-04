from typing import Any

import proto

class TextLabel(proto.Message):
    background_color: str
    description: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        background_color: str = ...,
        description: str = ...
    ) -> None: ...
