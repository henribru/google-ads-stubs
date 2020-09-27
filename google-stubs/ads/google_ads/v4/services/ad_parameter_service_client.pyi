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
    ad_parameter_service_pb2 as ad_parameter_service_pb2,
)
from google.ads.google_ads.v4.services import (
    ad_parameter_service_client_config as ad_parameter_service_client_config,
)
from google.ads.google_ads.v4.services.transports import (
    ad_parameter_service_grpc_transport as ad_parameter_service_grpc_transport,
)
from google.ads.google_ads.v4.types import AdParameter

class AdParameterServiceClient:
    SERVICE_ADDRESS: ClassVar[str] = ...
    @classmethod
    def from_service_account_file(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> AdParameterServiceClient: ...
    @classmethod
    def from_service_account_json(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> AdParameterServiceClient: ...
    @classmethod
    def ad_parameter_path(cls, customer: Any, ad_parameter: Any) -> str: ...
    transport: Union[
        ad_parameter_service_grpc_transport.AdParameterServiceGrpcTransport,
        Callable[
            [Credentials, type],
            ad_parameter_service_grpc_transport.AdParameterServiceGrpcTransport,
        ],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                ad_parameter_service_grpc_transport.AdParameterServiceGrpcTransport,
                Callable[
                    [Credentials, type],
                    ad_parameter_service_grpc_transport.AdParameterServiceGrpcTransport,
                ],
            ]
        ] = ...,
        channel: Optional[grpc.Channel] = ...,
        credentials: Optional[Credentials] = ...,
        client_config: Optional[Dict[str, Any]] = ...,
        client_info: Optional[ClientInfo] = ...,
    ) -> None: ...
    def get_ad_parameter(
        self,
        resource_name: str,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> AdParameter: ...
    def mutate_ad_parameters(
        self,
        customer_id: str,
        operations: List[
            Union[Dict[str, Any], ad_parameter_service_pb2.AdParameterOperation]
        ],
        partial_failure: Optional[bool] = ...,
        validate_only: Optional[bool] = ...,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> ad_parameter_service_pb2.MutateAdParametersResponse: ...
