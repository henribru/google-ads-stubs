from collections.abc import Mapping, MutableSequence
from typing import Any, TypeVar

import google.protobuf.message
import proto

from google.ads.googleads.v13.resources.types.keyword_theme_constant import (
    KeywordThemeConstant,
)

_M = TypeVar("_M")

class SuggestKeywordThemeConstantsRequest(proto.Message):
    query_text: str
    country_code: str
    language_code: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        query_text: str = ...,
        country_code: str = ...,
        language_code: str = ...
    ) -> None: ...

class SuggestKeywordThemeConstantsResponse(proto.Message):
    keyword_theme_constants: MutableSequence[KeywordThemeConstant]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        keyword_theme_constants: MutableSequence[KeywordThemeConstant] = ...
    ) -> None: ...
