import abc
import typing
from typing import Any

from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials

from google.ads.googleads.v8.services.types import google_ads_service

class GoogleAdsServiceTransport(metaclass=abc.ABCMeta):
    AUTH_SCOPES: Any
    def __init__(
        self,
        *,
        host: str = ...,
        credentials: ga_credentials.Credentials = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...
    ) -> None: ...
    @property
    def search(
        self,
    ) -> typing.Callable[
        [google_ads_service.SearchGoogleAdsRequest],
        google_ads_service.SearchGoogleAdsResponse,
    ]: ...
    @property
    def search_stream(
        self,
    ) -> typing.Callable[
        [google_ads_service.SearchGoogleAdsStreamRequest],
        google_ads_service.SearchGoogleAdsStreamResponse,
    ]: ...
    @property
    def mutate(
        self,
    ) -> typing.Callable[
        [google_ads_service.MutateGoogleAdsRequest],
        google_ads_service.MutateGoogleAdsResponse,
    ]: ...
