import types
from typing import Dict, MutableSequence, Sequence, Tuple, Type

from _typeshed import Incomplete
from google.api_core import (
    client_options as client_options_lib,
    gapic_v1,
    retry as retries,
)
from google.auth import credentials as ga_credentials

from google.ads.googleads.v14.services.types import conversion_upload_service

from .transports.base import ConversionUploadServiceTransport

__all__ = ["ConversionUploadServiceClient"]

class ConversionUploadServiceClientMeta(type):
    def get_transport_class(
        cls, label: str | None = None
    ) -> type[ConversionUploadServiceTransport]: ...

class ConversionUploadServiceClient(metaclass=ConversionUploadServiceClientMeta):
    DEFAULT_ENDPOINT: str
    DEFAULT_MTLS_ENDPOINT: Incomplete
    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs): ...
    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs): ...
    from_service_account_json = from_service_account_file
    @property
    def transport(self) -> ConversionUploadServiceTransport: ...
    def __enter__(self) -> ConversionUploadServiceClient: ...
    def __exit__(
        self,
        type: type[BaseException] | None,
        value: BaseException | None,
        traceback: types.TracebackType | None,
    ) -> None: ...
    @staticmethod
    def conversion_custom_variable_path(
        customer_id: str, conversion_custom_variable_id: str
    ) -> str: ...
    @staticmethod
    def parse_conversion_custom_variable_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def common_billing_account_path(billing_account: str) -> str: ...
    @staticmethod
    def parse_common_billing_account_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def common_folder_path(folder: str) -> str: ...
    @staticmethod
    def parse_common_folder_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def common_organization_path(organization: str) -> str: ...
    @staticmethod
    def parse_common_organization_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def common_project_path(project: str) -> str: ...
    @staticmethod
    def parse_common_project_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def common_location_path(project: str, location: str) -> str: ...
    @staticmethod
    def parse_common_location_path(path: str) -> dict[str, str]: ...
    def __init__(
        self,
        *,
        credentials: ga_credentials.Credentials | None = None,
        transport: str | ConversionUploadServiceTransport | None = None,
        client_options: client_options_lib.ClientOptions | dict | None = None,
        client_info: gapic_v1.client_info.ClientInfo = ...,
    ) -> None: ...
    def upload_click_conversions(
        self,
        request: conversion_upload_service.UploadClickConversionsRequest
        | dict
        | None = None,
        *,
        customer_id: str | None = None,
        conversions: MutableSequence[conversion_upload_service.ClickConversion]
        | None = None,
        partial_failure: bool | None = None,
        retry: retries.Retry | gapic_v1.method._MethodDefault = ...,
        timeout: float | object = ...,
        metadata: Sequence[tuple[str, str]] = (),
    ) -> conversion_upload_service.UploadClickConversionsResponse: ...
    def upload_call_conversions(
        self,
        request: conversion_upload_service.UploadCallConversionsRequest
        | dict
        | None = None,
        *,
        customer_id: str | None = None,
        conversions: MutableSequence[conversion_upload_service.CallConversion]
        | None = None,
        partial_failure: bool | None = None,
        retry: retries.Retry | gapic_v1.method._MethodDefault = ...,
        timeout: float | object = ...,
        metadata: Sequence[tuple[str, str]] = (),
    ) -> conversion_upload_service.UploadCallConversionsResponse: ...
