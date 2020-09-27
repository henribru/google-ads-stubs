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
    label_service_pb2 as label_service_pb2,
)
from google.ads.google_ads.v3.services import (
    label_service_client_config as label_service_client_config,
)
from google.ads.google_ads.v3.services.transports import (
    label_service_grpc_transport as label_service_grpc_transport,
)
from google.ads.google_ads.v3.types import Label

class LabelServiceClient:
    SERVICE_ADDRESS: ClassVar[str] = ...
    @classmethod
    def from_service_account_file(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> LabelServiceClient: ...
    @classmethod
    def from_service_account_json(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> LabelServiceClient: ...
    @classmethod
    def label_path(cls, customer: Any, label: Any) -> str: ...
    transport: Union[
        label_service_grpc_transport.LabelServiceGrpcTransport,
        Callable[
            [Credentials, type], label_service_grpc_transport.LabelServiceGrpcTransport
        ],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                label_service_grpc_transport.LabelServiceGrpcTransport,
                Callable[
                    [Credentials, type],
                    label_service_grpc_transport.LabelServiceGrpcTransport,
                ],
            ]
        ] = ...,
        channel: Optional[grpc.Channel] = ...,
        credentials: Optional[Credentials] = ...,
        client_config: Optional[Dict[str, Any]] = ...,
        client_info: Optional[ClientInfo] = ...,
    ) -> None: ...
    def get_label(
        self,
        resource_name: str,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> Label: ...
    def mutate_labels(
        self,
        customer_id: str,
        operations: List[Union[Dict[str, Any], label_service_pb2.LabelOperation]],
        partial_failure: Optional[bool] = ...,
        validate_only: Optional[bool] = ...,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> label_service_pb2.MutateLabelsResponse: ...
