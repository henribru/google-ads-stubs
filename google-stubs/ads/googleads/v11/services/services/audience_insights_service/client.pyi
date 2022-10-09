from typing import Dict, Optional, Sequence, Tuple, Type, Union

from _typeshed import Incomplete
from google.api_core import (
    client_options as client_options_lib,
    gapic_v1,
    retry as retries,
)
from google.auth import credentials as ga_credentials

from google.ads.googleads.v11.enums.types import audience_insights_dimension
from google.ads.googleads.v11.services.types import audience_insights_service

from .transports.base import AudienceInsightsServiceTransport

class AudienceInsightsServiceClientMeta(type):
    def get_transport_class(
        cls, label: str = ...
    ) -> Type[AudienceInsightsServiceTransport]: ...

class AudienceInsightsServiceClient(metaclass=AudienceInsightsServiceClientMeta):
    DEFAULT_ENDPOINT: str
    DEFAULT_MTLS_ENDPOINT: Incomplete
    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs): ...
    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs): ...
    from_service_account_json: Incomplete
    @property
    def transport(self) -> AudienceInsightsServiceTransport: ...
    def __enter__(self): ...
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
        transport: Union[str, AudienceInsightsServiceTransport, None] = ...,
        client_options: Optional[client_options_lib.ClientOptions] = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...
    ) -> None: ...
    def generate_insights_finder_report(
        self,
        request: Union[
            audience_insights_service.GenerateInsightsFinderReportRequest, dict
        ] = ...,
        *,
        customer_id: str = ...,
        baseline_audience: audience_insights_service.BasicInsightsAudience = ...,
        specific_audience: audience_insights_service.BasicInsightsAudience = ...,
        retry: Union[retries.Retry, gapic_v1.method._MethodDefault] = ...,
        timeout: float = ...,
        metadata: Sequence[Tuple[str, str]] = ...
    ) -> audience_insights_service.GenerateInsightsFinderReportResponse: ...
    def list_audience_insights_attributes(
        self,
        request: Union[
            audience_insights_service.ListAudienceInsightsAttributesRequest, dict
        ] = ...,
        *,
        customer_id: str = ...,
        dimensions: Sequence[
            audience_insights_dimension.AudienceInsightsDimensionEnum.AudienceInsightsDimension
        ] = ...,
        query_text: str = ...,
        retry: Union[retries.Retry, gapic_v1.method._MethodDefault] = ...,
        timeout: float = ...,
        metadata: Sequence[Tuple[str, str]] = ...
    ) -> audience_insights_service.ListAudienceInsightsAttributesResponse: ...
    def generate_audience_composition_insights(
        self,
        request: Union[
            audience_insights_service.GenerateAudienceCompositionInsightsRequest, dict
        ] = ...,
        *,
        customer_id: str = ...,
        audience: audience_insights_service.InsightsAudience = ...,
        dimensions: Sequence[
            audience_insights_dimension.AudienceInsightsDimensionEnum.AudienceInsightsDimension
        ] = ...,
        retry: Union[retries.Retry, gapic_v1.method._MethodDefault] = ...,
        timeout: float = ...,
        metadata: Sequence[Tuple[str, str]] = ...
    ) -> audience_insights_service.GenerateAudienceCompositionInsightsResponse: ...
