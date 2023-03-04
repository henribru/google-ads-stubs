from typing import Any

import proto

class KeywordThemeConstant(proto.Message):
    resource_name: str
    country_code: str
    language_code: str
    display_name: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        country_code: str = ...,
        language_code: str = ...,
        display_name: str = ...
    ) -> None: ...
