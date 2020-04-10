from google.ads.google_ads.v3.proto.services import (
    ad_group_service_pb2 as ad_group_service_pb2,
)
from google.ads.google_ads.v3.services import (
    ad_group_service_client_config as ad_group_service_client_config,
)
from google.ads.google_ads.v3.services.transports import (
    ad_group_service_grpc_transport as ad_group_service_grpc_transport,
)
from google.oauth2 import service_account as service_account  # type: ignore
import grpc  # type: ignore
from google.ads.google_ads.v3.services.transports.ad_group_service_grpc_transport import (
    AdGroupServiceGrpcTransport,
)
from google.auth.credentials import Credentials  # type: ignore
from google.api_core.gapic_v1.client_info import ClientInfo  # type: ignore
from google.api_core.retry import Retry  # type: ignore
from typing import Optional, Dict, Any, List, Sequence, Tuple, Union, Callable, ClassVar
from google.ads.google_ads.v3.proto.resources.ad_group_pb2 import AdGroup
from google.ads.google_ads.v3.proto.services.ad_group_service_pb2 import (
    AdGroupOperation,
    MutateAdGroupsResponse,
)

class AdGroupServiceClient:
    SERVICE_ADDRESS: ClassVar[str] = ...
    @classmethod
    def from_service_account_file(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> AdGroupServiceClient: ...
    @classmethod
    def from_service_account_json(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> AdGroupServiceClient: ...
    @classmethod
    def ad_group_path(cls, customer: Any, ad_group: Any) -> str: ...
    transport: Union[
        AdGroupServiceGrpcTransport,
        Callable[[Credentials, type], AdGroupServiceGrpcTransport],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                AdGroupServiceGrpcTransport,
                Callable[[Credentials, type], AdGroupServiceGrpcTransport],
            ]
        ] = ...,
        channel: Optional[grpc.Channel] = ...,
        credentials: Optional[Credentials] = ...,
        client_config: Optional[Dict[str, Any]] = ...,
        client_info: Optional[ClientInfo] = ...,
    ) -> None: ...
    def get_ad_group(
        self,
        resource_name: str,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> AdGroup: ...
    def mutate_ad_groups(
        self,
        customer_id: str,
        operations: List[Union[Dict[str, Any], AdGroupOperation]],
        partial_failure: Optional[bool] = ...,
        validate_only: Optional[bool] = ...,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> MutateAdGroupsResponse: ...
