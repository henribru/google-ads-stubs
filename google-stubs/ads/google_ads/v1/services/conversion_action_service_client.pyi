import grpc  # type: ignore
from google.ads.google_ads.v1.services.transports.conversion_action_service_grpc_transport import (
    ConversionActionServiceGrpcTransport,
)
from google.auth.credentials import Credentials  # type: ignore
from google.api_core.gapic_v1.client_info import ClientInfo  # type: ignore
from google.api_core.retry import Retry  # type: ignore
from typing import Optional, Dict, Any, List, Sequence, Tuple, Union, Callable, ClassVar
from google.ads.google_ads.v1.proto.resources.conversion_action_pb2 import (
    ConversionAction,
)
from google.ads.google_ads.v1.proto.services.conversion_action_service_pb2 import (
    ConversionActionOperation,
    MutateConversionActionsResponse,
)

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
        ConversionActionServiceGrpcTransport,
        Callable[[Credentials, type], ConversionActionServiceGrpcTransport],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                ConversionActionServiceGrpcTransport,
                Callable[[Credentials, type], ConversionActionServiceGrpcTransport],
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
        operations: List[Union[Dict[str, Any], ConversionActionOperation]],
        partial_failure: Optional[bool] = ...,
        validate_only: Optional[bool] = ...,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> MutateConversionActionsResponse: ...
