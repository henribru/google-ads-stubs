import grpc  # type: ignore
from google.ads.google_ads.v2.services.transports.campaign_audience_view_service_grpc_transport import (
    CampaignAudienceViewServiceGrpcTransport,
)
from google.auth.credentials import Credentials  # type: ignore
from google.api_core.gapic_v1.client_info import ClientInfo  # type: ignore
from google.api_core.retry import Retry  # type: ignore
from typing import Optional, Dict, Any, List, Sequence, Tuple, Union, Callable, ClassVar
from google.ads.google_ads.v2.proto.resources.campaign_audience_view_pb2 import (
    CampaignAudienceView,
)

class CampaignAudienceViewServiceClient:
    SERVICE_ADDRESS: ClassVar[str] = ...
    @classmethod
    def from_service_account_file(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> CampaignAudienceViewServiceClient: ...
    @classmethod
    def from_service_account_json(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> CampaignAudienceViewServiceClient: ...
    @classmethod
    def campaign_audience_view_path(
        cls, customer: Any, campaign_audience_view: Any
    ) -> str: ...
    transport: Union[
        CampaignAudienceViewServiceGrpcTransport,
        Callable[[Credentials, type], CampaignAudienceViewServiceGrpcTransport],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                CampaignAudienceViewServiceGrpcTransport,
                Callable[[Credentials, type], CampaignAudienceViewServiceGrpcTransport],
            ]
        ] = ...,
        channel: Optional[grpc.Channel] = ...,
        credentials: Optional[Credentials] = ...,
        client_config: Optional[Dict[str, Any]] = ...,
        client_info: Optional[ClientInfo] = ...,
    ) -> None: ...
    def get_campaign_audience_view(
        self,
        resource_name: str,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> CampaignAudienceView: ...
