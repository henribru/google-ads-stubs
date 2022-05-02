import abc
from typing import Awaitable, Callable, Optional, Sequence, Union

from _typeshed import Incomplete
from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials

from google.ads.googleads.v10.resources.types import google_ads_field
from google.ads.googleads.v10.services.types import google_ads_field_service

class GoogleAdsFieldServiceTransport(abc.ABC):
    AUTH_SCOPES: Incomplete
    DEFAULT_HOST: str
    def __init__(
        self,
        *,
        host: str = ...,
        credentials: ga_credentials.Credentials = ...,
        credentials_file: Optional[str] = ...,
        scopes: Optional[Sequence[str]] = ...,
        quota_project_id: Optional[str] = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...,
        always_use_jwt_access: Optional[bool] = ...,
        **kwargs
    ) -> None: ...
    def close(self) -> None: ...
    @property
    def get_google_ads_field(
        self,
    ) -> Callable[
        [google_ads_field_service.GetGoogleAdsFieldRequest],
        Union[
            google_ads_field.GoogleAdsField, Awaitable[google_ads_field.GoogleAdsField]
        ],
    ]: ...
    @property
    def search_google_ads_fields(
        self,
    ) -> Callable[
        [google_ads_field_service.SearchGoogleAdsFieldsRequest],
        Union[
            google_ads_field_service.SearchGoogleAdsFieldsResponse,
            Awaitable[google_ads_field_service.SearchGoogleAdsFieldsResponse],
        ],
    ]: ...
