from typing import (
    Any,
    Callable,
    ClassVar,
    Dict,
    Iterable,
    List,
    Optional,
    Sequence,
    Tuple,
    Union,
)

import grpc  # type: ignore
from google.api_core.client_options import ClientOptions  # type: ignore
from google.api_core.gapic_v1.client_info import ClientInfo  # type: ignore
from google.api_core.retry import Retry  # type: ignore
from google.auth.credentials import Credentials  # type: ignore
from google.oauth2 import service_account as service_account  # type: ignore

from google.ads.google_ads.v4.proto.services import (
    reach_plan_service_pb2 as reach_plan_service_pb2,
)
from google.ads.google_ads.v4.services import (
    reach_plan_service_client_config as reach_plan_service_client_config,
)
from google.ads.google_ads.v4.services.transports import (
    reach_plan_service_grpc_transport as reach_plan_service_grpc_transport,
)
from google.ads.google_ads.v4.types import (
    CampaignDuration,
    FrequencyCap,
    GenerateProductMixIdeasResponse,
    GenerateReachForecastResponse,
    Int32Value,
    Int64Value,
    ListPlannableLocationsResponse,
    ListPlannableProductsResponse,
    PlannedProduct,
    Preferences,
    StringValue,
    Targeting,
)

class ReachPlanServiceClient:
    SERVICE_ADDRESS: ClassVar[str] = ...
    @classmethod
    def from_service_account_file(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> ReachPlanServiceClient: ...
    @classmethod
    def from_service_account_json(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> ReachPlanServiceClient: ...
    transport: Union[
        reach_plan_service_grpc_transport.ReachPlanServiceGrpcTransport,
        Callable[
            [Credentials, type],
            reach_plan_service_grpc_transport.ReachPlanServiceGrpcTransport,
        ],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                reach_plan_service_grpc_transport.ReachPlanServiceGrpcTransport,
                Callable[
                    [Credentials, type],
                    reach_plan_service_grpc_transport.ReachPlanServiceGrpcTransport,
                ],
            ]
        ] = ...,
        channel: Optional[grpc.Channel] = ...,
        credentials: Optional[Credentials] = ...,
        client_config: Optional[Dict[str, Any]] = ...,
        client_info: Optional[ClientInfo] = ...,
    ) -> None: ...
    def list_plannable_locations(
        self,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> ListPlannableLocationsResponse: ...
    def list_plannable_products(
        self,
        plannable_location_id: Union[Dict[str, Any], StringValue],
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> ListPlannableProductsResponse: ...
    def generate_product_mix_ideas(
        self,
        customer_id: str,
        plannable_location_id: Union[Dict[str, Any], StringValue],
        currency_code: Union[Dict[str, Any], StringValue],
        budget_micros: Union[Dict[str, Any], Int64Value],
        preferences: Optional[Union[Dict[str, Any], Preferences]],
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> GenerateProductMixIdeasResponse: ...
    def generate_reach_forecast(
        self,
        customer_id: str,
        currency_code: Optional[Union[Dict[str, Any], StringValue]],
        campaign_duration: Union[Dict[str, Any], CampaignDuration],
        cookie_frequency_cap: Optional[Union[Dict[str, Any], Int32Value]],
        cookie_frequency_cap_setting: Optional[Union[Dict[str, Any], FrequencyCap]],
        min_effective_frequency: Optional[Union[Dict[str, Any], Int32Value]],
        targeting: Optional[Union[Dict[str, Any], Targeting]],
        planned_products: List[Union[Dict[str, Any], PlannedProduct]],
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> GenerateReachForecastResponse: ...
