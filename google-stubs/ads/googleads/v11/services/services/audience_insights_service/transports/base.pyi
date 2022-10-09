import abc
from typing import Awaitable, Callable, Optional, Sequence, Union

from _typeshed import Incomplete
from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials

from google.ads.googleads.v11.services.types import audience_insights_service

class AudienceInsightsServiceTransport(abc.ABC):
    AUTH_SCOPES: Incomplete
    DEFAULT_HOST: str
    def __init__(
        self,
        *,
        host: str = ...,
        credentials: ga_credentials.Credentials = ...,
        credentials_file: Optional[str] = ...,
        scopes: Optional[Sequence[str]] = ...,
        quota_project_id: Optional[str] = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...,
        always_use_jwt_access: Optional[bool] = ...,
        **kwargs
    ) -> None: ...
    def close(self) -> None: ...
    @property
    def generate_insights_finder_report(
        self,
    ) -> Callable[
        [audience_insights_service.GenerateInsightsFinderReportRequest],
        Union[
            audience_insights_service.GenerateInsightsFinderReportResponse,
            Awaitable[audience_insights_service.GenerateInsightsFinderReportResponse],
        ],
    ]: ...
    @property
    def list_audience_insights_attributes(
        self,
    ) -> Callable[
        [audience_insights_service.ListAudienceInsightsAttributesRequest],
        Union[
            audience_insights_service.ListAudienceInsightsAttributesResponse,
            Awaitable[audience_insights_service.ListAudienceInsightsAttributesResponse],
        ],
    ]: ...
    @property
    def generate_audience_composition_insights(
        self,
    ) -> Callable[
        [audience_insights_service.GenerateAudienceCompositionInsightsRequest],
        Union[
            audience_insights_service.GenerateAudienceCompositionInsightsResponse,
            Awaitable[
                audience_insights_service.GenerateAudienceCompositionInsightsResponse
            ],
        ],
    ]: ...
