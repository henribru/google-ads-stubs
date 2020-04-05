import grpc  # type: ignore
from google.ads.google_ads.v2.services.transports.campaign_shared_set_service_grpc_transport import (
    CampaignSharedSetServiceGrpcTransport,
)
from google.auth.credentials import Credentials  # type: ignore
from google.api_core.gapic_v1.client_info import ClientInfo  # type: ignore
from google.api_core.retry import Retry  # type: ignore
from typing import Optional, Dict, Any, List, Sequence, Tuple, Union, Callable, ClassVar
from google.ads.google_ads.v2.proto.resources.campaign_shared_set_pb2 import (
    CampaignSharedSet,
)
from google.ads.google_ads.v2.proto.services.campaign_shared_set_service_pb2 import (
    CampaignSharedSetOperation,
    MutateCampaignSharedSetsResponse,
)

class CampaignSharedSetServiceClient:
    SERVICE_ADDRESS: ClassVar[str] = ...
    @classmethod
    def from_service_account_file(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> CampaignSharedSetServiceClient: ...
    @classmethod
    def from_service_account_json(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> CampaignSharedSetServiceClient: ...
    @classmethod
    def campaign_shared_set_path(
        cls, customer: Any, campaign_shared_set: Any
    ) -> str: ...
    transport: Union[
        CampaignSharedSetServiceGrpcTransport,
        Callable[[Credentials, type], CampaignSharedSetServiceGrpcTransport],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                CampaignSharedSetServiceGrpcTransport,
                Callable[[Credentials, type], CampaignSharedSetServiceGrpcTransport],
            ]
        ] = ...,
        channel: Optional[grpc.Channel] = ...,
        credentials: Optional[Credentials] = ...,
        client_config: Optional[Dict[str, Any]] = ...,
        client_info: Optional[ClientInfo] = ...,
    ) -> None: ...
    def get_campaign_shared_set(
        self,
        resource_name: str,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> CampaignSharedSet: ...
    def mutate_campaign_shared_sets(
        self,
        customer_id: str,
        operations: List[Union[Dict[str, Any], CampaignSharedSetOperation]],
        partial_failure: Optional[bool] = ...,
        validate_only: Optional[bool] = ...,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> MutateCampaignSharedSetsResponse: ...
