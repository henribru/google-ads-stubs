from typing import Any, Callable, ClassVar, Dict, List, Optional, Sequence, Tuple, Union

import grpc  # type: ignore
from google.api_core.gapic_v1.client_info import ClientInfo  # type: ignore
from google.api_core.retry import Retry  # type: ignore
from google.auth.credentials import Credentials  # type: ignore
from google.oauth2 import service_account as service_account  # type: ignore

from google.ads.google_ads.v3.proto.resources.label_pb2 import Label
from google.ads.google_ads.v3.proto.services import (
    label_service_pb2 as label_service_pb2,
)
from google.ads.google_ads.v3.proto.services.label_service_pb2 import (
    LabelOperation,
    MutateLabelsResponse,
)
from google.ads.google_ads.v3.services import (
    label_service_client_config as label_service_client_config,
)
from google.ads.google_ads.v3.services.transports import (
    label_service_grpc_transport as label_service_grpc_transport,
)
from google.ads.google_ads.v3.services.transports.label_service_grpc_transport import (
    LabelServiceGrpcTransport,
)

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
        LabelServiceGrpcTransport,
        Callable[[Credentials, type], LabelServiceGrpcTransport],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                LabelServiceGrpcTransport,
                Callable[[Credentials, type], LabelServiceGrpcTransport],
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
        operations: List[Union[Dict[str, Any], LabelOperation]],
        partial_failure: Optional[bool] = ...,
        validate_only: Optional[bool] = ...,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> MutateLabelsResponse: ...
