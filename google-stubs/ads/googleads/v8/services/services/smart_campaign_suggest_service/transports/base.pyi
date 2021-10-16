import abc
import typing
from typing import Any

from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials

from google.ads.googleads.v8.services.types import smart_campaign_suggest_service

class SmartCampaignSuggestServiceTransport(metaclass=abc.ABCMeta):
    AUTH_SCOPES: Any
    def __init__(
        self,
        *,
        host: str = ...,
        credentials: ga_credentials.Credentials = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...
    ) -> None: ...
    @property
    def suggest_smart_campaign_budget_options(
        self,
    ) -> typing.Callable[
        [smart_campaign_suggest_service.SuggestSmartCampaignBudgetOptionsRequest],
        smart_campaign_suggest_service.SuggestSmartCampaignBudgetOptionsResponse,
    ]: ...
    @property
    def suggest_smart_campaign_ad(
        self,
    ) -> typing.Callable[
        [smart_campaign_suggest_service.SuggestSmartCampaignAdRequest],
        smart_campaign_suggest_service.SuggestSmartCampaignAdResponse,
    ]: ...
