import abc
import typing
from typing import Any

from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials

from google.ads.googleads.v8.resources.types import conversion_value_rule_set
from google.ads.googleads.v8.services.types import conversion_value_rule_set_service

class ConversionValueRuleSetServiceTransport(metaclass=abc.ABCMeta):
    AUTH_SCOPES: Any
    def __init__(
        self,
        *,
        host: str = ...,
        credentials: ga_credentials.Credentials = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...
    ) -> None: ...
    @property
    def get_conversion_value_rule_set(
        self,
    ) -> typing.Callable[
        [conversion_value_rule_set_service.GetConversionValueRuleSetRequest],
        conversion_value_rule_set.ConversionValueRuleSet,
    ]: ...
    @property
    def mutate_conversion_value_rule_sets(
        self,
    ) -> typing.Callable[
        [conversion_value_rule_set_service.MutateConversionValueRuleSetsRequest],
        conversion_value_rule_set_service.MutateConversionValueRuleSetsResponse,
    ]: ...
