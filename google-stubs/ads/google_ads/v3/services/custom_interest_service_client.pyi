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
    custom_interest_service_pb2 as custom_interest_service_pb2,
)
from google.ads.google_ads.v3.services import (
    custom_interest_service_client_config as custom_interest_service_client_config,
)
from google.ads.google_ads.v3.services.transports import (
    custom_interest_service_grpc_transport as custom_interest_service_grpc_transport,
)
from google.ads.google_ads.v3.types import CustomInterest

class CustomInterestServiceClient:
    SERVICE_ADDRESS: ClassVar[str] = ...
    @classmethod
    def from_service_account_file(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> CustomInterestServiceClient: ...
    @classmethod
    def from_service_account_json(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> CustomInterestServiceClient: ...
    @classmethod
    def custom_interest_path(cls, customer: Any, custom_interest: Any) -> str: ...
    transport: Union[
        custom_interest_service_grpc_transport.CustomInterestServiceGrpcTransport,
        Callable[
            [Credentials, type],
            custom_interest_service_grpc_transport.CustomInterestServiceGrpcTransport,
        ],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                custom_interest_service_grpc_transport.CustomInterestServiceGrpcTransport,
                Callable[
                    [Credentials, type],
                    custom_interest_service_grpc_transport.CustomInterestServiceGrpcTransport,
                ],
            ]
        ] = ...,
        channel: Optional[grpc.Channel] = ...,
        credentials: Optional[Credentials] = ...,
        client_config: Optional[Dict[str, Any]] = ...,
        client_info: Optional[ClientInfo] = ...,
    ) -> None: ...
    def get_custom_interest(
        self,
        resource_name: str,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> CustomInterest: ...
    def mutate_custom_interests(
        self,
        customer_id: str,
        operations: List[
            Union[Dict[str, Any], custom_interest_service_pb2.CustomInterestOperation]
        ],
        validate_only: Optional[bool] = ...,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> custom_interest_service_pb2.MutateCustomInterestsResponse: ...
