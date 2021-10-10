import abc
import typing
from typing import Any

from google.api_core import gapic_v1
from google.auth import credentials

from google.ads.googleads.v7.resources.types import third_party_app_analytics_link
from google.ads.googleads.v7.services.types import (
    third_party_app_analytics_link_service,
)

class ThirdPartyAppAnalyticsLinkServiceTransport(metaclass=abc.ABCMeta):
    AUTH_SCOPES: Any
    def __init__(
        self,
        *,
        host: str = ...,
        credentials: credentials.Credentials = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...
    ) -> None: ...
    @property
    def get_third_party_app_analytics_link(
        self,
    ) -> typing.Callable[
        [third_party_app_analytics_link_service.GetThirdPartyAppAnalyticsLinkRequest],
        third_party_app_analytics_link.ThirdPartyAppAnalyticsLink,
    ]: ...
    @property
    def regenerate_shareable_link_id(
        self,
    ) -> typing.Callable[
        [third_party_app_analytics_link_service.RegenerateShareableLinkIdRequest],
        third_party_app_analytics_link_service.RegenerateShareableLinkIdResponse,
    ]: ...
