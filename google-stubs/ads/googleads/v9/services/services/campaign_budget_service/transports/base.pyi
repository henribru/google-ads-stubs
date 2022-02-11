import abc
import typing
from typing import Any

from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials

from google.ads.googleads.v9.resources.types import campaign_budget
from google.ads.googleads.v9.services.types import campaign_budget_service

class CampaignBudgetServiceTransport(metaclass=abc.ABCMeta):
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
    def get_campaign_budget(
        self,
    ) -> typing.Callable[
        [campaign_budget_service.GetCampaignBudgetRequest],
        campaign_budget.CampaignBudget,
    ]: ...
    @property
    def mutate_campaign_budgets(
        self,
    ) -> typing.Callable[
        [campaign_budget_service.MutateCampaignBudgetsRequest],
        campaign_budget_service.MutateCampaignBudgetsResponse,
    ]: ...
