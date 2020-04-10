import grpc  # type: ignore
from google.ads.google_ads.v2.services.transports.campaign_draft_service_grpc_transport import (
    CampaignDraftServiceGrpcTransport,
)
from google.api_core.operation import Operation  # type: ignore
from google.auth.credentials import Credentials  # type: ignore
from google.api_core.gapic_v1.client_info import ClientInfo  # type: ignore
from google.api_core.retry import Retry  # type: ignore
from typing import (
    Optional,
    Dict,
    Any,
    List,
    Sequence,
    Tuple,
    Union,
    Callable,
    ClassVar,
    Iterable,
)
from google.ads.google_ads.v2.proto.resources.campaign_draft_pb2 import CampaignDraft
from google.ads.google_ads.v2.proto.services.campaign_draft_service_pb2 import (
    CampaignDraftOperation,
    MutateCampaignDraftsResponse,
)
from google.ads.google_ads.v2.types import Status

class CampaignDraftServiceClient:
    SERVICE_ADDRESS: ClassVar[str] = ...
    @classmethod
    def from_service_account_file(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> CampaignDraftServiceClient: ...
    @classmethod
    def from_service_account_json(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> CampaignDraftServiceClient: ...
    @classmethod
    def campaign_draft_path(cls, customer: Any, campaign_draft: Any) -> str: ...
    transport: Union[
        CampaignDraftServiceGrpcTransport,
        Callable[[Credentials, type], CampaignDraftServiceGrpcTransport],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                CampaignDraftServiceGrpcTransport,
                Callable[[Credentials, type], CampaignDraftServiceGrpcTransport],
            ]
        ] = ...,
        channel: Optional[grpc.Channel] = ...,
        credentials: Optional[Credentials] = ...,
        client_config: Optional[Dict[str, Any]] = ...,
        client_info: Optional[ClientInfo] = ...,
    ) -> None: ...
    def get_campaign_draft(
        self,
        resource_name: str,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> CampaignDraft: ...
    def mutate_campaign_drafts(
        self,
        customer_id: str,
        operations: List[Union[Dict[str, Any], CampaignDraftOperation]],
        partial_failure: Optional[bool] = ...,
        validate_only: Optional[bool] = ...,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> MutateCampaignDraftsResponse: ...
    def promote_campaign_draft(
        self,
        campaign_draft: str,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> Operation: ...
    def list_campaign_draft_async_errors(
        self,
        resource_name: str,
        page_size: Optional[int] = ...,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> Iterable[Status]: ...
