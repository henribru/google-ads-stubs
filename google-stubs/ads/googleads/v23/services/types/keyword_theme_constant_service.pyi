from collections.abc import MutableSequence
from google.ads.googleads.v23.resources.types.keyword_theme_constant import KeywordThemeConstant
import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class SuggestKeywordThemeConstantsRequest(proto.Message):
    query_text: str
    country_code: str
    language_code: str
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, query_text: str = ..., country_code: str = ..., language_code: str = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["query_text", "country_code", "language_code"]) -> bool: ...
class SuggestKeywordThemeConstantsResponse(proto.Message):
    keyword_theme_constants: MutableSequence[KeywordThemeConstant]
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, keyword_theme_constants: MutableSequence[KeywordThemeConstant] = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["keyword_theme_constants"]) -> bool: ...
