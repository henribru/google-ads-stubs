from google.ads.google_ads.v3.proto.services import (
    reach_plan_service_pb2 as reach_plan_service_pb2,
)
from google.ads.google_ads.v3.services import (
    reach_plan_service_client_config as reach_plan_service_client_config,
)
from google.ads.google_ads.v3.services.transports import (
    reach_plan_service_grpc_transport as reach_plan_service_grpc_transport,
)
from google.oauth2 import service_account as service_account  # type: ignore
import grpc  # type: ignore
from google.ads.google_ads.v3.services.transports.reach_plan_service_grpc_transport import (
    ReachPlanServiceGrpcTransport,
)
from google.auth.credentials import Credentials  # type: ignore
from google.api_core.gapic_v1.client_info import ClientInfo  # type: ignore
from google.api_core.retry import Retry  # type: ignore
from typing import (
    Optional,
    Dict,
    Any,
    List,
    Sequence,
    Tuple,
    Union,
    Callable,
    ClassVar,
    Text,
)
from google.ads.google_ads.v3.types import (
    ListPlannableLocationsResponse,
    ListPlannableProductsResponse,
    StringValue,
    Preferences,
    Int64Value,
    Int32Value,
    GenerateProductMixIdeasResponse,
    CampaignDuration,
    Targeting,
    PlannedProduct,
    GenerateReachForecastResponse,
)
from typing_extensions import TypedDict

class StringValueDict(TypedDict):
    value: Text

class Int64ValueDict(TypedDict):
    value: int

class Int32ValueDict(TypedDict):
    value: int

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
        ReachPlanServiceGrpcTransport,
        Callable[[Credentials, type], ReachPlanServiceGrpcTransport],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                ReachPlanServiceGrpcTransport,
                Callable[[Credentials, type], ReachPlanServiceGrpcTransport],
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
        plannable_location_id: Union[StringValueDict, StringValue],
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> ListPlannableProductsResponse: ...
    def generate_product_mix_ideas(
        self,
        customer_id: str,
        plannable_location_id: Union[StringValueDict, StringValue],
        currency_code: Union[StringValueDict, StringValue],
        budget_micros: Union[Int64ValueDict, Int64Value],
        preferences: Union[Dict[str, Any], Preferences],
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> GenerateProductMixIdeasResponse: ...
    def generate_reach_forecast(
        self,
        customer_id: str,
        currency_code: Union[StringValueDict, StringValue],
        campaign_duration: Union[Dict[str, Any], CampaignDuration],
        cookie_frequency_cap: Union[Int32ValueDict, Int32Value],
        min_effective_frequency: Union[Int32ValueDict, Int32Value],
        targeting: Union[Dict[str, Any], Targeting],
        planned_products: List[Union[Dict[str, Any], PlannedProduct]],
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> GenerateReachForecastResponse: ...
