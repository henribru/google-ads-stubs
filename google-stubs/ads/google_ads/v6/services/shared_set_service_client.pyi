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

from google.ads.google_ads.v6.proto.services import (
    shared_set_service_pb2 as shared_set_service_pb2,
)
from google.ads.google_ads.v6.services import (
    shared_set_service_client_config as shared_set_service_client_config,
)
from google.ads.google_ads.v6.services.transports import (
    shared_set_service_grpc_transport as shared_set_service_grpc_transport,
)
from google.ads.google_ads.v6.types import ResponseContentTypeEnum, SharedSet

class SharedSetServiceClient:
    SERVICE_ADDRESS: ClassVar[str] = ...
    @classmethod
    def from_service_account_file(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> SharedSetServiceClient: ...
    @classmethod
    def from_service_account_json(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> SharedSetServiceClient: ...
    @classmethod
    def shared_set_path(cls, customer: Any, shared_set: Any) -> str: ...
    transport: Union[
        shared_set_service_grpc_transport.SharedSetServiceGrpcTransport,
        Callable[
            [Credentials, type],
            shared_set_service_grpc_transport.SharedSetServiceGrpcTransport,
        ],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                shared_set_service_grpc_transport.SharedSetServiceGrpcTransport,
                Callable[
                    [Credentials, type],
                    shared_set_service_grpc_transport.SharedSetServiceGrpcTransport,
                ],
            ]
        ] = ...,
        channel: Optional[grpc.Channel] = ...,
        credentials: Optional[Credentials] = ...,
        client_config: Optional[Dict[str, Any]] = ...,
        client_info: Optional[ClientInfo] = ...,
        client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    ) -> None: ...
    def get_shared_set(
        self,
        resource_name: str,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> SharedSet: ...
    def mutate_shared_sets(
        self,
        customer_id: str,
        operations: List[
            Union[Dict[str, Any], shared_set_service_pb2.SharedSetOperation]
        ],
        partial_failure: Optional[bool] = ...,
        validate_only: Optional[bool] = ...,
        response_content_type: Optional[
            ResponseContentTypeEnum.ResponseContentTypeValue
        ] = ...,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> shared_set_service_pb2.MutateSharedSetsResponse: ...
