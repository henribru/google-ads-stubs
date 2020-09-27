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

from google.ads.google_ads.v4.proto.services import (
    topic_constant_service_pb2 as topic_constant_service_pb2,
)
from google.ads.google_ads.v4.services import (
    topic_constant_service_client_config as topic_constant_service_client_config,
)
from google.ads.google_ads.v4.services.transports import (
    topic_constant_service_grpc_transport as topic_constant_service_grpc_transport,
)
from google.ads.google_ads.v4.types import TopicConstant

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
    def topic_constant_path(cls, topic_constant: Any) -> str: ...
    transport: Union[
        topic_constant_service_grpc_transport.TopicConstantServiceGrpcTransport,
        Callable[
            [Credentials, type],
            topic_constant_service_grpc_transport.TopicConstantServiceGrpcTransport,
        ],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                topic_constant_service_grpc_transport.TopicConstantServiceGrpcTransport,
                Callable[
                    [Credentials, type],
                    topic_constant_service_grpc_transport.TopicConstantServiceGrpcTransport,
                ],
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
