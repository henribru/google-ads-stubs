from typing import Any, Dict, Optional, Sequence, Tuple, Type, Union

from google.api_core import (
    client_options as client_options_lib,
    gapic_v1,
    retry as retries,
)
from google.auth import credentials as ga_credentials

from google.ads.googleads.v9.resources.types import paid_organic_search_term_view
from google.ads.googleads.v9.services.types import paid_organic_search_term_view_service

from .transports.base import PaidOrganicSearchTermViewServiceTransport

class PaidOrganicSearchTermViewServiceClientMeta(type):
    def get_transport_class(
        cls, label: str = ...
    ) -> Type[PaidOrganicSearchTermViewServiceTransport]: ...

class PaidOrganicSearchTermViewServiceClient(
    metaclass=PaidOrganicSearchTermViewServiceClientMeta
):
    DEFAULT_ENDPOINT: str
    DEFAULT_MTLS_ENDPOINT: Any
    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs): ...
    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs): ...
    from_service_account_json: Any
    @property
    def transport(self) -> PaidOrganicSearchTermViewServiceTransport: ...
    def __enter__(self): ...
    def __exit__(self, type, value, traceback) -> None: ...
    @staticmethod
    def paid_organic_search_term_view_path(
        customer_id: str, campaign_id: str, ad_group_id: str, base64_search_term: str
    ) -> str: ...
    @staticmethod
    def parse_paid_organic_search_term_view_path(path: str) -> Dict[str, str]: ...
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
        transport: Union[str, PaidOrganicSearchTermViewServiceTransport, None] = ...,
        client_options: Optional[client_options_lib.ClientOptions] = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...
    ) -> None: ...
    def get_paid_organic_search_term_view(
        self,
        request: Union[
            paid_organic_search_term_view_service.GetPaidOrganicSearchTermViewRequest,
            dict,
        ] = ...,
        *,
        resource_name: str = ...,
        retry: Union[retries.Retry, gapic_v1.method._MethodDefault] = ...,
        timeout: float = ...,
        metadata: Sequence[Tuple[str, str]] = ...
    ) -> paid_organic_search_term_view.PaidOrganicSearchTermView: ...
