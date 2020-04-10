from google.ads.google_ads.v3.proto.services import (
    language_constant_service_pb2 as language_constant_service_pb2,
)
from google.ads.google_ads.v3.services import (
    language_constant_service_client_config as language_constant_service_client_config,
)
from google.ads.google_ads.v3.services.transports import (
    language_constant_service_grpc_transport as language_constant_service_grpc_transport,
)
from google.oauth2 import service_account as service_account  # type: ignore
import grpc  # type: ignore
from google.ads.google_ads.v3.services.transports.language_constant_service_grpc_transport import (
    LanguageConstantServiceGrpcTransport,
)
from google.auth.credentials import Credentials  # type: ignore
from google.api_core.gapic_v1.client_info import ClientInfo  # type: ignore
from google.api_core.retry import Retry  # type: ignore
from typing import Optional, Dict, Any, List, Sequence, Tuple, Union, Callable, ClassVar
from google.ads.google_ads.v3.proto.resources.language_constant_pb2 import (
    LanguageConstant,
)

class LanguageConstantServiceClient:
    SERVICE_ADDRESS: ClassVar[str] = ...
    @classmethod
    def from_service_account_file(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> LanguageConstantServiceClient: ...
    @classmethod
    def from_service_account_json(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> LanguageConstantServiceClient: ...
    @classmethod
    def language_constant_path(cls, language_constant: Any): ...
    transport: Union[
        LanguageConstantServiceGrpcTransport,
        Callable[[Credentials, type], LanguageConstantServiceGrpcTransport],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                LanguageConstantServiceGrpcTransport,
                Callable[[Credentials, type], LanguageConstantServiceGrpcTransport],
            ]
        ] = ...,
        channel: Optional[grpc.Channel] = ...,
        credentials: Optional[Credentials] = ...,
        client_config: Optional[Dict[str, Any]] = ...,
        client_info: Optional[ClientInfo] = ...,
    ) -> None: ...
    def get_language_constant(
        self,
        resource_name: str,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> LanguageConstant: ...
