from typing import Any

import proto

from google.ads.googleads.v9.resources.types import (
    keyword_theme_constant as keyword_theme_constant,
)

__protobuf__: Any

class GetKeywordThemeConstantRequest(proto.Message):
    resource_name: Any

class SuggestKeywordThemeConstantsRequest(proto.Message):
    query_text: Any
    country_code: Any
    language_code: Any

class SuggestKeywordThemeConstantsResponse(proto.Message):
    keyword_theme_constants: Any
