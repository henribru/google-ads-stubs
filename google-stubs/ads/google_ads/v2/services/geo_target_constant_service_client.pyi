import grpc  # type: ignore
from google.ads.google_ads.v2.services.transports.geo_target_constant_service_grpc_transport import (
    GeoTargetConstantServiceGrpcTransport,
)
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
    Text,
)
from google.ads.google_ads.v2.proto.resources.geo_target_constant_pb2 import (
    GeoTargetConstant,
)

from google.ads.google_ads.v2.proto.services.geo_target_constant_service_pb2 import (
    SuggestGeoTargetConstantsResponse,
    SuggestGeoTargetConstantsRequest,
)
from google.protobuf.wrappers_pb2 import StringValue
from typing_extensions import TypedDict

class StringValueDict(TypedDict):
    value: Text

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
    def geo_target_constant_path(cls, geo_target_constant: Any): ...
    transport: Union[
        GeoTargetConstantServiceGrpcTransport,
        Callable[[Credentials, type], GeoTargetConstantServiceGrpcTransport],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                GeoTargetConstantServiceGrpcTransport,
                Callable[[Credentials, type], GeoTargetConstantServiceGrpcTransport],
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
        locale: Union[StringValueDict, StringValue],
        country_code: Union[StringValueDict, StringValue],
        location_names: Optional[
            Union[Dict[str, Any], SuggestGeoTargetConstantsRequest.LocationNames]
        ] = ...,
        geo_targets: Optional[
            Union[Dict[str, Any], SuggestGeoTargetConstantsRequest.GeoTargets]
        ] = ...,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> SuggestGeoTargetConstantsResponse: ...
