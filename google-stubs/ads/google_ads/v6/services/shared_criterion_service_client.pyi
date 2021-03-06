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

import grpc
from google.api_core.client_options import ClientOptions  # type: ignore
from google.api_core.gapic_v1.client_info import ClientInfo  # type: ignore
from google.api_core.retry import Retry  # type: ignore
from google.auth.credentials import Credentials  # type: ignore
from google.oauth2 import service_account as service_account  # type: ignore

from google.ads.google_ads.v6.proto.services import (
    shared_criterion_service_pb2 as shared_criterion_service_pb2,
)
from google.ads.google_ads.v6.services import (
    shared_criterion_service_client_config as shared_criterion_service_client_config,
)
from google.ads.google_ads.v6.services.transports import (
    shared_criterion_service_grpc_transport as shared_criterion_service_grpc_transport,
)
from google.ads.google_ads.v6.types import ResponseContentTypeEnum, SharedCriterion

class SharedCriterionServiceClient:
    SERVICE_ADDRESS: ClassVar[str] = ...
    @classmethod
    def from_service_account_file(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> SharedCriterionServiceClient: ...
    @classmethod
    def from_service_account_json(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> SharedCriterionServiceClient: ...
    @classmethod
    def shared_criteria_path(
        cls, customer_id: Any, shared_set_id: Any, criterion_id: Any
    ) -> str: ...
    transport: Union[
        shared_criterion_service_grpc_transport.SharedCriterionServiceGrpcTransport,
        Callable[
            [Credentials, type],
            shared_criterion_service_grpc_transport.SharedCriterionServiceGrpcTransport,
        ],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                shared_criterion_service_grpc_transport.SharedCriterionServiceGrpcTransport,
                Callable[
                    [Credentials, type],
                    shared_criterion_service_grpc_transport.SharedCriterionServiceGrpcTransport,
                ],
            ]
        ] = ...,
        channel: Optional[grpc.Channel] = ...,
        credentials: Optional[Credentials] = ...,
        client_config: Optional[Dict[str, Any]] = ...,
        client_info: Optional[ClientInfo] = ...,
        client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    ) -> None: ...
    def get_shared_criterion(
        self,
        resource_name: str,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> SharedCriterion: ...
    def mutate_shared_criteria(
        self,
        customer_id: str,
        operations: List[
            Union[Dict[str, Any], shared_criterion_service_pb2.SharedCriterionOperation]
        ],
        partial_failure: Optional[bool] = ...,
        validate_only: Optional[bool] = ...,
        response_content_type: Optional[
            ResponseContentTypeEnum.ResponseContentType.V
        ] = ...,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> shared_criterion_service_pb2.MutateSharedCriteriaResponse: ...
