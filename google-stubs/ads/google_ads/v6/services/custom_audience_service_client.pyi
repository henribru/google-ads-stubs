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

from google.ads.google_ads.v6.proto.services import (
    custom_audience_service_pb2 as custom_audience_service_pb2,
)
from google.ads.google_ads.v6.services import (
    custom_audience_service_client_config as custom_audience_service_client_config,
)
from google.ads.google_ads.v6.services.transports import (
    custom_audience_service_grpc_transport as custom_audience_service_grpc_transport,
)
from google.ads.google_ads.v6.types import CustomAudience

class CustomAudienceServiceClient:
    SERVICE_ADDRESS: ClassVar[str] = ...
    @classmethod
    def from_service_account_file(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> CustomAudienceServiceClient: ...
    @classmethod
    def from_service_account_json(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> CustomAudienceServiceClient: ...
    @classmethod
    def custom_audience_path(cls, customer: Any, custom_audience: Any) -> str: ...
    transport: Union[
        custom_audience_service_grpc_transport.CustomAudienceServiceGrpcTransport,
        Callable[
            [Credentials, type],
            custom_audience_service_grpc_transport.CustomAudienceServiceGrpcTransport,
        ],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                custom_audience_service_grpc_transport.CustomAudienceServiceGrpcTransport,
                Callable[
                    [Credentials, type],
                    custom_audience_service_grpc_transport.CustomAudienceServiceGrpcTransport,
                ],
            ]
        ] = ...,
        channel: Optional[grpc.Channel] = ...,
        credentials: Optional[Credentials] = ...,
        client_config: Optional[Dict[str, Any]] = ...,
        client_info: Optional[ClientInfo] = ...,
        client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    ) -> None: ...
    def get_custom_audience(
        self,
        resource_name: str,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> CustomAudience: ...
    def mutate_custom_audiences(
        self,
        customer_id: str,
        operations: List[
            Union[Dict[str, Any], custom_audience_service_pb2.CustomAudienceOperation]
        ],
        validate_only: Optional[bool] = ...,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> custom_audience_service_pb2.MutateCustomAudiencesResponse: ...
