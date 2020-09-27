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
    conversion_upload_service_pb2 as conversion_upload_service_pb2,
)
from google.ads.google_ads.v4.services import (
    conversion_upload_service_client_config as conversion_upload_service_client_config,
)
from google.ads.google_ads.v4.services.transports import (
    conversion_upload_service_grpc_transport as conversion_upload_service_grpc_transport,
)
from google.ads.google_ads.v4.types import (
    CallConversion,
    ClickConversion,
    UploadCallConversionsResponse,
    UploadClickConversionsResponse,
)

class ConversionUploadServiceClient:
    SERVICE_ADDRESS: ClassVar[str] = ...
    @classmethod
    def from_service_account_file(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> ConversionUploadServiceClient: ...
    @classmethod
    def from_service_account_json(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> ConversionUploadServiceClient: ...
    transport: Union[
        conversion_upload_service_grpc_transport.ConversionUploadServiceGrpcTransport,
        Callable[
            [Credentials, type],
            conversion_upload_service_grpc_transport.ConversionUploadServiceGrpcTransport,
        ],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                conversion_upload_service_grpc_transport.ConversionUploadServiceGrpcTransport,
                Callable[
                    [Credentials, type],
                    conversion_upload_service_grpc_transport.ConversionUploadServiceGrpcTransport,
                ],
            ]
        ] = ...,
        channel: Optional[grpc.Channel] = ...,
        credentials: Optional[Credentials] = ...,
        client_config: Optional[Dict[str, Any]] = ...,
        client_info: Optional[ClientInfo] = ...,
    ) -> None: ...
    def upload_click_conversions(
        self,
        customer_id: str,
        conversions: List[Union[Dict[str, Any], ClickConversion]],
        partial_failure: Optional[bool] = ...,
        validate_only: Optional[bool] = ...,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> UploadClickConversionsResponse: ...
    def upload_call_conversions(
        self,
        customer_id: str,
        conversions: List[Union[Dict[str, Any], CallConversion]],
        partial_failure: Optional[bool] = ...,
        validate_only: Optional[bool] = ...,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> UploadCallConversionsResponse: ...
