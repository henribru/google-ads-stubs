from typing import Any, Dict, Optional, Sequence, Tuple, Type, Union

from google.api_core import (
    client_options as client_options_lib,
    gapic_v1,
    retry as retries,
)
from google.auth import credentials

from google.ads.googleads.v7.resources.types import google_ads_field
from google.ads.googleads.v7.services.services.google_ads_field_service import pagers
from google.ads.googleads.v7.services.types import google_ads_field_service

from .transports.base import GoogleAdsFieldServiceTransport

class GoogleAdsFieldServiceClientMeta(type):
    def get_transport_class(
        cls, label: str = ...
    ) -> Type[GoogleAdsFieldServiceTransport]: ...

class GoogleAdsFieldServiceClient(metaclass=GoogleAdsFieldServiceClientMeta):
    DEFAULT_ENDPOINT: str
    DEFAULT_MTLS_ENDPOINT: Any
    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs): ...
    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs): ...
    from_service_account_json: Any
    @property
    def transport(self) -> GoogleAdsFieldServiceTransport: ...
    @staticmethod
    def google_ads_field_path(google_ads_field: str) -> str: ...
    @staticmethod
    def parse_google_ads_field_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def common_billing_account_path(billing_account: str) -> str: ...
    @staticmethod
    def parse_common_billing_account_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def common_folder_path(folder: str) -> str: ...
    @staticmethod
    def parse_common_folder_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def common_organization_path(organization: str) -> str: ...
    @staticmethod
    def parse_common_organization_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def common_project_path(project: str) -> str: ...
    @staticmethod
    def parse_common_project_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def common_location_path(project: str, location: str) -> str: ...
    @staticmethod
    def parse_common_location_path(path: str) -> Dict[str, str]: ...
    def __init__(
        self,
        *,
        credentials: Optional[credentials.Credentials] = ...,
        transport: Union[str, GoogleAdsFieldServiceTransport, None] = ...,
        client_options: Optional[client_options_lib.ClientOptions] = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...
    ) -> None: ...
    def get_google_ads_field(
        self,
        request: google_ads_field_service.GetGoogleAdsFieldRequest = ...,
        *,
        resource_name: str = ...,
        retry: retries.Retry = ...,
        timeout: float = ...,
        metadata: Sequence[Tuple[str, str]] = ...
    ) -> google_ads_field.GoogleAdsField: ...
    def search_google_ads_fields(
        self,
        request: google_ads_field_service.SearchGoogleAdsFieldsRequest = ...,
        *,
        query: str = ...,
        retry: retries.Retry = ...,
        timeout: float = ...,
        metadata: Sequence[Tuple[str, str]] = ...
    ) -> pagers.SearchGoogleAdsFieldsPager: ...
