from typing import Dict, Optional, Sequence, Tuple, Type, Union

from _typeshed import Incomplete
from google.api_core import (
    client_options as client_options_lib,
    gapic_v1,
    retry as retries,
)
from google.auth import credentials as ga_credentials

from google.ads.googleads.v12.services.types import (
    keyword_plan_campaign_keyword_service,
)

from .transports.base import KeywordPlanCampaignKeywordServiceTransport

class KeywordPlanCampaignKeywordServiceClientMeta(type):
    def get_transport_class(
        cls, label: str = ...
    ) -> Type[KeywordPlanCampaignKeywordServiceTransport]: ...

class KeywordPlanCampaignKeywordServiceClient(
    metaclass=KeywordPlanCampaignKeywordServiceClientMeta
):
    DEFAULT_ENDPOINT: str
    DEFAULT_MTLS_ENDPOINT: Incomplete
    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs): ...
    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs): ...
    from_service_account_json = from_service_account_file
    @property
    def transport(self) -> KeywordPlanCampaignKeywordServiceTransport: ...
    def __enter__(self): ...
    def __exit__(self, type, value, traceback) -> None: ...
    @staticmethod
    def keyword_plan_campaign_path(
        customer_id: str, keyword_plan_campaign_id: str
    ) -> str: ...
    @staticmethod
    def parse_keyword_plan_campaign_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def keyword_plan_campaign_keyword_path(
        customer_id: str, keyword_plan_campaign_keyword_id: str
    ) -> str: ...
    @staticmethod
    def parse_keyword_plan_campaign_keyword_path(path: str) -> Dict[str, str]: ...
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
        transport: Union[str, KeywordPlanCampaignKeywordServiceTransport, None] = ...,
        client_options: Optional[client_options_lib.ClientOptions] = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...
    ) -> None: ...
    def mutate_keyword_plan_campaign_keywords(
        self,
        request: Union[
            keyword_plan_campaign_keyword_service.MutateKeywordPlanCampaignKeywordsRequest,
            dict,
        ] = ...,
        *,
        customer_id: str = ...,
        operations: Sequence[
            keyword_plan_campaign_keyword_service.KeywordPlanCampaignKeywordOperation
        ] = ...,
        retry: Union[retries.Retry, gapic_v1.method._MethodDefault] = ...,
        timeout: float = ...,
        metadata: Sequence[Tuple[str, str]] = ...
    ) -> (
        keyword_plan_campaign_keyword_service.MutateKeywordPlanCampaignKeywordsResponse
    ): ...
