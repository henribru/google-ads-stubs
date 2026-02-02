from .transports.base import KeywordPlanIdeaServiceTransport
from _typeshed import Incomplete
from google.ads.googleads.v22.services.services.keyword_plan_idea_service import pagers
from google.ads.googleads.v22.services.types import keyword_plan_idea_service
from google.api_core import gapic_v1, retry_async as retries
from google.api_core.client_options import ClientOptions
from google.auth import credentials as ga_credentials
from typing import Callable, MutableSequence, Sequence

__all__ = ['KeywordPlanIdeaServiceAsyncClient']

class KeywordPlanIdeaServiceAsyncClient:
    DEFAULT_ENDPOINT: Incomplete
    DEFAULT_MTLS_ENDPOINT: Incomplete
    common_billing_account_path: Incomplete
    parse_common_billing_account_path: Incomplete
    common_folder_path: Incomplete
    parse_common_folder_path: Incomplete
    common_organization_path: Incomplete
    parse_common_organization_path: Incomplete
    common_project_path: Incomplete
    parse_common_project_path: Incomplete
    common_location_path: Incomplete
    parse_common_location_path: Incomplete
    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs): ...
    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs): ...
    from_service_account_json = from_service_account_file
    @classmethod
    def get_mtls_endpoint_and_cert_source(cls, client_options: ClientOptions | None = None): ...
    @property
    def transport(self) -> KeywordPlanIdeaServiceTransport: ...
    @property
    def api_endpoint(self): ...
    @property
    def universe_domain(self) -> str: ...
    get_transport_class: Incomplete
    def __init__(self, *, credentials: ga_credentials.Credentials | None = None, transport: str | KeywordPlanIdeaServiceTransport | Callable[..., KeywordPlanIdeaServiceTransport] | None = 'grpc_asyncio', client_options: ClientOptions | None = None, client_info: gapic_v1.client_info.ClientInfo = ...) -> None: ...
    async def generate_keyword_ideas(self, request: keyword_plan_idea_service.GenerateKeywordIdeasRequest | dict | None = None, *, retry: retries.AsyncRetry | gapic_v1.method._MethodDefault = ..., timeout: float | object = ..., metadata: Sequence[tuple[str, str | bytes]] = ()) -> pagers.GenerateKeywordIdeasAsyncPager: ...
    async def generate_keyword_historical_metrics(self, request: keyword_plan_idea_service.GenerateKeywordHistoricalMetricsRequest | dict | None = None, *, retry: retries.AsyncRetry | gapic_v1.method._MethodDefault = ..., timeout: float | object = ..., metadata: Sequence[tuple[str, str | bytes]] = ()) -> keyword_plan_idea_service.GenerateKeywordHistoricalMetricsResponse: ...
    async def generate_ad_group_themes(self, request: keyword_plan_idea_service.GenerateAdGroupThemesRequest | dict | None = None, *, customer_id: str | None = None, keywords: MutableSequence[str] | None = None, ad_groups: MutableSequence[str] | None = None, retry: retries.AsyncRetry | gapic_v1.method._MethodDefault = ..., timeout: float | object = ..., metadata: Sequence[tuple[str, str | bytes]] = ()) -> keyword_plan_idea_service.GenerateAdGroupThemesResponse: ...
    async def generate_keyword_forecast_metrics(self, request: keyword_plan_idea_service.GenerateKeywordForecastMetricsRequest | dict | None = None, *, campaign: keyword_plan_idea_service.CampaignToForecast | None = None, retry: retries.AsyncRetry | gapic_v1.method._MethodDefault = ..., timeout: float | object = ..., metadata: Sequence[tuple[str, str | bytes]] = ()) -> keyword_plan_idea_service.GenerateKeywordForecastMetricsResponse: ...
    async def __aenter__(self) -> KeywordPlanIdeaServiceAsyncClient: ...
    async def __aexit__(self, exc_type, exc, tb) -> None: ...
