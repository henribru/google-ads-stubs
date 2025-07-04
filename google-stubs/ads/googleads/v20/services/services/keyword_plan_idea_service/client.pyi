import types
from typing import Callable, Dict, MutableSequence, Sequence, Tuple, Type

from _typeshed import Incomplete
from google.api_core import (
    client_options as client_options_lib,
    gapic_v1,
    retry as retries,
)
from google.auth import credentials as ga_credentials

from google.ads.googleads.v20.services.services.keyword_plan_idea_service import pagers
from google.ads.googleads.v20.services.types import keyword_plan_idea_service

from .transports.base import KeywordPlanIdeaServiceTransport

__all__ = ["KeywordPlanIdeaServiceClient"]

class KeywordPlanIdeaServiceClientMeta(type):
    def get_transport_class(
        cls, label: str | None = None
    ) -> type[KeywordPlanIdeaServiceTransport]: ...

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
    @staticmethod
    def common_billing_account_path(billing_account: str) -> str: ...
    @staticmethod
    def parse_common_billing_account_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def common_folder_path(folder: str) -> str: ...
    @staticmethod
    def parse_common_folder_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def common_organization_path(organization: str) -> str: ...
    @staticmethod
    def parse_common_organization_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def common_project_path(project: str) -> str: ...
    @staticmethod
    def parse_common_project_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def common_location_path(project: str, location: str) -> str: ...
    @staticmethod
    def parse_common_location_path(path: str) -> dict[str, str]: ...
    @classmethod
    def get_mtls_endpoint_and_cert_source(
        cls, client_options: client_options_lib.ClientOptions | None = None
    ): ...
    @property
    def api_endpoint(self): ...
    @property
    def universe_domain(self) -> str: ...
    def __init__(
        self,
        *,
        credentials: ga_credentials.Credentials | None = None,
        transport: str
        | KeywordPlanIdeaServiceTransport
        | Callable[..., KeywordPlanIdeaServiceTransport]
        | None = None,
        client_options: client_options_lib.ClientOptions | dict | None = None,
        client_info: gapic_v1.client_info.ClientInfo = ...,
    ) -> None: ...
    def generate_keyword_ideas(
        self,
        request: keyword_plan_idea_service.GenerateKeywordIdeasRequest
        | dict
        | None = None,
        *,
        retry: retries.Retry | gapic_v1.method._MethodDefault = ...,
        timeout: float | object = ...,
        metadata: Sequence[tuple[str, str | bytes]] = (),
    ) -> pagers.GenerateKeywordIdeasPager: ...
    def generate_keyword_historical_metrics(
        self,
        request: keyword_plan_idea_service.GenerateKeywordHistoricalMetricsRequest
        | dict
        | None = None,
        *,
        retry: retries.Retry | gapic_v1.method._MethodDefault = ...,
        timeout: float | object = ...,
        metadata: Sequence[tuple[str, str | bytes]] = (),
    ) -> keyword_plan_idea_service.GenerateKeywordHistoricalMetricsResponse: ...
    def generate_ad_group_themes(
        self,
        request: keyword_plan_idea_service.GenerateAdGroupThemesRequest
        | dict
        | None = None,
        *,
        customer_id: str | None = None,
        keywords: MutableSequence[str] | None = None,
        ad_groups: MutableSequence[str] | None = None,
        retry: retries.Retry | gapic_v1.method._MethodDefault = ...,
        timeout: float | object = ...,
        metadata: Sequence[tuple[str, str | bytes]] = (),
    ) -> keyword_plan_idea_service.GenerateAdGroupThemesResponse: ...
    def generate_keyword_forecast_metrics(
        self,
        request: keyword_plan_idea_service.GenerateKeywordForecastMetricsRequest
        | dict
        | None = None,
        *,
        campaign: keyword_plan_idea_service.CampaignToForecast | None = None,
        retry: retries.Retry | gapic_v1.method._MethodDefault = ...,
        timeout: float | object = ...,
        metadata: Sequence[tuple[str, str | bytes]] = (),
    ) -> keyword_plan_idea_service.GenerateKeywordForecastMetricsResponse: ...
    def __enter__(self) -> KeywordPlanIdeaServiceClient: ...
    def __exit__(
        self,
        type: type[BaseException] | None,
        value: BaseException | None,
        traceback: types.TracebackType | None,
    ) -> None: ...
