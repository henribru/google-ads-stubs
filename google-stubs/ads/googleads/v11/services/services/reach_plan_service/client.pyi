from typing import Dict, Optional, Sequence, Tuple, Type, Union

from _typeshed import Incomplete
from google.api_core import (
    client_options as client_options_lib,
    gapic_v1,
    retry as retries,
)
from google.auth import credentials as ga_credentials

from google.ads.googleads.v11.services.types import reach_plan_service

from .transports.base import ReachPlanServiceTransport

class ReachPlanServiceClientMeta(type):
    def get_transport_class(
        cls, label: str = ...
    ) -> Type[ReachPlanServiceTransport]: ...

class ReachPlanServiceClient(metaclass=ReachPlanServiceClientMeta):
    DEFAULT_ENDPOINT: str
    DEFAULT_MTLS_ENDPOINT: Incomplete
    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs): ...
    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs): ...
    from_service_account_json: Incomplete
    @property
    def transport(self) -> ReachPlanServiceTransport: ...
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
        transport: Union[str, ReachPlanServiceTransport, None] = ...,
        client_options: Optional[client_options_lib.ClientOptions] = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...
    ) -> None: ...
    def list_plannable_locations(
        self,
        request: Union[reach_plan_service.ListPlannableLocationsRequest, dict] = ...,
        *,
        retry: Union[retries.Retry, gapic_v1.method._MethodDefault] = ...,
        timeout: float = ...,
        metadata: Sequence[Tuple[str, str]] = ...
    ) -> reach_plan_service.ListPlannableLocationsResponse: ...
    def list_plannable_products(
        self,
        request: Union[reach_plan_service.ListPlannableProductsRequest, dict] = ...,
        *,
        plannable_location_id: str = ...,
        retry: Union[retries.Retry, gapic_v1.method._MethodDefault] = ...,
        timeout: float = ...,
        metadata: Sequence[Tuple[str, str]] = ...
    ) -> reach_plan_service.ListPlannableProductsResponse: ...
    def generate_product_mix_ideas(
        self,
        request: Union[reach_plan_service.GenerateProductMixIdeasRequest, dict] = ...,
        *,
        customer_id: str = ...,
        plannable_location_id: str = ...,
        currency_code: str = ...,
        budget_micros: int = ...,
        retry: Union[retries.Retry, gapic_v1.method._MethodDefault] = ...,
        timeout: float = ...,
        metadata: Sequence[Tuple[str, str]] = ...
    ) -> reach_plan_service.GenerateProductMixIdeasResponse: ...
    def generate_reach_forecast(
        self,
        request: Union[reach_plan_service.GenerateReachForecastRequest, dict] = ...,
        *,
        customer_id: str = ...,
        campaign_duration: reach_plan_service.CampaignDuration = ...,
        planned_products: Sequence[reach_plan_service.PlannedProduct] = ...,
        retry: Union[retries.Retry, gapic_v1.method._MethodDefault] = ...,
        timeout: float = ...,
        metadata: Sequence[Tuple[str, str]] = ...
    ) -> reach_plan_service.GenerateReachForecastResponse: ...
