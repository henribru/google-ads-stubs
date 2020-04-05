import grpc  # type: ignore
from google.ads.google_ads.v2.services.transports.campaign_extension_setting_service_grpc_transport import (
    CampaignExtensionSettingServiceGrpcTransport,
)
from google.auth.credentials import Credentials  # type: ignore
from google.api_core.gapic_v1.client_info import ClientInfo  # type: ignore
from google.api_core.retry import Retry  # type: ignore
from typing import Optional, Dict, Any, List, Sequence, Tuple, Union, Callable, ClassVar
from google.ads.google_ads.v2.proto.resources.campaign_extension_setting_pb2 import (
    CampaignExtensionSetting,
)
from google.ads.google_ads.v2.proto.services.campaign_extension_setting_service_pb2 import (
    CampaignExtensionSettingOperation,
    MutateCampaignExtensionSettingsResponse,
)

class CampaignExtensionSettingServiceClient:
    SERVICE_ADDRESS: ClassVar[str] = ...
    @classmethod
    def from_service_account_file(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> CampaignExtensionSettingServiceClient: ...
    @classmethod
    def from_service_account_json(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> CampaignExtensionSettingServiceClient: ...
    @classmethod
    def campaign_extension_setting_path(
        cls, customer: Any, campaign_extension_setting: Any
    ) -> str: ...
    transport: Union[
        CampaignExtensionSettingServiceGrpcTransport,
        Callable[[Credentials, type], CampaignExtensionSettingServiceGrpcTransport],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                CampaignExtensionSettingServiceGrpcTransport,
                Callable[
                    [Credentials, type], CampaignExtensionSettingServiceGrpcTransport
                ],
            ]
        ] = ...,
        channel: Optional[grpc.Channel] = ...,
        credentials: Optional[Credentials] = ...,
        client_config: Optional[Dict[str, Any]] = ...,
        client_info: Optional[ClientInfo] = ...,
    ) -> None: ...
    def get_campaign_extension_setting(
        self,
        resource_name: str,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> CampaignExtensionSetting: ...
    def mutate_campaign_extension_settings(
        self,
        customer_id: str,
        operations: List[Union[Dict[str, Any], CampaignExtensionSettingOperation]],
        partial_failure: Optional[bool] = ...,
        validate_only: Optional[bool] = ...,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> MutateCampaignExtensionSettingsResponse: ...
