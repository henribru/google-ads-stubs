import abc
import typing
from typing import Any

from google.api_core import gapic_v1
from google.auth import credentials

from google.ads.googleads.v7.resources.types import billing_setup
from google.ads.googleads.v7.services.types import billing_setup_service

class BillingSetupServiceTransport(metaclass=abc.ABCMeta):
    AUTH_SCOPES: Any
    def __init__(
        self,
        *,
        host: str = ...,
        credentials: credentials.Credentials = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...
    ) -> None: ...
    @property
    def get_billing_setup(
        self,
    ) -> typing.Callable[
        [billing_setup_service.GetBillingSetupRequest], billing_setup.BillingSetup
    ]: ...
    @property
    def mutate_billing_setup(
        self,
    ) -> typing.Callable[
        [billing_setup_service.MutateBillingSetupRequest],
        billing_setup_service.MutateBillingSetupResponse,
    ]: ...
