from google.ads.google_ads.v3.proto.services import (
    recommendation_service_pb2 as recommendation_service_pb2,
)
from google.ads.google_ads.v3.services import (
    recommendation_service_client_config as recommendation_service_client_config,
)
from google.ads.google_ads.v3.services.transports import (
    recommendation_service_grpc_transport as recommendation_service_grpc_transport,
)
from google.oauth2 import service_account as service_account  # type: ignore
import grpc  # type: ignore
from google.ads.google_ads.v3.services.transports.recommendation_service_grpc_transport import (
    RecommendationServiceGrpcTransport,
)
from google.auth.credentials import Credentials  # type: ignore
from google.api_core.gapic_v1.client_info import ClientInfo  # type: ignore
from google.api_core.retry import Retry  # type: ignore
from typing import Optional, Dict, Any, List, Sequence, Tuple, Union, Callable, ClassVar
from google.ads.google_ads.v3.proto.resources.recommendation_pb2 import Recommendation
from google.ads.google_ads.v3.types import (
    ApplyRecommendationOperation,
    ApplyRecommendationResponse,
    DismissRecommendationRequest,
    DismissRecommendationResponse,
)

class RecommendationServiceClient:
    SERVICE_ADDRESS: ClassVar[str] = ...
    @classmethod
    def from_service_account_file(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> RecommendationServiceClient: ...
    @classmethod
    def from_service_account_json(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> RecommendationServiceClient: ...
    @classmethod
    def recommendation_path(cls, customer: Any, recommendation: Any) -> str: ...
    transport: Union[
        RecommendationServiceGrpcTransport,
        Callable[[Credentials, type], RecommendationServiceGrpcTransport],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                RecommendationServiceGrpcTransport,
                Callable[[Credentials, type], RecommendationServiceGrpcTransport],
            ]
        ] = ...,
        channel: Optional[grpc.Channel] = ...,
        credentials: Optional[Credentials] = ...,
        client_config: Optional[Dict[str, Any]] = ...,
        client_info: Optional[ClientInfo] = ...,
    ) -> None: ...
    def get_recommendation(
        self,
        resource_name: str,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> Recommendation: ...
    def apply_recommendation(
        self,
        customer_id: str,
        operations: List[Union[Dict[str, Any], ApplyRecommendationOperation]],
        partial_failure: Optional[bool] = ...,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> ApplyRecommendationResponse: ...
    def dismiss_recommendation(
        self,
        customer_id: str,
        operations: List[
            Union[
                Dict[str, Any],
                DismissRecommendationRequest.DismissRecommendationOperation,
            ]
        ],
        partial_failure: Optional[bool] = ...,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> DismissRecommendationResponse: ...
