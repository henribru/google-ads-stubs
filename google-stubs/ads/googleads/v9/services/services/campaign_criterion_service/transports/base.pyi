import abc
import typing
from typing import Any

from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials

from google.ads.googleads.v9.resources.types import campaign_criterion
from google.ads.googleads.v9.services.types import campaign_criterion_service

class CampaignCriterionServiceTransport(metaclass=abc.ABCMeta):
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
    def get_campaign_criterion(
        self,
    ) -> typing.Callable[
        [campaign_criterion_service.GetCampaignCriterionRequest],
        campaign_criterion.CampaignCriterion,
    ]: ...
    @property
    def mutate_campaign_criteria(
        self,
    ) -> typing.Callable[
        [campaign_criterion_service.MutateCampaignCriteriaRequest],
        campaign_criterion_service.MutateCampaignCriteriaResponse,
    ]: ...
