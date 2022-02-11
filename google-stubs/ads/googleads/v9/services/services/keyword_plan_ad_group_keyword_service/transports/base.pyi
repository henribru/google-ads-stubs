import abc
import typing
from typing import Any

from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials

from google.ads.googleads.v9.resources.types import keyword_plan_ad_group_keyword
from google.ads.googleads.v9.services.types import keyword_plan_ad_group_keyword_service

class KeywordPlanAdGroupKeywordServiceTransport(metaclass=abc.ABCMeta):
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
    def get_keyword_plan_ad_group_keyword(
        self,
    ) -> typing.Callable[
        [keyword_plan_ad_group_keyword_service.GetKeywordPlanAdGroupKeywordRequest],
        keyword_plan_ad_group_keyword.KeywordPlanAdGroupKeyword,
    ]: ...
    @property
    def mutate_keyword_plan_ad_group_keywords(
        self,
    ) -> typing.Callable[
        [keyword_plan_ad_group_keyword_service.MutateKeywordPlanAdGroupKeywordsRequest],
        keyword_plan_ad_group_keyword_service.MutateKeywordPlanAdGroupKeywordsResponse,
    ]: ...
