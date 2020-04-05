import grpc  # type: ignore
from google.ads.google_ads.v1.services.transports.keyword_plan_service_grpc_transport import (
    KeywordPlanServiceGrpcTransport,
)
from google.auth.credentials import Credentials  # type: ignore
from google.api_core.gapic_v1.client_info import ClientInfo  # type: ignore
from google.api_core.retry import Retry  # type: ignore
from typing import Optional, Dict, Any, List, Sequence, Tuple, Union, Callable, ClassVar
from google.ads.google_ads.v1.proto.resources.keyword_plan_pb2 import KeywordPlan
from google.ads.google_ads.v1.proto.services.keyword_plan_service_pb2 import (
    KeywordPlanOperation,
    MutateKeywordPlansResponse,
    GenerateForecastMetricsResponse,
    GenerateHistoricalMetricsResponse,
)

class KeywordPlanServiceClient:
    SERVICE_ADDRESS: ClassVar[str] = ...
    @classmethod
    def from_service_account_file(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> KeywordPlanServiceClient: ...
    @classmethod
    def from_service_account_json(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> KeywordPlanServiceClient: ...
    @classmethod
    def keyword_plan_path(cls, customer: Any, keyword_plan: Any) -> str: ...
    transport: Union[
        KeywordPlanServiceGrpcTransport,
        Callable[[Credentials, type], KeywordPlanServiceGrpcTransport],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                KeywordPlanServiceGrpcTransport,
                Callable[[Credentials, type], KeywordPlanServiceGrpcTransport],
            ]
        ] = ...,
        channel: Optional[grpc.Channel] = ...,
        credentials: Optional[Credentials] = ...,
        client_config: Optional[Dict[str, Any]] = ...,
        client_info: Optional[ClientInfo] = ...,
    ) -> None: ...
    def get_keyword_plan(
        self,
        resource_name: str,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> KeywordPlan: ...
    def mutate_keyword_plans(
        self,
        customer_id: str,
        operations: List[Union[Dict[str, Any], KeywordPlanOperation]],
        partial_failure: Optional[bool] = ...,
        validate_only: Optional[bool] = ...,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> MutateKeywordPlansResponse: ...
    def generate_forecast_metrics(
        self,
        keyword_plan: str,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> GenerateForecastMetricsResponse: ...
    def generate_historical_metrics(
        self,
        keyword_plan: str,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> GenerateHistoricalMetricsResponse: ...
