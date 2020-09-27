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

from google.ads.google_ads.v5.proto.services import (
    remarketing_action_service_pb2 as remarketing_action_service_pb2,
)
from google.ads.google_ads.v5.services import (
    remarketing_action_service_client_config as remarketing_action_service_client_config,
)
from google.ads.google_ads.v5.services.transports import (
    remarketing_action_service_grpc_transport as remarketing_action_service_grpc_transport,
)
from google.ads.google_ads.v5.types import RemarketingAction

class RemarketingActionServiceClient:
    SERVICE_ADDRESS: ClassVar[str] = ...
    @classmethod
    def from_service_account_file(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> RemarketingActionServiceClient: ...
    @classmethod
    def from_service_account_json(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> RemarketingActionServiceClient: ...
    @classmethod
    def remarketing_action_path(cls, customer: Any, remarketing_action: Any) -> str: ...
    transport: Union[
        remarketing_action_service_grpc_transport.RemarketingActionServiceGrpcTransport,
        Callable[
            [Credentials, type],
            remarketing_action_service_grpc_transport.RemarketingActionServiceGrpcTransport,
        ],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                remarketing_action_service_grpc_transport.RemarketingActionServiceGrpcTransport,
                Callable[
                    [Credentials, type],
                    remarketing_action_service_grpc_transport.RemarketingActionServiceGrpcTransport,
                ],
            ]
        ] = ...,
        channel: Optional[grpc.Channel] = ...,
        credentials: Optional[Credentials] = ...,
        client_config: Optional[Dict[str, Any]] = ...,
        client_info: Optional[ClientInfo] = ...,
        client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    ) -> None: ...
    def get_remarketing_action(
        self,
        resource_name: str,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> RemarketingAction: ...
    def mutate_remarketing_actions(
        self,
        customer_id: str,
        operations: List[
            Union[
                Dict[str, Any],
                remarketing_action_service_pb2.RemarketingActionOperation,
            ]
        ],
        partial_failure: Optional[bool] = ...,
        validate_only: Optional[bool] = ...,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> remarketing_action_service_pb2.MutateRemarketingActionsResponse: ...
