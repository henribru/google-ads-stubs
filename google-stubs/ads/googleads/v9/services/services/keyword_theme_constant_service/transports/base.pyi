import abc
import typing
from typing import Any

from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials

from google.ads.googleads.v9.resources.types import keyword_theme_constant
from google.ads.googleads.v9.services.types import keyword_theme_constant_service

class KeywordThemeConstantServiceTransport(metaclass=abc.ABCMeta):
    AUTH_SCOPES: Any
    def __init__(
        self,
        *,
        host: str = ...,
        credentials: ga_credentials.Credentials = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...
    ) -> None: ...
    def close(self) -> None: ...
    @property
    def get_keyword_theme_constant(
        self,
    ) -> typing.Callable[
        [keyword_theme_constant_service.GetKeywordThemeConstantRequest],
        keyword_theme_constant.KeywordThemeConstant,
    ]: ...
    @property
    def suggest_keyword_theme_constants(
        self,
    ) -> typing.Callable[
        [keyword_theme_constant_service.SuggestKeywordThemeConstantsRequest],
        keyword_theme_constant_service.SuggestKeywordThemeConstantsResponse,
    ]: ...
