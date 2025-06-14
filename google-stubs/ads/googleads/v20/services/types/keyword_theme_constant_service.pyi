import proto
from _typeshed import Incomplete
from google.ads.googleads.v20.resources.types import keyword_theme_constant
from typing import MutableSequence

__protobuf__: Incomplete

class SuggestKeywordThemeConstantsRequest(proto.Message):
    query_text: str
    country_code: str
    language_code: str

class SuggestKeywordThemeConstantsResponse(proto.Message):
    keyword_theme_constants: MutableSequence[keyword_theme_constant.KeywordThemeConstant]
