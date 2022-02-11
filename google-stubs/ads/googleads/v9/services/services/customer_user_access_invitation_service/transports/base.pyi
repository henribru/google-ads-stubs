import abc
import typing
from typing import Any

from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials

from google.ads.googleads.v9.resources.types import customer_user_access_invitation
from google.ads.googleads.v9.services.types import (
    customer_user_access_invitation_service,
)

class CustomerUserAccessInvitationServiceTransport(metaclass=abc.ABCMeta):
    AUTH_SCOPES: Any
    def __init__(
        self,
        *,
        host: str = ...,
        credentials: ga_credentials.Credentials = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...
    ) -> None: ...
    def close(self) -> None: ...
    @property
    def get_customer_user_access_invitation(
        self,
    ) -> typing.Callable[
        [
            customer_user_access_invitation_service.GetCustomerUserAccessInvitationRequest
        ],
        customer_user_access_invitation.CustomerUserAccessInvitation,
    ]: ...
    @property
    def mutate_customer_user_access_invitation(
        self,
    ) -> typing.Callable[
        [
            customer_user_access_invitation_service.MutateCustomerUserAccessInvitationRequest
        ],
        customer_user_access_invitation_service.MutateCustomerUserAccessInvitationResponse,
    ]: ...
