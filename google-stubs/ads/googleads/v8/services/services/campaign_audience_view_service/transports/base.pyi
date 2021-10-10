import abc
import typing
from typing import Any

from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials

from google.ads.googleads.v8.resources.types import campaign_audience_view
from google.ads.googleads.v8.services.types import campaign_audience_view_service

class CampaignAudienceViewServiceTransport(metaclass=abc.ABCMeta):
    AUTH_SCOPES: Any
    def __init__(
        self,
        *,
        host: str = ...,
        credentials: ga_credentials.Credentials = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...
    ) -> None: ...
    @property
    def get_campaign_audience_view(
        self,
    ) -> typing.Callable[
        [campaign_audience_view_service.GetCampaignAudienceViewRequest],
        campaign_audience_view.CampaignAudienceView,
    ]: ...
