import abc
import typing
from typing import Any

from google.api_core import gapic_v1
from google.auth import credentials

from google.ads.googleads.v7.services.types import payments_account_service

class PaymentsAccountServiceTransport(metaclass=abc.ABCMeta):
    AUTH_SCOPES: Any
    def __init__(
        self,
        *,
        host: str = ...,
        credentials: credentials.Credentials = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...
    ) -> None: ...
    @property
    def list_payments_accounts(
        self,
    ) -> typing.Callable[
        [payments_account_service.ListPaymentsAccountsRequest],
        payments_account_service.ListPaymentsAccountsResponse,
    ]: ...
