import abc
import typing
from typing import Any

from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials

from google.ads.googleads.v8.resources.types import keyword_plan_campaign
from google.ads.googleads.v8.services.types import keyword_plan_campaign_service

class KeywordPlanCampaignServiceTransport(metaclass=abc.ABCMeta):
    AUTH_SCOPES: Any
    def __init__(
        self,
        *,
        host: str = ...,
        credentials: ga_credentials.Credentials = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...
    ) -> None: ...
    @property
    def get_keyword_plan_campaign(
        self,
    ) -> typing.Callable[
        [keyword_plan_campaign_service.GetKeywordPlanCampaignRequest],
        keyword_plan_campaign.KeywordPlanCampaign,
    ]: ...
    @property
    def mutate_keyword_plan_campaigns(
        self,
    ) -> typing.Callable[
        [keyword_plan_campaign_service.MutateKeywordPlanCampaignsRequest],
        keyword_plan_campaign_service.MutateKeywordPlanCampaignsResponse,
    ]: ...
