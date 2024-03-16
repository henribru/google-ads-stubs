from collections.abc import Mapping, MutableSequence
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v16.resources.types.keyword_theme_constant import (
    KeywordThemeConstant,
)

_M = TypeVar("_M")

class SuggestKeywordThemeConstantsRequest(proto.Message):
    query_text: str
    country_code: str
    language_code: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        query_text: str = ...,
        country_code: str = ...,
        language_code: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["query_text", "country_code", "language_code"]
    ) -> bool: ...

class SuggestKeywordThemeConstantsResponse(proto.Message):
    keyword_theme_constants: MutableSequence[KeywordThemeConstant]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        keyword_theme_constants: MutableSequence[KeywordThemeConstant] = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["keyword_theme_constants"]
    ) -> bool: ...
