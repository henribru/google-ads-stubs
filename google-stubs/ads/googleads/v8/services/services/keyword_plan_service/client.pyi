from typing import Any, Dict, Optional, Sequence, Tuple, Type, Union

from google.api_core import (
    client_options as client_options_lib,
    gapic_v1,
    retry as retries,
)
from google.auth import credentials as ga_credentials

from google.ads.googleads.v8.resources.types import keyword_plan
from google.ads.googleads.v8.services.types import keyword_plan_service

from .transports.base import KeywordPlanServiceTransport

class KeywordPlanServiceClientMeta(type):
    def get_transport_class(
        cls, label: str = ...
    ) -> Type[KeywordPlanServiceTransport]: ...

class KeywordPlanServiceClient(metaclass=KeywordPlanServiceClientMeta):
    DEFAULT_ENDPOINT: str
    DEFAULT_MTLS_ENDPOINT: Any
    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs): ...
    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs): ...
    from_service_account_json: Any
    @property
    def transport(self) -> KeywordPlanServiceTransport: ...
    @staticmethod
    def keyword_plan_path(customer_id: str, keyword_plan_id: str) -> str: ...
    @staticmethod
    def parse_keyword_plan_path(path: str) -> Dict[str, str]: ...
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
        transport: Union[str, KeywordPlanServiceTransport, None] = ...,
        client_options: Optional[client_options_lib.ClientOptions] = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...
    ) -> None: ...
    def get_keyword_plan(
        self,
        request: keyword_plan_service.GetKeywordPlanRequest = ...,
        *,
        resource_name: str = ...,
        retry: retries.Retry = ...,
        timeout: float = ...,
        metadata: Sequence[Tuple[str, str]] = ...
    ) -> keyword_plan.KeywordPlan: ...
    def mutate_keyword_plans(
        self,
        request: keyword_plan_service.MutateKeywordPlansRequest = ...,
        *,
        customer_id: str = ...,
        operations: Sequence[keyword_plan_service.KeywordPlanOperation] = ...,
        retry: retries.Retry = ...,
        timeout: float = ...,
        metadata: Sequence[Tuple[str, str]] = ...
    ) -> keyword_plan_service.MutateKeywordPlansResponse: ...
    def generate_forecast_curve(
        self,
        request: keyword_plan_service.GenerateForecastCurveRequest = ...,
        *,
        keyword_plan: str = ...,
        retry: retries.Retry = ...,
        timeout: float = ...,
        metadata: Sequence[Tuple[str, str]] = ...
    ) -> keyword_plan_service.GenerateForecastCurveResponse: ...
    def generate_forecast_time_series(
        self,
        request: keyword_plan_service.GenerateForecastTimeSeriesRequest = ...,
        *,
        keyword_plan: str = ...,
        retry: retries.Retry = ...,
        timeout: float = ...,
        metadata: Sequence[Tuple[str, str]] = ...
    ) -> keyword_plan_service.GenerateForecastTimeSeriesResponse: ...
    def generate_forecast_metrics(
        self,
        request: keyword_plan_service.GenerateForecastMetricsRequest = ...,
        *,
        keyword_plan: str = ...,
        retry: retries.Retry = ...,
        timeout: float = ...,
        metadata: Sequence[Tuple[str, str]] = ...
    ) -> keyword_plan_service.GenerateForecastMetricsResponse: ...
    def generate_historical_metrics(
        self,
        request: keyword_plan_service.GenerateHistoricalMetricsRequest = ...,
        *,
        keyword_plan: str = ...,
        retry: retries.Retry = ...,
        timeout: float = ...,
        metadata: Sequence[Tuple[str, str]] = ...
    ) -> keyword_plan_service.GenerateHistoricalMetricsResponse: ...
