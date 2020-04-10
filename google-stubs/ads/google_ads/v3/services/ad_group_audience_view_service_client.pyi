from google.ads.google_ads.v3.proto.services import (
    ad_group_audience_view_service_pb2 as ad_group_audience_view_service_pb2,
)
from google.ads.google_ads.v3.services import (
    ad_group_audience_view_service_client_config as ad_group_audience_view_service_client_config,
)
from google.ads.google_ads.v3.services.transports import (
    ad_group_audience_view_service_grpc_transport as ad_group_audience_view_service_grpc_transport,
)
from google.oauth2 import service_account as service_account  # type: ignore
import grpc  # type: ignore
from google.ads.google_ads.v3.services.transports.ad_group_audience_view_service_grpc_transport import (
    AdGroupAudienceViewServiceGrpcTransport,
)
from google.auth.credentials import Credentials  # type: ignore
from google.api_core.gapic_v1.client_info import ClientInfo  # type: ignore
from google.api_core.retry import Retry  # type: ignore
from typing import Optional, Dict, Any, List, Sequence, Tuple, Union, Callable, ClassVar
from google.ads.google_ads.v3.proto.resources.ad_group_audience_view_pb2 import (
    AdGroupAudienceView,
)

class AdGroupAudienceViewServiceClient:
    SERVICE_ADDRESS: ClassVar[str] = ...
    @classmethod
    def from_service_account_file(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> AdGroupAudienceViewServiceClient: ...
    @classmethod
    def from_service_account_json(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> AdGroupAudienceViewServiceClient: ...
    @classmethod
    def ad_group_audience_view_path(
        cls, customer: Any, ad_group_audience_view: Any
    ) -> str: ...
    transport: Union[
        AdGroupAudienceViewServiceGrpcTransport,
        Callable[[Credentials, type], AdGroupAudienceViewServiceGrpcTransport],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                AdGroupAudienceViewServiceGrpcTransport,
                Callable[[Credentials, type], AdGroupAudienceViewServiceGrpcTransport],
            ]
        ] = ...,
        channel: Optional[grpc.Channel] = ...,
        credentials: Optional[Credentials] = ...,
        client_config: Optional[Dict[str, Any]] = ...,
        client_info: Optional[ClientInfo] = ...,
    ) -> None: ...
    def get_ad_group_audience_view(
        self,
        resource_name: str,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> AdGroupAudienceView: ...
