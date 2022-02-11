import abc
import typing
from typing import Any

from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials

from google.ads.googleads.v9.services.types import campaign_customizer_service

class CampaignCustomizerServiceTransport(metaclass=abc.ABCMeta):
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
    def mutate_campaign_customizers(
        self,
    ) -> typing.Callable[
        [campaign_customizer_service.MutateCampaignCustomizersRequest],
        campaign_customizer_service.MutateCampaignCustomizersResponse,
    ]: ...
