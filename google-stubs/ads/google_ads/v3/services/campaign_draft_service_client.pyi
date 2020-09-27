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
from google.api_core.operation import Operation  # type: ignore
from google.api_core.retry import Retry  # type: ignore
from google.auth.credentials import Credentials  # type: ignore
from google.oauth2 import service_account as service_account  # type: ignore
from google.protobuf import empty_pb2 as empty_pb2

from google.ads.google_ads.v3.proto.services import (
    campaign_draft_service_pb2 as campaign_draft_service_pb2,
)
from google.ads.google_ads.v3.services import (
    campaign_draft_service_client_config as campaign_draft_service_client_config,
)
from google.ads.google_ads.v3.services.transports import (
    campaign_draft_service_grpc_transport as campaign_draft_service_grpc_transport,
)
from google.ads.google_ads.v3.types import CampaignDraft, Status

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
        campaign_draft_service_grpc_transport.CampaignDraftServiceGrpcTransport,
        Callable[
            [Credentials, type],
            campaign_draft_service_grpc_transport.CampaignDraftServiceGrpcTransport,
        ],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                campaign_draft_service_grpc_transport.CampaignDraftServiceGrpcTransport,
                Callable[
                    [Credentials, type],
                    campaign_draft_service_grpc_transport.CampaignDraftServiceGrpcTransport,
                ],
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
        operations: List[
            Union[Dict[str, Any], campaign_draft_service_pb2.CampaignDraftOperation]
        ],
        partial_failure: Optional[bool] = ...,
        validate_only: Optional[bool] = ...,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> campaign_draft_service_pb2.MutateCampaignDraftsResponse: ...
    def promote_campaign_draft(
        self,
        campaign_draft: str,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> Iterable[Operation]: ...
    def list_campaign_draft_async_errors(
        self,
        resource_name: str,
        page_size: Optional[int] = ...,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> Iterable[Status]: ...
