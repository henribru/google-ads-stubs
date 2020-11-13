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
    asset_service_pb2 as asset_service_pb2,
)
from google.ads.google_ads.v6.services import (
    asset_service_client_config as asset_service_client_config,
)
from google.ads.google_ads.v6.services.transports import (
    asset_service_grpc_transport as asset_service_grpc_transport,
)
from google.ads.google_ads.v6.types import Asset, ResponseContentTypeEnum

class AssetServiceClient:
    SERVICE_ADDRESS: ClassVar[str] = ...
    @classmethod
    def from_service_account_file(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> AssetServiceClient: ...
    @classmethod
    def from_service_account_json(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> AssetServiceClient: ...
    @classmethod
    def asset_path(cls, customer: Any, asset: Any) -> str: ...
    transport: Union[
        asset_service_grpc_transport.AssetServiceGrpcTransport,
        Callable[
            [Credentials, type], asset_service_grpc_transport.AssetServiceGrpcTransport
        ],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                asset_service_grpc_transport.AssetServiceGrpcTransport,
                Callable[
                    [Credentials, type],
                    asset_service_grpc_transport.AssetServiceGrpcTransport,
                ],
            ]
        ] = ...,
        channel: Optional[grpc.Channel] = ...,
        credentials: Optional[Credentials] = ...,
        client_config: Optional[Dict[str, Any]] = ...,
        client_info: Optional[ClientInfo] = ...,
        client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    ) -> None: ...
    def get_asset(
        self,
        resource_name: str,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> Asset: ...
    def mutate_assets(
        self,
        customer_id: str,
        operations: List[Union[Dict[str, Any], asset_service_pb2.AssetOperation]],
        response_content_type: Optional[
            ResponseContentTypeEnum.ResponseContentTypeValue
        ] = ...,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> asset_service_pb2.MutateAssetsResponse: ...
