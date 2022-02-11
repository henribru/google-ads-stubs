import abc
import typing
from typing import Any

from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials

from google.ads.googleads.v9.resources.types import conversion_value_rule
from google.ads.googleads.v9.services.types import conversion_value_rule_service

class ConversionValueRuleServiceTransport(metaclass=abc.ABCMeta):
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
    def get_conversion_value_rule(
        self,
    ) -> typing.Callable[
        [conversion_value_rule_service.GetConversionValueRuleRequest],
        conversion_value_rule.ConversionValueRule,
    ]: ...
    @property
    def mutate_conversion_value_rules(
        self,
    ) -> typing.Callable[
        [conversion_value_rule_service.MutateConversionValueRulesRequest],
        conversion_value_rule_service.MutateConversionValueRulesResponse,
    ]: ...
