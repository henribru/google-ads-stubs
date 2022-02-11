import abc
import typing
from typing import Any

from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials

from google.ads.googleads.v9.services.types import (
    conversion_goal_campaign_config_service,
)

class ConversionGoalCampaignConfigServiceTransport(metaclass=abc.ABCMeta):
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
    def mutate_conversion_goal_campaign_configs(
        self,
    ) -> typing.Callable[
        [
            conversion_goal_campaign_config_service.MutateConversionGoalCampaignConfigsRequest
        ],
        conversion_goal_campaign_config_service.MutateConversionGoalCampaignConfigsResponse,
    ]: ...
