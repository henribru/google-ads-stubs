from typing import Callable, MutableSequence, Sequence, Tuple

from _typeshed import Incomplete
from google.api_core import gapic_v1, retry_async as retries
from google.api_core.client_options import ClientOptions
from google.auth import credentials as ga_credentials

from google.ads.googleads.v17.common.types import criteria
from google.ads.googleads.v17.enums.types import audience_insights_dimension
from google.ads.googleads.v17.services.types import audience_insights_service

from .transports.base import AudienceInsightsServiceTransport

__all__ = ["AudienceInsightsServiceAsyncClient"]

class AudienceInsightsServiceAsyncClient:
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
    def get_mtls_endpoint_and_cert_source(
        cls, client_options: ClientOptions | None = None
    ): ...
    @property
    def transport(self) -> AudienceInsightsServiceTransport: ...
    @property
    def api_endpoint(self): ...
    @property
    def universe_domain(self) -> str: ...
    get_transport_class: Incomplete
    def __init__(
        self,
        *,
        credentials: ga_credentials.Credentials | None = None,
        transport: str
        | AudienceInsightsServiceTransport
        | Callable[..., AudienceInsightsServiceTransport]
        | None = "grpc_asyncio",
        client_options: ClientOptions | None = None,
        client_info: gapic_v1.client_info.ClientInfo = ...,
    ) -> None: ...
    async def generate_insights_finder_report(
        self,
        request: audience_insights_service.GenerateInsightsFinderReportRequest
        | dict
        | None = None,
        *,
        customer_id: str | None = None,
        baseline_audience: audience_insights_service.BasicInsightsAudience
        | None = None,
        specific_audience: audience_insights_service.BasicInsightsAudience
        | None = None,
        retry: retries.AsyncRetry | gapic_v1.method._MethodDefault = ...,
        timeout: float | object = ...,
        metadata: Sequence[tuple[str, str | bytes]] = (),
    ) -> audience_insights_service.GenerateInsightsFinderReportResponse: ...
    async def list_audience_insights_attributes(
        self,
        request: audience_insights_service.ListAudienceInsightsAttributesRequest
        | dict
        | None = None,
        *,
        customer_id: str | None = None,
        dimensions: MutableSequence[
            audience_insights_dimension.AudienceInsightsDimensionEnum.AudienceInsightsDimension
        ]
        | None = None,
        query_text: str | None = None,
        retry: retries.AsyncRetry | gapic_v1.method._MethodDefault = ...,
        timeout: float | object = ...,
        metadata: Sequence[tuple[str, str | bytes]] = (),
    ) -> audience_insights_service.ListAudienceInsightsAttributesResponse: ...
    async def list_insights_eligible_dates(
        self,
        request: audience_insights_service.ListInsightsEligibleDatesRequest
        | dict
        | None = None,
        *,
        retry: retries.AsyncRetry | gapic_v1.method._MethodDefault = ...,
        timeout: float | object = ...,
        metadata: Sequence[tuple[str, str | bytes]] = (),
    ) -> audience_insights_service.ListInsightsEligibleDatesResponse: ...
    async def generate_audience_composition_insights(
        self,
        request: audience_insights_service.GenerateAudienceCompositionInsightsRequest
        | dict
        | None = None,
        *,
        customer_id: str | None = None,
        audience: audience_insights_service.InsightsAudience | None = None,
        dimensions: MutableSequence[
            audience_insights_dimension.AudienceInsightsDimensionEnum.AudienceInsightsDimension
        ]
        | None = None,
        retry: retries.AsyncRetry | gapic_v1.method._MethodDefault = ...,
        timeout: float | object = ...,
        metadata: Sequence[tuple[str, str | bytes]] = (),
    ) -> audience_insights_service.GenerateAudienceCompositionInsightsResponse: ...
    async def generate_suggested_targeting_insights(
        self,
        request: audience_insights_service.GenerateSuggestedTargetingInsightsRequest
        | dict
        | None = None,
        *,
        customer_id: str | None = None,
        audience: audience_insights_service.InsightsAudience | None = None,
        retry: retries.AsyncRetry | gapic_v1.method._MethodDefault = ...,
        timeout: float | object = ...,
        metadata: Sequence[tuple[str, str | bytes]] = (),
    ) -> audience_insights_service.GenerateSuggestedTargetingInsightsResponse: ...
    async def generate_audience_overlap_insights(
        self,
        request: audience_insights_service.GenerateAudienceOverlapInsightsRequest
        | dict
        | None = None,
        *,
        customer_id: str | None = None,
        country_location: criteria.LocationInfo | None = None,
        primary_attribute: audience_insights_service.AudienceInsightsAttribute
        | None = None,
        dimensions: MutableSequence[
            audience_insights_dimension.AudienceInsightsDimensionEnum.AudienceInsightsDimension
        ]
        | None = None,
        retry: retries.AsyncRetry | gapic_v1.method._MethodDefault = ...,
        timeout: float | object = ...,
        metadata: Sequence[tuple[str, str | bytes]] = (),
    ) -> audience_insights_service.GenerateAudienceOverlapInsightsResponse: ...
    async def __aenter__(self) -> AudienceInsightsServiceAsyncClient: ...
    async def __aexit__(self, exc_type, exc, tb) -> None: ...
