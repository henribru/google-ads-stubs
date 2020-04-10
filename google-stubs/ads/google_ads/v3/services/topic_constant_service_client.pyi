from google.ads.google_ads.v3.proto.services import (
    topic_constant_service_pb2 as topic_constant_service_pb2,
)
from google.ads.google_ads.v3.services import (
    topic_constant_service_client_config as topic_constant_service_client_config,
)
from google.ads.google_ads.v3.services.transports import (
    topic_constant_service_grpc_transport as topic_constant_service_grpc_transport,
)
from google.oauth2 import service_account as service_account  # type: ignore
import grpc  # type: ignore
from google.ads.google_ads.v3.services.transports.topic_constant_service_grpc_transport import (
    TopicConstantServiceGrpcTransport,
)
from google.auth.credentials import Credentials  # type: ignore
from google.api_core.gapic_v1.client_info import ClientInfo  # type: ignore
from google.api_core.retry import Retry  # type: ignore
from typing import Optional, Dict, Any, List, Sequence, Tuple, Union, Callable, ClassVar
from google.ads.google_ads.v3.proto.resources.topic_constant_pb2 import TopicConstant

class TopicConstantServiceClient:
    SERVICE_ADDRESS: ClassVar[str] = ...
    @classmethod
    def from_service_account_file(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> TopicConstantServiceClient: ...
    @classmethod
    def from_service_account_json(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> TopicConstantServiceClient: ...
    @classmethod
    def topic_constant_path(cls, topic_constant: Any): ...
    transport: Union[
        TopicConstantServiceGrpcTransport,
        Callable[[Credentials, type], TopicConstantServiceGrpcTransport],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                TopicConstantServiceGrpcTransport,
                Callable[[Credentials, type], TopicConstantServiceGrpcTransport],
            ]
        ] = ...,
        channel: Optional[grpc.Channel] = ...,
        credentials: Optional[Credentials] = ...,
        client_config: Optional[Dict[str, Any]] = ...,
        client_info: Optional[ClientInfo] = ...,
    ) -> None: ...
    def get_topic_constant(
        self,
        resource_name: str,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> TopicConstant: ...
