import grpc  # type: ignore
from google.ads.google_ads.v1.services.transports.conversion_adjustment_upload_service_grpc_transport import (
    ConversionAdjustmentUploadServiceGrpcTransport,
)
from google.auth.credentials import Credentials  # type: ignore
from google.api_core.gapic_v1.client_info import ClientInfo  # type: ignore
from google.api_core.retry import Retry  # type: ignore
from typing import Optional, Dict, Any, List, Sequence, Tuple, Union, Callable, ClassVar

from google.ads.google_ads.v1.proto.services.conversion_adjustment_upload_service_pb2 import (
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
        partial_failure: Optional[bool] = ...,
        validate_only: Optional[bool] = ...,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> UploadConversionAdjustmentsResponse: ...
