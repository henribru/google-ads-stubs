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
    conversion_action_service_pb2 as conversion_action_service_pb2,
)
from google.ads.google_ads.v3.services import (
    conversion_action_service_client_config as conversion_action_service_client_config,
)
from google.ads.google_ads.v3.services.transports import (
    conversion_action_service_grpc_transport as conversion_action_service_grpc_transport,
)
from google.ads.google_ads.v3.types import ConversionAction

class ConversionActionServiceClient:
    SERVICE_ADDRESS: ClassVar[str] = ...
    @classmethod
    def from_service_account_file(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> ConversionActionServiceClient: ...
    @classmethod
    def from_service_account_json(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> ConversionActionServiceClient: ...
    @classmethod
    def conversion_action_path(cls, customer: Any, conversion_action: Any) -> str: ...
    transport: Union[
        conversion_action_service_grpc_transport.ConversionActionServiceGrpcTransport,
        Callable[
            [Credentials, type],
            conversion_action_service_grpc_transport.ConversionActionServiceGrpcTransport,
        ],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                conversion_action_service_grpc_transport.ConversionActionServiceGrpcTransport,
                Callable[
                    [Credentials, type],
                    conversion_action_service_grpc_transport.ConversionActionServiceGrpcTransport,
                ],
            ]
        ] = ...,
        channel: Optional[grpc.Channel] = ...,
        credentials: Optional[Credentials] = ...,
        client_config: Optional[Dict[str, Any]] = ...,
        client_info: Optional[ClientInfo] = ...,
    ) -> None: ...
    def get_conversion_action(
        self,
        resource_name: str,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> ConversionAction: ...
    def mutate_conversion_actions(
        self,
        customer_id: str,
        operations: List[
            Union[
                Dict[str, Any], conversion_action_service_pb2.ConversionActionOperation
            ]
        ],
        partial_failure: Optional[bool] = ...,
        validate_only: Optional[bool] = ...,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> conversion_action_service_pb2.MutateConversionActionsResponse: ...
