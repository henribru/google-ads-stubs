import abc
from typing import Awaitable, Callable, Sequence

from _typeshed import Incomplete
from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials

from google.ads.googleads.v15.services.types import audience_insights_service

__all__ = ["AudienceInsightsServiceTransport"]

class AudienceInsightsServiceTransport(abc.ABC):
    AUTH_SCOPES: Incomplete
    DEFAULT_HOST: str
    def __init__(
        self,
        *,
        host: str = "googleads.googleapis.com",
        credentials: ga_credentials.Credentials | None = None,
        credentials_file: str | None = None,
        scopes: Sequence[str] | None = None,
        quota_project_id: str | None = None,
        client_info: gapic_v1.client_info.ClientInfo = ...,
        always_use_jwt_access: bool | None = False,
        **kwargs,
    ) -> None: ...
    def close(self) -> None: ...
    @property
    def generate_insights_finder_report(
        self,
    ) -> Callable[
        [audience_insights_service.GenerateInsightsFinderReportRequest],
        audience_insights_service.GenerateInsightsFinderReportResponse
        | Awaitable[audience_insights_service.GenerateInsightsFinderReportResponse],
    ]: ...
    @property
    def list_audience_insights_attributes(
        self,
    ) -> Callable[
        [audience_insights_service.ListAudienceInsightsAttributesRequest],
        audience_insights_service.ListAudienceInsightsAttributesResponse
        | Awaitable[audience_insights_service.ListAudienceInsightsAttributesResponse],
    ]: ...
    @property
    def list_insights_eligible_dates(
        self,
    ) -> Callable[
        [audience_insights_service.ListInsightsEligibleDatesRequest],
        audience_insights_service.ListInsightsEligibleDatesResponse
        | Awaitable[audience_insights_service.ListInsightsEligibleDatesResponse],
    ]: ...
    @property
    def generate_audience_composition_insights(
        self,
    ) -> Callable[
        [audience_insights_service.GenerateAudienceCompositionInsightsRequest],
        audience_insights_service.GenerateAudienceCompositionInsightsResponse
        | Awaitable[
            audience_insights_service.GenerateAudienceCompositionInsightsResponse
        ],
    ]: ...
    @property
    def generate_suggested_targeting_insights(
        self,
    ) -> Callable[
        [audience_insights_service.GenerateSuggestedTargetingInsightsRequest],
        audience_insights_service.GenerateSuggestedTargetingInsightsResponse
        | Awaitable[
            audience_insights_service.GenerateSuggestedTargetingInsightsResponse
        ],
    ]: ...
