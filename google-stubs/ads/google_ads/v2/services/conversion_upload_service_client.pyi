import grpc  # type: ignore
from google.ads.google_ads.v2.services.transports.conversion_upload_service_grpc_transport import (
    ConversionUploadServiceGrpcTransport,
)
from google.auth.credentials import Credentials  # type: ignore
from google.api_core.gapic_v1.client_info import ClientInfo  # type: ignore
from google.api_core.retry import Retry  # type: ignore
from typing import Optional, Dict, Any, List, Sequence, Tuple, Union, Callable, ClassVar

from google.ads.google_ads.v2.proto.services.conversion_upload_service_pb2 import (
    ClickConversion,
    UploadClickConversionsResponse,
    CallConversion,
    UploadCallConversionsResponse,
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
        ConversionUploadServiceGrpcTransport,
        Callable[[Credentials, type], ConversionUploadServiceGrpcTransport],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                ConversionUploadServiceGrpcTransport,
                Callable[[Credentials, type], ConversionUploadServiceGrpcTransport],
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
