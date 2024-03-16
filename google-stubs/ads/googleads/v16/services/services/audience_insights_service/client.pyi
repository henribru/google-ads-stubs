import types
from typing import Dict, MutableSequence, Sequence, Tuple, Type

from _typeshed import Incomplete
from google.api_core import (
    client_options as client_options_lib,
    gapic_v1,
    retry as retries,
)
from google.auth import credentials as ga_credentials

from google.ads.googleads.v16.enums.types import audience_insights_dimension
from google.ads.googleads.v16.services.types import audience_insights_service

from .transports.base import AudienceInsightsServiceTransport

__all__ = ["AudienceInsightsServiceClient"]

class AudienceInsightsServiceClientMeta(type):
    def get_transport_class(
        cls, label: str | None = None
    ) -> type[AudienceInsightsServiceTransport]: ...

class AudienceInsightsServiceClient(metaclass=AudienceInsightsServiceClientMeta):
    DEFAULT_ENDPOINT: str
    DEFAULT_MTLS_ENDPOINT: Incomplete
    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs): ...
    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs): ...
    from_service_account_json = from_service_account_file
    @property
    def transport(self) -> AudienceInsightsServiceTransport: ...
    def __enter__(self) -> AudienceInsightsServiceClient: ...
    def __exit__(
        self,
        type: type[BaseException] | None,
        value: BaseException | None,
        traceback: types.TracebackType | None,
    ) -> None: ...
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
    def __init__(
        self,
        *,
        credentials: ga_credentials.Credentials | None = None,
        transport: str | AudienceInsightsServiceTransport | None = None,
        client_options: client_options_lib.ClientOptions | dict | None = None,
        client_info: gapic_v1.client_info.ClientInfo = ...,
    ) -> None: ...
    def generate_insights_finder_report(
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
        retry: retries.Retry | gapic_v1.method._MethodDefault = ...,
        timeout: float | object = ...,
        metadata: Sequence[tuple[str, str]] = (),
    ) -> audience_insights_service.GenerateInsightsFinderReportResponse: ...
    def list_audience_insights_attributes(
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
        retry: retries.Retry | gapic_v1.method._MethodDefault = ...,
        timeout: float | object = ...,
        metadata: Sequence[tuple[str, str]] = (),
    ) -> audience_insights_service.ListAudienceInsightsAttributesResponse: ...
    def list_insights_eligible_dates(
        self,
        request: audience_insights_service.ListInsightsEligibleDatesRequest
        | dict
        | None = None,
        *,
        retry: retries.Retry | gapic_v1.method._MethodDefault = ...,
        timeout: float | object = ...,
        metadata: Sequence[tuple[str, str]] = (),
    ) -> audience_insights_service.ListInsightsEligibleDatesResponse: ...
    def generate_audience_composition_insights(
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
        retry: retries.Retry | gapic_v1.method._MethodDefault = ...,
        timeout: float | object = ...,
        metadata: Sequence[tuple[str, str]] = (),
    ) -> audience_insights_service.GenerateAudienceCompositionInsightsResponse: ...
    def generate_suggested_targeting_insights(
        self,
        request: audience_insights_service.GenerateSuggestedTargetingInsightsRequest
        | dict
        | None = None,
        *,
        customer_id: str | None = None,
        audience: audience_insights_service.InsightsAudience | None = None,
        retry: retries.Retry | gapic_v1.method._MethodDefault = ...,
        timeout: float | object = ...,
        metadata: Sequence[tuple[str, str]] = (),
    ) -> audience_insights_service.GenerateSuggestedTargetingInsightsResponse: ...
