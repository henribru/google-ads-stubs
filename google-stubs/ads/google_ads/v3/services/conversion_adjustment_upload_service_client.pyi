from google.ads.google_ads.v3.proto.services import (
    conversion_adjustment_upload_service_pb2 as conversion_adjustment_upload_service_pb2,
)
from google.ads.google_ads.v3.services import (
    conversion_adjustment_upload_service_client_config as conversion_adjustment_upload_service_client_config,
)
from google.ads.google_ads.v3.services.transports import (
    conversion_adjustment_upload_service_grpc_transport as conversion_adjustment_upload_service_grpc_transport,
)
from google.oauth2 import service_account as service_account  # type: ignore
import grpc  # type: ignore
from google.ads.google_ads.v3.services.transports.conversion_adjustment_upload_service_grpc_transport import (
    ConversionAdjustmentUploadServiceGrpcTransport,
)
from google.auth.credentials import Credentials  # type: ignore
from google.api_core.gapic_v1.client_info import ClientInfo  # type: ignore
from google.api_core.retry import Retry  # type: ignore
from typing import Optional, Dict, Any, List, Sequence, Tuple, Union, Callable, ClassVar
from google.ads.google_ads.v3.types import (
    ConversionAdjustment,
    UploadConversionAdjustmentsResponse,
)

class ConversionAdjustmentUploadServiceClient:
    SERVICE_ADDRESS: ClassVar[str] = ...
    @classmethod
    def from_service_account_file(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> ConversionAdjustmentUploadServiceClient: ...
    @classmethod
    def from_service_account_json(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> ConversionAdjustmentUploadServiceClient: ...
    transport: Union[
        ConversionAdjustmentUploadServiceGrpcTransport,
        Callable[[Credentials, type], ConversionAdjustmentUploadServiceGrpcTransport],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                ConversionAdjustmentUploadServiceGrpcTransport,
                Callable[
                    [Credentials, type], ConversionAdjustmentUploadServiceGrpcTransport
                ],
            ]
        ] = ...,
        channel: Optional[grpc.Channel] = ...,
        credentials: Optional[Credentials] = ...,
        client_config: Optional[Dict[str, Any]] = ...,
        client_info: Optional[ClientInfo] = ...,
    ) -> None: ...
    def upload_conversion_adjustments(
        self,
        customer_id: str,
        conversion_adjustments: List[Union[Dict[str, Any], ConversionAdjustment]],
        partial_failure: Optional[str] = ...,
        validate_only: Optional[str] = ...,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> UploadConversionAdjustmentsResponse: ...
