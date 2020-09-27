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
    bidding_strategy_service_pb2 as bidding_strategy_service_pb2,
)
from google.ads.google_ads.v3.services import (
    bidding_strategy_service_client_config as bidding_strategy_service_client_config,
)
from google.ads.google_ads.v3.services.transports import (
    bidding_strategy_service_grpc_transport as bidding_strategy_service_grpc_transport,
)
from google.ads.google_ads.v3.types import BiddingStrategy

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
        bidding_strategy_service_grpc_transport.BiddingStrategyServiceGrpcTransport,
        Callable[
            [Credentials, type],
            bidding_strategy_service_grpc_transport.BiddingStrategyServiceGrpcTransport,
        ],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                bidding_strategy_service_grpc_transport.BiddingStrategyServiceGrpcTransport,
                Callable[
                    [Credentials, type],
                    bidding_strategy_service_grpc_transport.BiddingStrategyServiceGrpcTransport,
                ],
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
        operations: List[
            Union[Dict[str, Any], bidding_strategy_service_pb2.BiddingStrategyOperation]
        ],
        partial_failure: Optional[bool] = ...,
        validate_only: Optional[bool] = ...,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> bidding_strategy_service_pb2.MutateBiddingStrategiesResponse: ...
