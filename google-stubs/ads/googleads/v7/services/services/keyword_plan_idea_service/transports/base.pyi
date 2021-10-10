import abc
import typing
from typing import Any

from google.api_core import gapic_v1
from google.auth import credentials

from google.ads.googleads.v7.services.types import keyword_plan_idea_service

class KeywordPlanIdeaServiceTransport(metaclass=abc.ABCMeta):
    AUTH_SCOPES: Any
    def __init__(
        self,
        *,
        host: str = ...,
        credentials: credentials.Credentials = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...
    ) -> None: ...
    @property
    def generate_keyword_ideas(
        self,
    ) -> typing.Callable[
        [keyword_plan_idea_service.GenerateKeywordIdeasRequest],
        keyword_plan_idea_service.GenerateKeywordIdeaResponse,
    ]: ...
