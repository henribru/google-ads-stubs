import abc
import typing
from typing import Any

from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials

from google.ads.googleads.v9.resources.types import keyword_plan_campaign_keyword
from google.ads.googleads.v9.services.types import keyword_plan_campaign_keyword_service

class KeywordPlanCampaignKeywordServiceTransport(metaclass=abc.ABCMeta):
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
    def get_keyword_plan_campaign_keyword(
        self,
    ) -> typing.Callable[
        [keyword_plan_campaign_keyword_service.GetKeywordPlanCampaignKeywordRequest],
        keyword_plan_campaign_keyword.KeywordPlanCampaignKeyword,
    ]: ...
    @property
    def mutate_keyword_plan_campaign_keywords(
        self,
    ) -> typing.Callable[
        [
            keyword_plan_campaign_keyword_service.MutateKeywordPlanCampaignKeywordsRequest
        ],
        keyword_plan_campaign_keyword_service.MutateKeywordPlanCampaignKeywordsResponse,
    ]: ...
