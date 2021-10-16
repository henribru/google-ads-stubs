import abc
import typing
from typing import Any

from google.api_core import gapic_v1
from google.auth import credentials

from google.ads.googleads.v7.resources.types import dynamic_search_ads_search_term_view
from google.ads.googleads.v7.services.types import (
    dynamic_search_ads_search_term_view_service,
)

class DynamicSearchAdsSearchTermViewServiceTransport(metaclass=abc.ABCMeta):
    AUTH_SCOPES: Any
    def __init__(
        self,
        *,
        host: str = ...,
        credentials: credentials.Credentials = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...
    ) -> None: ...
    @property
    def get_dynamic_search_ads_search_term_view(
        self,
    ) -> typing.Callable[
        [
            dynamic_search_ads_search_term_view_service.GetDynamicSearchAdsSearchTermViewRequest
        ],
        dynamic_search_ads_search_term_view.DynamicSearchAdsSearchTermView,
    ]: ...
