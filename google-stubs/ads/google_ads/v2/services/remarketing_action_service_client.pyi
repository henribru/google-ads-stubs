import grpc  # type: ignore
from google.ads.google_ads.v2.services.transports.remarketing_action_service_grpc_transport import (
    RemarketingActionServiceGrpcTransport,
)
from google.auth.credentials import Credentials  # type: ignore
from google.api_core.gapic_v1.client_info import ClientInfo  # type: ignore
from google.api_core.retry import Retry  # type: ignore
from typing import Optional, Dict, Any, List, Sequence, Tuple, Union, Callable, ClassVar
from google.ads.google_ads.v2.proto.resources.remarketing_action_pb2 import (
    RemarketingAction,
)
from google.ads.google_ads.v2.proto.services.remarketing_action_service_pb2 import (
    RemarketingActionOperation,
    MutateRemarketingActionsResponse,
)

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
        RemarketingActionServiceGrpcTransport,
        Callable[[Credentials, type], RemarketingActionServiceGrpcTransport],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                RemarketingActionServiceGrpcTransport,
                Callable[[Credentials, type], RemarketingActionServiceGrpcTransport],
            ]
        ] = ...,
        channel: Optional[grpc.Channel] = ...,
        credentials: Optional[Credentials] = ...,
        client_config: Optional[Dict[str, Any]] = ...,
        client_info: Optional[ClientInfo] = ...,
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
        operations: List[Union[Dict[str, Any], RemarketingActionOperation]],
        partial_failure: Optional[bool] = ...,
        validate_only: Optional[bool] = ...,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> MutateRemarketingActionsResponse: ...
