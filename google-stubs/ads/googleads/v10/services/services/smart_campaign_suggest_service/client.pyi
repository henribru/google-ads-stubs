from typing import Dict, Optional, Sequence, Tuple, Type, Union

from _typeshed import Incomplete
from google.api_core import (
    client_options as client_options_lib,
    gapic_v1,
    retry as retries,
)
from google.auth import credentials as ga_credentials

from google.ads.googleads.v10.services.types import smart_campaign_suggest_service

from .transports.base import SmartCampaignSuggestServiceTransport

class SmartCampaignSuggestServiceClientMeta(type):
    def get_transport_class(
        cls, label: str = ...
    ) -> Type[SmartCampaignSuggestServiceTransport]: ...

class SmartCampaignSuggestServiceClient(
    metaclass=SmartCampaignSuggestServiceClientMeta
):
    DEFAULT_ENDPOINT: str
    DEFAULT_MTLS_ENDPOINT: Incomplete
    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs): ...
    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs): ...
    from_service_account_json: Incomplete
    @property
    def transport(self) -> SmartCampaignSuggestServiceTransport: ...
    def __enter__(self): ...
    def __exit__(self, type, value, traceback) -> None: ...
    @staticmethod
    def campaign_path(customer_id: str, campaign_id: str) -> str: ...
    @staticmethod
    def parse_campaign_path(path: str) -> Dict[str, str]: ...
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
        transport: Union[str, SmartCampaignSuggestServiceTransport, None] = ...,
        client_options: Optional[client_options_lib.ClientOptions] = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...
    ) -> None: ...
    def suggest_smart_campaign_budget_options(
        self,
        request: Union[
            smart_campaign_suggest_service.SuggestSmartCampaignBudgetOptionsRequest,
            dict,
        ] = ...,
        *,
        retry: Union[retries.Retry, gapic_v1.method._MethodDefault] = ...,
        timeout: float = ...,
        metadata: Sequence[Tuple[str, str]] = ...
    ) -> smart_campaign_suggest_service.SuggestSmartCampaignBudgetOptionsResponse: ...
    def suggest_smart_campaign_ad(
        self,
        request: Union[
            smart_campaign_suggest_service.SuggestSmartCampaignAdRequest, dict
        ] = ...,
        *,
        retry: Union[retries.Retry, gapic_v1.method._MethodDefault] = ...,
        timeout: float = ...,
        metadata: Sequence[Tuple[str, str]] = ...
    ) -> smart_campaign_suggest_service.SuggestSmartCampaignAdResponse: ...
    def suggest_keyword_themes(
        self,
        request: Union[
            smart_campaign_suggest_service.SuggestKeywordThemesRequest, dict
        ] = ...,
        *,
        retry: Union[retries.Retry, gapic_v1.method._MethodDefault] = ...,
        timeout: float = ...,
        metadata: Sequence[Tuple[str, str]] = ...
    ) -> smart_campaign_suggest_service.SuggestKeywordThemesResponse: ...
