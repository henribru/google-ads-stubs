import abc
import typing
from typing import Any

from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials

from google.ads.googleads.v8.resources.types import smart_campaign_search_term_view
from google.ads.googleads.v8.services.types import (
    smart_campaign_search_term_view_service,
)

class SmartCampaignSearchTermViewServiceTransport(metaclass=abc.ABCMeta):
    AUTH_SCOPES: Any
    def __init__(
        self,
        *,
        host: str = ...,
        credentials: ga_credentials.Credentials = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...
    ) -> None: ...
    @property
    def get_smart_campaign_search_term_view(
        self,
    ) -> typing.Callable[
        [smart_campaign_search_term_view_service.GetSmartCampaignSearchTermViewRequest],
        smart_campaign_search_term_view.SmartCampaignSearchTermView,
    ]: ...
