from typing import Any, Dict, Optional, Sequence, Tuple, Type, Union

from google.api_core import (
    client_options as client_options_lib,
    gapic_v1,
    retry as retries,
)
from google.auth import credentials

from google.ads.googleads.v7.resources.types import conversion_custom_variable
from google.ads.googleads.v7.services.types import conversion_custom_variable_service

from .transports.base import ConversionCustomVariableServiceTransport

class ConversionCustomVariableServiceClientMeta(type):
    def get_transport_class(
        cls, label: str = ...
    ) -> Type[ConversionCustomVariableServiceTransport]: ...

class ConversionCustomVariableServiceClient(
    metaclass=ConversionCustomVariableServiceClientMeta
):
    DEFAULT_ENDPOINT: str
    DEFAULT_MTLS_ENDPOINT: Any
    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs): ...
    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs): ...
    from_service_account_json: Any
    @property
    def transport(self) -> ConversionCustomVariableServiceTransport: ...
    @staticmethod
    def conversion_custom_variable_path(
        customer_id: str, conversion_custom_variable_id: str
    ) -> str: ...
    @staticmethod
    def parse_conversion_custom_variable_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def customer_path(customer_id: str) -> str: ...
    @staticmethod
    def parse_customer_path(path: str) -> Dict[str, str]: ...
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
        transport: Union[str, ConversionCustomVariableServiceTransport, None] = ...,
        client_options: Optional[client_options_lib.ClientOptions] = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...
    ) -> None: ...
    def get_conversion_custom_variable(
        self,
        request: conversion_custom_variable_service.GetConversionCustomVariableRequest = ...,
        *,
        resource_name: str = ...,
        retry: retries.Retry = ...,
        timeout: float = ...,
        metadata: Sequence[Tuple[str, str]] = ...
    ) -> conversion_custom_variable.ConversionCustomVariable: ...
    def mutate_conversion_custom_variables(
        self,
        request: conversion_custom_variable_service.MutateConversionCustomVariablesRequest = ...,
        *,
        customer_id: str = ...,
        operations: Sequence[
            conversion_custom_variable_service.ConversionCustomVariableOperation
        ] = ...,
        retry: retries.Retry = ...,
        timeout: float = ...,
        metadata: Sequence[Tuple[str, str]] = ...
    ) -> conversion_custom_variable_service.MutateConversionCustomVariablesResponse: ...