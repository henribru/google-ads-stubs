import grpc  # type: ignore
from google.ads.google_ads.v1.services.transports.bidding_strategy_service_grpc_transport import (
    BiddingStrategyServiceGrpcTransport,
)
from google.auth.credentials import Credentials  # type: ignore
from google.api_core.gapic_v1.client_info import ClientInfo  # type: ignore
from google.api_core.retry import Retry  # type: ignore
from typing import Optional, Dict, Any, List, Sequence, Tuple, Union, Callable, ClassVar
from google.ads.google_ads.v1.proto.resources.bidding_strategy_pb2 import (
    BiddingStrategy,
)
from google.ads.google_ads.v1.proto.services.bidding_strategy_service_pb2 import (
    BiddingStrategyOperation,
    MutateBiddingStrategiesResponse,
)

class BiddingStrategyServiceClient:
    SERVICE_ADDRESS: ClassVar[str] = ...
    @classmethod
    def from_service_account_file(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> BiddingStrategyServiceClient: ...
    @classmethod
    def from_service_account_json(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> BiddingStrategyServiceClient: ...
    @classmethod
    def bidding_strategy_path(cls, customer: Any, bidding_strategy: Any) -> str: ...
    transport: Union[
        BiddingStrategyServiceGrpcTransport,
        Callable[[Credentials, type], BiddingStrategyServiceGrpcTransport],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                BiddingStrategyServiceGrpcTransport,
                Callable[[Credentials, type], BiddingStrategyServiceGrpcTransport],
            ]
        ] = ...,
        channel: Optional[grpc.Channel] = ...,
        credentials: Optional[Credentials] = ...,
        client_config: Optional[Dict[str, Any]] = ...,
        client_info: Optional[ClientInfo] = ...,
    ) -> None: ...
    def get_bidding_strategy(
        self,
        resource_name: str,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> BiddingStrategy: ...
    def mutate_bidding_strategies(
        self,
        customer_id: str,
        operations: List[Union[Dict[str, Any], BiddingStrategyOperation]],
        partial_failure: Optional[bool] = ...,
        validate_only: Optional[bool] = ...,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> MutateBiddingStrategiesResponse: ...
