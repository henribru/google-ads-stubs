import grpc  # type: ignore
from google.ads.google_ads.v1.services.transports.customer_extension_setting_service_grpc_transport import (
    CustomerExtensionSettingServiceGrpcTransport,
)
from google.auth.credentials import Credentials  # type: ignore
from google.api_core.gapic_v1.client_info import ClientInfo  # type: ignore
from google.api_core.retry import Retry  # type: ignore
from typing import Optional, Dict, Any, List, Sequence, Tuple, Union, Callable, ClassVar
from google.ads.google_ads.v1.proto.resources.customer_extension_setting_pb2 import (
    CustomerExtensionSetting,
)
from google.ads.google_ads.v1.proto.services.customer_extension_setting_service_pb2 import (
    CustomerExtensionSettingOperation,
    MutateCustomerExtensionSettingsResponse,
)

class CustomerExtensionSettingServiceClient:
    SERVICE_ADDRESS: ClassVar[str] = ...
    @classmethod
    def from_service_account_file(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> CustomerExtensionSettingServiceClient: ...
    @classmethod
    def from_service_account_json(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> CustomerExtensionSettingServiceClient: ...
    @classmethod
    def customer_extension_setting_path(
        cls, customer: Any, customer_extension_setting: Any
    ) -> str: ...
    transport: Union[
        CustomerExtensionSettingServiceGrpcTransport,
        Callable[[Credentials, type], CustomerExtensionSettingServiceGrpcTransport],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                CustomerExtensionSettingServiceGrpcTransport,
                Callable[
                    [Credentials, type], CustomerExtensionSettingServiceGrpcTransport
                ],
            ]
        ] = ...,
        channel: Optional[grpc.Channel] = ...,
        credentials: Optional[Credentials] = ...,
        client_config: Optional[Dict[str, Any]] = ...,
        client_info: Optional[ClientInfo] = ...,
    ) -> None: ...
    def get_customer_extension_setting(
        self,
        resource_name: str,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> CustomerExtensionSetting: ...
    def mutate_customer_extension_settings(
        self,
        customer_id: str,
        operations: List[Union[Dict[str, Any], CustomerExtensionSettingOperation]],
        partial_failure: Optional[bool] = ...,
        validate_only: Optional[bool] = ...,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> MutateCustomerExtensionSettingsResponse: ...
