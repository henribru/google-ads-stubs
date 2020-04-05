import grpc  # type: ignore
from google.ads.google_ads.v1.services.transports.ad_group_extension_setting_service_grpc_transport import (
    AdGroupExtensionSettingServiceGrpcTransport,
)
from google.auth.credentials import Credentials  # type: ignore
from google.api_core.gapic_v1.client_info import ClientInfo  # type: ignore
from google.api_core.retry import Retry  # type: ignore
from typing import Optional, Dict, Any, List, Sequence, Tuple, Union, Callable, ClassVar
from google.ads.google_ads.v1.proto.resources.ad_group_extension_setting_pb2 import (
    AdGroupExtensionSetting,
)
from google.ads.google_ads.v1.proto.services.ad_group_extension_setting_service_pb2 import (
    AdGroupExtensionSettingOperation,
    MutateAdGroupExtensionSettingsResponse,
)

class AdGroupExtensionSettingServiceClient:
    SERVICE_ADDRESS: ClassVar[str] = ...
    @classmethod
    def from_service_account_file(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> AdGroupExtensionSettingServiceClient: ...
    @classmethod
    def from_service_account_json(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> AdGroupExtensionSettingServiceClient: ...
    @classmethod
    def ad_group_extension_setting_path(
        cls, customer: Any, ad_group_extension_setting: Any
    ) -> str: ...
    transport: Union[
        AdGroupExtensionSettingServiceGrpcTransport,
        Callable[[Credentials, type], AdGroupExtensionSettingServiceGrpcTransport],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                AdGroupExtensionSettingServiceGrpcTransport,
                Callable[
                    [Credentials, type], AdGroupExtensionSettingServiceGrpcTransport
                ],
            ]
        ] = ...,
        channel: Optional[grpc.Channel] = ...,
        credentials: Optional[Credentials] = ...,
        client_config: Optional[Dict[str, Any]] = ...,
        client_info: Optional[ClientInfo] = ...,
    ) -> None: ...
    def get_ad_group_extension_setting(
        self,
        resource_name: str,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> AdGroupExtensionSetting: ...
    def mutate_ad_group_extension_settings(
        self,
        customer_id: str,
        operations: List[Union[Dict[str, Any], AdGroupExtensionSettingOperation]],
        partial_failure: Optional[bool] = ...,
        validate_only: Optional[bool] = ...,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> MutateAdGroupExtensionSettingsResponse: ...
