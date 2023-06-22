from typing import Dict, MutableSequence, Optional, Sequence, Tuple, Type, Union

from _typeshed import Incomplete
from google.api_core import (
    client_options as client_options_lib,
    gapic_v1,
    retry as retries,
)
from google.auth import credentials as ga_credentials

from google.ads.googleads.v14.services.types import (
    keyword_plan_ad_group_keyword_service,
)

from .transports.base import KeywordPlanAdGroupKeywordServiceTransport

class KeywordPlanAdGroupKeywordServiceClientMeta(type):
    def get_transport_class(
        cls, label: Optional[str] = ...
    ) -> Type[KeywordPlanAdGroupKeywordServiceTransport]: ...

class KeywordPlanAdGroupKeywordServiceClient(
    metaclass=KeywordPlanAdGroupKeywordServiceClientMeta
):
    DEFAULT_ENDPOINT: str
    DEFAULT_MTLS_ENDPOINT: Incomplete
    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs): ...
    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs): ...
    from_service_account_json = from_service_account_file
    @property
    def transport(self) -> KeywordPlanAdGroupKeywordServiceTransport: ...
    def __enter__(self) -> KeywordPlanAdGroupKeywordServiceClient: ...
    def __exit__(self, type, value, traceback) -> None: ...
    @staticmethod
    def keyword_plan_ad_group_path(
        customer_id: str, keyword_plan_ad_group_id: str
    ) -> str: ...
    @staticmethod
    def parse_keyword_plan_ad_group_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def keyword_plan_ad_group_keyword_path(
        customer_id: str, keyword_plan_ad_group_keyword_id: str
    ) -> str: ...
    @staticmethod
    def parse_keyword_plan_ad_group_keyword_path(path: str) -> Dict[str, str]: ...
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
        transport: Optional[
            Union[str, KeywordPlanAdGroupKeywordServiceTransport]
        ] = ...,
        client_options: Optional[Union[client_options_lib.ClientOptions, dict]] = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...
    ) -> None: ...
    def mutate_keyword_plan_ad_group_keywords(
        self,
        request: Optional[
            Union[
                keyword_plan_ad_group_keyword_service.MutateKeywordPlanAdGroupKeywordsRequest,
                dict,
            ]
        ] = ...,
        *,
        customer_id: Optional[str] = ...,
        operations: Optional[
            MutableSequence[
                keyword_plan_ad_group_keyword_service.KeywordPlanAdGroupKeywordOperation
            ]
        ] = ...,
        retry: Union[retries.Retry, gapic_v1.method._MethodDefault] = ...,
        timeout: Union[float, object] = ...,
        metadata: Sequence[Tuple[str, str]] = ...
    ) -> (
        keyword_plan_ad_group_keyword_service.MutateKeywordPlanAdGroupKeywordsResponse
    ): ...
