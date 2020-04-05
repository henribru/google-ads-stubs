import grpc  # type: ignore
from google.ads.google_ads.v2.services.transports.asset_service_grpc_transport import (
    AssetServiceGrpcTransport,
)
from google.auth.credentials import Credentials  # type: ignore
from google.api_core.gapic_v1.client_info import ClientInfo  # type: ignore
from google.api_core.retry import Retry  # type: ignore
from typing import Optional, Dict, Any, List, Sequence, Tuple, Union, Callable, ClassVar
from google.ads.google_ads.v2.proto.resources.asset_pb2 import Asset
from google.ads.google_ads.v2.proto.services.asset_service_pb2 import (
    AssetOperation,
    MutateAssetsResponse,
)

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
        AssetServiceGrpcTransport,
        Callable[[Credentials, type], AssetServiceGrpcTransport],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                AssetServiceGrpcTransport,
                Callable[[Credentials, type], AssetServiceGrpcTransport],
            ]
        ] = ...,
        channel: Optional[grpc.Channel] = ...,
        credentials: Optional[Credentials] = ...,
        client_config: Optional[Dict[str, Any]] = ...,
        client_info: Optional[ClientInfo] = ...,
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
        operations: List[Union[Dict[str, Any], AssetOperation]],
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> MutateAssetsResponse: ...
