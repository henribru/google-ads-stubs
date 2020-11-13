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

from google.ads.google_ads.v6.proto.services import (
    reach_plan_service_pb2 as reach_plan_service_pb2,
)
from google.ads.google_ads.v6.services import (
    reach_plan_service_client_config as reach_plan_service_client_config,
)
from google.ads.google_ads.v6.services.transports import (
    reach_plan_service_grpc_transport as reach_plan_service_grpc_transport,
)
from google.ads.google_ads.v6.types import (
    CampaignDuration,
    FrequencyCap,
    GenerateProductMixIdeasResponse,
    GenerateReachForecastResponse,
    ListPlannableLocationsResponse,
    ListPlannableProductsResponse,
    PlannedProduct,
    Preferences,
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
        client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    ) -> None: ...
    def list_plannable_locations(
        self,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> ListPlannableLocationsResponse: ...
    def list_plannable_products(
        self,
        plannable_location_id: str,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> ListPlannableProductsResponse: ...
    def generate_product_mix_ideas(
        self,
        customer_id: str,
        plannable_location_id: str,
        currency_code: str,
        budget_micros: int,
        preferences: Optional[Union[Dict[str, Any], Preferences]] = ...,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> GenerateProductMixIdeasResponse: ...
    def generate_reach_forecast(
        self,
        customer_id: str,
        campaign_duration: Union[Dict[str, Any], CampaignDuration],
        planned_products: List[Union[Dict[str, Any], PlannedProduct]],
        currency_code: str = ...,
        cookie_frequency_cap: int = ...,
        cookie_frequency_cap_setting: Optional[
            Union[Dict[str, Any], FrequencyCap]
        ] = ...,
        min_effective_frequency: int = ...,
        targeting: Optional[Union[Dict[str, Any], Targeting]] = ...,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> GenerateReachForecastResponse: ...
