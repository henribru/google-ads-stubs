from typing import Dict, Optional, Sequence, Tuple, Type, Union

from _typeshed import Incomplete
from google.api_core import (
    client_options as client_options_lib,
    gapic_v1,
    retry as retries,
)
from google.auth import credentials as ga_credentials

from google.ads.googleads.v11.services.types import (
    third_party_app_analytics_link_service,
)

from .transports.base import ThirdPartyAppAnalyticsLinkServiceTransport

class ThirdPartyAppAnalyticsLinkServiceClientMeta(type):
    def get_transport_class(
        cls, label: str = ...
    ) -> Type[ThirdPartyAppAnalyticsLinkServiceTransport]: ...

class ThirdPartyAppAnalyticsLinkServiceClient(
    metaclass=ThirdPartyAppAnalyticsLinkServiceClientMeta
):
    DEFAULT_ENDPOINT: str
    DEFAULT_MTLS_ENDPOINT: Incomplete
    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs): ...
    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs): ...
    from_service_account_json: Incomplete
    @property
    def transport(self) -> ThirdPartyAppAnalyticsLinkServiceTransport: ...
    def __enter__(self): ...
    def __exit__(self, type, value, traceback) -> None: ...
    @staticmethod
    def third_party_app_analytics_link_path(
        customer_id: str, customer_link_id: str
    ) -> str: ...
    @staticmethod
    def parse_third_party_app_analytics_link_path(path: str) -> Dict[str, str]: ...
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
        credentials: Optional[ga_credentials.Credentials] = ...,
        transport: Union[str, ThirdPartyAppAnalyticsLinkServiceTransport, None] = ...,
        client_options: Optional[client_options_lib.ClientOptions] = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...
    ) -> None: ...
    def regenerate_shareable_link_id(
        self,
        request: Union[
            third_party_app_analytics_link_service.RegenerateShareableLinkIdRequest,
            dict,
        ] = ...,
        *,
        retry: Union[retries.Retry, gapic_v1.method._MethodDefault] = ...,
        timeout: float = ...,
        metadata: Sequence[Tuple[str, str]] = ...
    ) -> third_party_app_analytics_link_service.RegenerateShareableLinkIdResponse: ...
