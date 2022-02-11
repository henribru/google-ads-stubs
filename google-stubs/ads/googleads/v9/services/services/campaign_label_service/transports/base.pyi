import abc
import typing
from typing import Any

from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials

from google.ads.googleads.v9.resources.types import campaign_label
from google.ads.googleads.v9.services.types import campaign_label_service

class CampaignLabelServiceTransport(metaclass=abc.ABCMeta):
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
    def get_campaign_label(
        self,
    ) -> typing.Callable[
        [campaign_label_service.GetCampaignLabelRequest], campaign_label.CampaignLabel
    ]: ...
    @property
    def mutate_campaign_labels(
        self,
    ) -> typing.Callable[
        [campaign_label_service.MutateCampaignLabelsRequest],
        campaign_label_service.MutateCampaignLabelsResponse,
    ]: ...
