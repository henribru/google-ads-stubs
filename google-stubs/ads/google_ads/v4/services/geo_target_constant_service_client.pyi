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

from google.ads.google_ads.v4.proto.services import (
    geo_target_constant_service_pb2 as geo_target_constant_service_pb2,
)
from google.ads.google_ads.v4.services import (
    geo_target_constant_service_client_config as geo_target_constant_service_client_config,
)
from google.ads.google_ads.v4.services.transports import (
    geo_target_constant_service_grpc_transport as geo_target_constant_service_grpc_transport,
)
from google.ads.google_ads.v4.types import (
    GeoTargetConstant,
    StringValue,
    SuggestGeoTargetConstantsRequest,
    SuggestGeoTargetConstantsResponse,
)

class GeoTargetConstantServiceClient:
    SERVICE_ADDRESS: ClassVar[str] = ...
    @classmethod
    def from_service_account_file(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> GeoTargetConstantServiceClient: ...
    @classmethod
    def from_service_account_json(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> GeoTargetConstantServiceClient: ...
    @classmethod
    def geo_target_constant_path(cls, geo_target_constant: Any) -> str: ...
    transport: Union[
        geo_target_constant_service_grpc_transport.GeoTargetConstantServiceGrpcTransport,
        Callable[
            [Credentials, type],
            geo_target_constant_service_grpc_transport.GeoTargetConstantServiceGrpcTransport,
        ],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                geo_target_constant_service_grpc_transport.GeoTargetConstantServiceGrpcTransport,
                Callable[
                    [Credentials, type],
                    geo_target_constant_service_grpc_transport.GeoTargetConstantServiceGrpcTransport,
                ],
            ]
        ] = ...,
        channel: Optional[grpc.Channel] = ...,
        credentials: Optional[Credentials] = ...,
        client_config: Optional[Dict[str, Any]] = ...,
        client_info: Optional[ClientInfo] = ...,
    ) -> None: ...
    def get_geo_target_constant(
        self,
        resource_name: str,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> GeoTargetConstant: ...
    def suggest_geo_target_constants(
        self,
        locale: Union[Dict[str, Any], StringValue],
        country_code: Union[Dict[str, Any], StringValue],
        location_names: Optional[SuggestGeoTargetConstantsRequest.LocationNames] = ...,
        geo_targets: Optional[SuggestGeoTargetConstantsRequest.GeoTargets] = ...,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> SuggestGeoTargetConstantsResponse: ...
