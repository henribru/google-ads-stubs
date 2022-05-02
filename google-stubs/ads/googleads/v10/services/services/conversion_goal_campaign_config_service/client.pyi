from typing import Dict, Optional, Sequence, Tuple, Type, Union

from _typeshed import Incomplete
from google.api_core import (
    client_options as client_options_lib,
    gapic_v1,
    retry as retries,
)
from google.auth import credentials as ga_credentials

from google.ads.googleads.v10.services.types import (
    conversion_goal_campaign_config_service,
)

from .transports.base import ConversionGoalCampaignConfigServiceTransport

class ConversionGoalCampaignConfigServiceClientMeta(type):
    def get_transport_class(
        cls, label: str = ...
    ) -> Type[ConversionGoalCampaignConfigServiceTransport]: ...

class ConversionGoalCampaignConfigServiceClient(
    metaclass=ConversionGoalCampaignConfigServiceClientMeta
):
    DEFAULT_ENDPOINT: str
    DEFAULT_MTLS_ENDPOINT: Incomplete
    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs): ...
    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs): ...
    from_service_account_json: Incomplete
    @property
    def transport(self) -> ConversionGoalCampaignConfigServiceTransport: ...
    def __enter__(self): ...
    def __exit__(self, type, value, traceback) -> None: ...
    @staticmethod
    def campaign_path(customer_id: str, campaign_id: str) -> str: ...
    @staticmethod
    def parse_campaign_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def conversion_goal_campaign_config_path(
        customer_id: str, campaign_id: str
    ) -> str: ...
    @staticmethod
    def parse_conversion_goal_campaign_config_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def custom_conversion_goal_path(customer_id: str, goal_id: str) -> str: ...
    @staticmethod
    def parse_custom_conversion_goal_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def common_billing_account_path(billing_account: str) -> str: ...
    @staticmethod
    def parse_common_billing_account_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def common_folder_path(folder: str) -> str: ...
    @staticmethod
    def parse_common_folder_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def common_organization_path(organization: str) -> str: ...
    @staticmethod
    def parse_common_organization_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def common_project_path(project: str) -> str: ...
    @staticmethod
    def parse_common_project_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def common_location_path(project: str, location: str) -> str: ...
    @staticmethod
    def parse_common_location_path(path: str) -> Dict[str, str]: ...
    def __init__(
        self,
        *,
        credentials: Optional[ga_credentials.Credentials] = ...,
        transport: Union[str, ConversionGoalCampaignConfigServiceTransport, None] = ...,
        client_options: Optional[client_options_lib.ClientOptions] = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...
    ) -> None: ...
    def mutate_conversion_goal_campaign_configs(
        self,
        request: Union[
            conversion_goal_campaign_config_service.MutateConversionGoalCampaignConfigsRequest,
            dict,
        ] = ...,
        *,
        customer_id: str = ...,
        operations: Sequence[
            conversion_goal_campaign_config_service.ConversionGoalCampaignConfigOperation
        ] = ...,
        retry: Union[retries.Retry, gapic_v1.method._MethodDefault] = ...,
        timeout: float = ...,
        metadata: Sequence[Tuple[str, str]] = ...
    ) -> conversion_goal_campaign_config_service.MutateConversionGoalCampaignConfigsResponse: ...
