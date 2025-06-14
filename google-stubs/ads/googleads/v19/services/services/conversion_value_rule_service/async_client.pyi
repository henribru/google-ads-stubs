from typing import Callable, MutableSequence, Sequence, Tuple

from _typeshed import Incomplete
from google.api_core import gapic_v1, retry_async as retries
from google.api_core.client_options import ClientOptions
from google.auth import credentials as ga_credentials

from google.ads.googleads.v19.services.types import conversion_value_rule_service

from .transports.base import ConversionValueRuleServiceTransport

__all__ = ["ConversionValueRuleServiceAsyncClient"]

class ConversionValueRuleServiceAsyncClient:
    DEFAULT_ENDPOINT: Incomplete
    DEFAULT_MTLS_ENDPOINT: Incomplete
    conversion_value_rule_path: Incomplete
    parse_conversion_value_rule_path: Incomplete
    customer_path: Incomplete
    parse_customer_path: Incomplete
    geo_target_constant_path: Incomplete
    parse_geo_target_constant_path: Incomplete
    user_interest_path: Incomplete
    parse_user_interest_path: Incomplete
    user_list_path: Incomplete
    parse_user_list_path: Incomplete
    common_billing_account_path: Incomplete
    parse_common_billing_account_path: Incomplete
    common_folder_path: Incomplete
    parse_common_folder_path: Incomplete
    common_organization_path: Incomplete
    parse_common_organization_path: Incomplete
    common_project_path: Incomplete
    parse_common_project_path: Incomplete
    common_location_path: Incomplete
    parse_common_location_path: Incomplete
    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs): ...
    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs): ...
    from_service_account_json = from_service_account_file
    @classmethod
    def get_mtls_endpoint_and_cert_source(
        cls, client_options: ClientOptions | None = None
    ): ...
    @property
    def transport(self) -> ConversionValueRuleServiceTransport: ...
    @property
    def api_endpoint(self): ...
    @property
    def universe_domain(self) -> str: ...
    get_transport_class: Incomplete
    def __init__(
        self,
        *,
        credentials: ga_credentials.Credentials | None = None,
        transport: str
        | ConversionValueRuleServiceTransport
        | Callable[..., ConversionValueRuleServiceTransport]
        | None = "grpc_asyncio",
        client_options: ClientOptions | None = None,
        client_info: gapic_v1.client_info.ClientInfo = ...,
    ) -> None: ...
    async def mutate_conversion_value_rules(
        self,
        request: conversion_value_rule_service.MutateConversionValueRulesRequest
        | dict
        | None = None,
        *,
        customer_id: str | None = None,
        operations: MutableSequence[
            conversion_value_rule_service.ConversionValueRuleOperation
        ]
        | None = None,
        retry: retries.AsyncRetry | gapic_v1.method._MethodDefault = ...,
        timeout: float | object = ...,
        metadata: Sequence[tuple[str, str | bytes]] = (),
    ) -> conversion_value_rule_service.MutateConversionValueRulesResponse: ...
    async def __aenter__(self) -> ConversionValueRuleServiceAsyncClient: ...
    async def __aexit__(self, exc_type, exc, tb) -> None: ...
