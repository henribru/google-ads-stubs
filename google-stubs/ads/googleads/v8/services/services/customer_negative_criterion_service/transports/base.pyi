import abc
import typing
from typing import Any

from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials

from google.ads.googleads.v8.resources.types import customer_negative_criterion
from google.ads.googleads.v8.services.types import customer_negative_criterion_service

class CustomerNegativeCriterionServiceTransport(metaclass=abc.ABCMeta):
    AUTH_SCOPES: Any
    def __init__(
        self,
        *,
        host: str = ...,
        credentials: ga_credentials.Credentials = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...
    ) -> None: ...
    @property
    def get_customer_negative_criterion(
        self,
    ) -> typing.Callable[
        [customer_negative_criterion_service.GetCustomerNegativeCriterionRequest],
        customer_negative_criterion.CustomerNegativeCriterion,
    ]: ...
    @property
    def mutate_customer_negative_criteria(
        self,
    ) -> typing.Callable[
        [customer_negative_criterion_service.MutateCustomerNegativeCriteriaRequest],
        customer_negative_criterion_service.MutateCustomerNegativeCriteriaResponse,
    ]: ...
