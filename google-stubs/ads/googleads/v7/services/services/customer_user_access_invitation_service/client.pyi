from typing import Any, Dict, Optional, Sequence, Tuple, Type, Union

from google.api_core import (
    client_options as client_options_lib,
    gapic_v1,
    retry as retries,
)
from google.auth import credentials

from google.ads.googleads.v7.resources.types import customer_user_access_invitation
from google.ads.googleads.v7.services.types import (
    customer_user_access_invitation_service,
)

from .transports.base import CustomerUserAccessInvitationServiceTransport

class CustomerUserAccessInvitationServiceClientMeta(type):
    def get_transport_class(
        cls, label: str = ...
    ) -> Type[CustomerUserAccessInvitationServiceTransport]: ...

class CustomerUserAccessInvitationServiceClient(
    metaclass=CustomerUserAccessInvitationServiceClientMeta
):
    DEFAULT_ENDPOINT: str
    DEFAULT_MTLS_ENDPOINT: Any
    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs): ...
    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs): ...
    from_service_account_json: Any
    @property
    def transport(self) -> CustomerUserAccessInvitationServiceTransport: ...
    @staticmethod
    def customer_user_access_invitation_path(
        customer_id: str, invitation_id: str
    ) -> str: ...
    @staticmethod
    def parse_customer_user_access_invitation_path(path: str) -> Dict[str, str]: ...
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
        credentials: Optional[credentials.Credentials] = ...,
        transport: Union[str, CustomerUserAccessInvitationServiceTransport, None] = ...,
        client_options: Optional[client_options_lib.ClientOptions] = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...
    ) -> None: ...
    def get_customer_user_access_invitation(
        self,
        request: customer_user_access_invitation_service.GetCustomerUserAccessInvitationRequest = ...,
        *,
        resource_name: str = ...,
        retry: retries.Retry = ...,
        timeout: float = ...,
        metadata: Sequence[Tuple[str, str]] = ...
    ) -> customer_user_access_invitation.CustomerUserAccessInvitation: ...
    def mutate_customer_user_access_invitation(
        self,
        request: customer_user_access_invitation_service.MutateCustomerUserAccessInvitationRequest = ...,
        *,
        customer_id: str = ...,
        operation: customer_user_access_invitation_service.CustomerUserAccessInvitationOperation = ...,
        retry: retries.Retry = ...,
        timeout: float = ...,
        metadata: Sequence[Tuple[str, str]] = ...
    ) -> customer_user_access_invitation_service.MutateCustomerUserAccessInvitationResponse: ...
