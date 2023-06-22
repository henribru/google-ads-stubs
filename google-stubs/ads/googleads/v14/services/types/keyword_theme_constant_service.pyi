from collections.abc import MutableSequence
from typing import Any

import proto

from google.ads.googleads.v14.resources.types.keyword_theme_constant import (
    KeywordThemeConstant,
)

class SuggestKeywordThemeConstantsRequest(proto.Message):
    query_text: str
    country_code: str
    language_code: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        query_text: str = ...,
        country_code: str = ...,
        language_code: str = ...
    ) -> None: ...

class SuggestKeywordThemeConstantsResponse(proto.Message):
    keyword_theme_constants: MutableSequence[KeywordThemeConstant]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        keyword_theme_constants: MutableSequence[KeywordThemeConstant] = ...
    ) -> None: ...
