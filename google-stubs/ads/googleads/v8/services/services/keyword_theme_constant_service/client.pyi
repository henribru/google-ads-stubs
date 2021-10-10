from typing import Any, Dict, Optional, Sequence, Tuple, Type, Union

from google.api_core import (
    client_options as client_options_lib,
    gapic_v1,
    retry as retries,
)
from google.auth import credentials as ga_credentials

from google.ads.googleads.v8.resources.types import keyword_theme_constant
from google.ads.googleads.v8.services.types import keyword_theme_constant_service

from .transports.base import KeywordThemeConstantServiceTransport

class KeywordThemeConstantServiceClientMeta(type):
    def get_transport_class(
        cls, label: str = ...
    ) -> Type[KeywordThemeConstantServiceTransport]: ...

class KeywordThemeConstantServiceClient(
    metaclass=KeywordThemeConstantServiceClientMeta
):
    DEFAULT_ENDPOINT: str
    DEFAULT_MTLS_ENDPOINT: Any
    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs): ...
    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs): ...
    from_service_account_json: Any
    @property
    def transport(self) -> KeywordThemeConstantServiceTransport: ...
    @staticmethod
    def keyword_theme_constant_path(
        express_category_id: str, express_sub_category_id: str
    ) -> str: ...
    @staticmethod
    def parse_keyword_theme_constant_path(path: str) -> Dict[str, str]: ...
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
        transport: Union[str, KeywordThemeConstantServiceTransport, None] = ...,
        client_options: Optional[client_options_lib.ClientOptions] = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...
    ) -> None: ...
    def get_keyword_theme_constant(
        self,
        request: keyword_theme_constant_service.GetKeywordThemeConstantRequest = ...,
        *,
        resource_name: str = ...,
        retry: retries.Retry = ...,
        timeout: float = ...,
        metadata: Sequence[Tuple[str, str]] = ...
    ) -> keyword_theme_constant.KeywordThemeConstant: ...
    def suggest_keyword_theme_constants(
        self,
        request: keyword_theme_constant_service.SuggestKeywordThemeConstantsRequest = ...,
        *,
        retry: retries.Retry = ...,
        timeout: float = ...,
        metadata: Sequence[Tuple[str, str]] = ...
    ) -> keyword_theme_constant_service.SuggestKeywordThemeConstantsResponse: ...
