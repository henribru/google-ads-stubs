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

from google.ads.google_ads.v3.proto.services import (
    keyword_plan_service_pb2 as keyword_plan_service_pb2,
)
from google.ads.google_ads.v3.services import (
    keyword_plan_service_client_config as keyword_plan_service_client_config,
)
from google.ads.google_ads.v3.services.transports import (
    keyword_plan_service_grpc_transport as keyword_plan_service_grpc_transport,
)
from google.ads.google_ads.v3.types import (
    GenerateForecastMetricsResponse,
    GenerateHistoricalMetricsResponse,
    KeywordPlan,
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
        keyword_plan_service_grpc_transport.KeywordPlanServiceGrpcTransport,
        Callable[
            [Credentials, type],
            keyword_plan_service_grpc_transport.KeywordPlanServiceGrpcTransport,
        ],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                keyword_plan_service_grpc_transport.KeywordPlanServiceGrpcTransport,
                Callable[
                    [Credentials, type],
                    keyword_plan_service_grpc_transport.KeywordPlanServiceGrpcTransport,
                ],
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
        operations: List[
            Union[Dict[str, Any], keyword_plan_service_pb2.KeywordPlanOperation]
        ],
        partial_failure: Optional[bool] = ...,
        validate_only: Optional[bool] = ...,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> keyword_plan_service_pb2.MutateKeywordPlansResponse: ...
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
