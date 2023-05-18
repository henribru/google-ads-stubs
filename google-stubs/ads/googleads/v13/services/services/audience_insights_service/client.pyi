from typing import Dict, MutableSequence, Optional, Sequence, Tuple, Type, Union

from _typeshed import Incomplete
from google.api_core import (
    client_options as client_options_lib,
    gapic_v1,
    retry as retries,
)
from google.auth import credentials as ga_credentials

from google.ads.googleads.v13.enums.types import audience_insights_dimension
from google.ads.googleads.v13.services.types import audience_insights_service

from .transports.base import AudienceInsightsServiceTransport

class AudienceInsightsServiceClientMeta(type):
    def get_transport_class(
        cls, label: Optional[str] = ...
    ) -> Type[AudienceInsightsServiceTransport]: ...

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
        transport: Optional[Union[str, AudienceInsightsServiceTransport]] = ...,
        client_options: Optional[Union[client_options_lib.ClientOptions, dict]] = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...
    ) -> None: ...
    def generate_insights_finder_report(
        self,
        request: Optional[
            Union[audience_insights_service.GenerateInsightsFinderReportRequest, dict]
        ] = ...,
        *,
        customer_id: Optional[str] = ...,
        baseline_audience: Optional[
            audience_insights_service.BasicInsightsAudience
        ] = ...,
        specific_audience: Optional[
            audience_insights_service.BasicInsightsAudience
        ] = ...,
        retry: Union[retries.Retry, gapic_v1.method._MethodDefault] = ...,
        timeout: Union[float, object] = ...,
        metadata: Sequence[Tuple[str, str]] = ...
    ) -> audience_insights_service.GenerateInsightsFinderReportResponse: ...
    def list_audience_insights_attributes(
        self,
        request: Optional[
            Union[audience_insights_service.ListAudienceInsightsAttributesRequest, dict]
        ] = ...,
        *,
        customer_id: Optional[str] = ...,
        dimensions: Optional[
            MutableSequence[
                audience_insights_dimension.AudienceInsightsDimensionEnum.AudienceInsightsDimension
            ]
        ] = ...,
        query_text: Optional[str] = ...,
        retry: Union[retries.Retry, gapic_v1.method._MethodDefault] = ...,
        timeout: Union[float, object] = ...,
        metadata: Sequence[Tuple[str, str]] = ...
    ) -> audience_insights_service.ListAudienceInsightsAttributesResponse: ...
    def list_insights_eligible_dates(
        self,
        request: Optional[
            Union[audience_insights_service.ListInsightsEligibleDatesRequest, dict]
        ] = ...,
        *,
        retry: Union[retries.Retry, gapic_v1.method._MethodDefault] = ...,
        timeout: Union[float, object] = ...,
        metadata: Sequence[Tuple[str, str]] = ...
    ) -> audience_insights_service.ListInsightsEligibleDatesResponse: ...
    def generate_audience_composition_insights(
        self,
        request: Optional[
            Union[
                audience_insights_service.GenerateAudienceCompositionInsightsRequest,
                dict,
            ]
        ] = ...,
        *,
        customer_id: Optional[str] = ...,
        audience: Optional[audience_insights_service.InsightsAudience] = ...,
        dimensions: Optional[
            MutableSequence[
                audience_insights_dimension.AudienceInsightsDimensionEnum.AudienceInsightsDimension
            ]
        ] = ...,
        retry: Union[retries.Retry, gapic_v1.method._MethodDefault] = ...,
        timeout: Union[float, object] = ...,
        metadata: Sequence[Tuple[str, str]] = ...
    ) -> audience_insights_service.GenerateAudienceCompositionInsightsResponse: ...
