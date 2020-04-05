import grpc  # type: ignore
from google.ads.google_ads.v1.services.transports.ad_group_feed_service_grpc_transport import (
    AdGroupFeedServiceGrpcTransport,
)
from google.auth.credentials import Credentials  # type: ignore
from google.api_core.gapic_v1.client_info import ClientInfo  # type: ignore
from google.api_core.retry import Retry  # type: ignore
from typing import Optional, Dict, Any, List, Sequence, Tuple, Union, Callable, ClassVar
from google.ads.google_ads.v1.proto.resources.ad_group_feed_pb2 import AdGroupFeed
from google.ads.google_ads.v1.proto.services.ad_group_feed_service_pb2 import (
    AdGroupFeedOperation,
    MutateAdGroupFeedsResponse,
)

class AdGroupFeedServiceClient:
    SERVICE_ADDRESS: ClassVar[str] = ...
    @classmethod
    def from_service_account_file(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> AdGroupFeedServiceClient: ...
    @classmethod
    def from_service_account_json(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> AdGroupFeedServiceClient: ...
    @classmethod
    def ad_group_feed_path(cls, customer: Any, ad_group_feed: Any) -> str: ...
    transport: Union[
        AdGroupFeedServiceGrpcTransport,
        Callable[[Credentials, type], AdGroupFeedServiceGrpcTransport],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                AdGroupFeedServiceGrpcTransport,
                Callable[[Credentials, type], AdGroupFeedServiceGrpcTransport],
            ]
        ] = ...,
        channel: Optional[grpc.Channel] = ...,
        credentials: Optional[Credentials] = ...,
        client_config: Optional[Dict[str, Any]] = ...,
        client_info: Optional[ClientInfo] = ...,
    ) -> None: ...
    def get_ad_group_feed(
        self,
        resource_name: str,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> AdGroupFeed: ...
    def mutate_ad_group_feeds(
        self,
        customer_id: str,
        operations: List[Union[Dict[str, Any], AdGroupFeedOperation]],
        partial_failure: Optional[bool] = ...,
        validate_only: Optional[bool] = ...,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> MutateAdGroupFeedsResponse: ...
