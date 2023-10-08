from typing import Dict, Optional, Sequence, Tuple, Type, Union

from _typeshed import Incomplete
from google.api_core import (
    client_options as client_options_lib,
    gapic_v1,
    retry as retries,
)
from google.auth import credentials as ga_credentials

from google.ads.googleads.v14.services.services.keyword_plan_idea_service import pagers
from google.ads.googleads.v14.services.types import keyword_plan_idea_service

from .transports.base import KeywordPlanIdeaServiceTransport

class KeywordPlanIdeaServiceClientMeta(type):
    def get_transport_class(
        cls, label: Optional[str] = ...
    ) -> Type[KeywordPlanIdeaServiceTransport]: ...

class KeywordPlanIdeaServiceClient(metaclass=KeywordPlanIdeaServiceClientMeta):
    DEFAULT_ENDPOINT: str
    DEFAULT_MTLS_ENDPOINT: Incomplete
    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs): ...
    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs): ...
    from_service_account_json = from_service_account_file
    @property
    def transport(self) -> KeywordPlanIdeaServiceTransport: ...
    def __enter__(self) -> KeywordPlanIdeaServiceClient: ...
    def __exit__(self, type, value, traceback) -> None: ...
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
        transport: Optional[Union[str, KeywordPlanIdeaServiceTransport]] = ...,
        client_options: Optional[Union[client_options_lib.ClientOptions, dict]] = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...
    ) -> None: ...
    def generate_keyword_ideas(
        self,
        request: Optional[
            Union[keyword_plan_idea_service.GenerateKeywordIdeasRequest, dict]
        ] = ...,
        *,
        retry: Union[retries.Retry, gapic_v1.method._MethodDefault] = ...,
        timeout: Union[float, object] = ...,
        metadata: Sequence[Tuple[str, str]] = ...
    ) -> pagers.GenerateKeywordIdeasPager: ...
    def generate_keyword_historical_metrics(
        self,
        request: Optional[
            Union[
                keyword_plan_idea_service.GenerateKeywordHistoricalMetricsRequest, dict
            ]
        ] = ...,
        *,
        retry: Union[retries.Retry, gapic_v1.method._MethodDefault] = ...,
        timeout: Union[float, object] = ...,
        metadata: Sequence[Tuple[str, str]] = ...
    ) -> keyword_plan_idea_service.GenerateKeywordHistoricalMetricsResponse: ...
    def generate_ad_group_themes(
        self,
        request: Optional[
            Union[keyword_plan_idea_service.GenerateAdGroupThemesRequest, dict]
        ] = ...,
        *,
        retry: Union[retries.Retry, gapic_v1.method._MethodDefault] = ...,
        timeout: Union[float, object] = ...,
        metadata: Sequence[Tuple[str, str]] = ...
    ) -> keyword_plan_idea_service.GenerateAdGroupThemesResponse: ...
    def generate_keyword_forecast_metrics(
        self,
        request: Optional[
            Union[keyword_plan_idea_service.GenerateKeywordForecastMetricsRequest, dict]
        ] = ...,
        *,
        retry: Union[retries.Retry, gapic_v1.method._MethodDefault] = ...,
        timeout: Union[float, object] = ...,
        metadata: Sequence[Tuple[str, str]] = ...
    ) -> keyword_plan_idea_service.GenerateKeywordForecastMetricsResponse: ...