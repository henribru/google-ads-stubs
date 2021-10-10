import abc
import typing
from typing import Any

from google.api_core import gapic_v1
from google.auth import credentials

from google.ads.googleads.v7.resources.types import google_ads_field
from google.ads.googleads.v7.services.types import google_ads_field_service

class GoogleAdsFieldServiceTransport(metaclass=abc.ABCMeta):
    AUTH_SCOPES: Any
    def __init__(
        self,
        *,
        host: str = ...,
        credentials: credentials.Credentials = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...
    ) -> None: ...
    @property
    def get_google_ads_field(
        self,
    ) -> typing.Callable[
        [google_ads_field_service.GetGoogleAdsFieldRequest],
        google_ads_field.GoogleAdsField,
    ]: ...
    @property
    def search_google_ads_fields(
        self,
    ) -> typing.Callable[
        [google_ads_field_service.SearchGoogleAdsFieldsRequest],
        google_ads_field_service.SearchGoogleAdsFieldsResponse,
    ]: ...
