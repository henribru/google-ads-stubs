from typing import Dict, MutableSequence, Optional, Sequence, Tuple, Type, Union

from _typeshed import Incomplete
from google.api_core import (
    client_options as client_options_lib,
    gapic_v1,
    retry as retries,
)
from google.auth import credentials as ga_credentials

from google.ads.googleads.v13.services.types import conversion_upload_service

from .transports.base import ConversionUploadServiceTransport

class ConversionUploadServiceClientMeta(type):
    def get_transport_class(
        cls, label: Optional[str] = ...
    ) -> Type[ConversionUploadServiceTransport]: ...

class ConversionUploadServiceClient(metaclass=ConversionUploadServiceClientMeta):
    DEFAULT_ENDPOINT: str
    DEFAULT_MTLS_ENDPOINT: Incomplete
    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs): ...
    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs): ...
    from_service_account_json: Incomplete
    @property
    def transport(self) -> ConversionUploadServiceTransport: ...
    def __enter__(self) -> ConversionUploadServiceClient: ...
    def __exit__(self, type, value, traceback) -> None: ...
    @staticmethod
    def conversion_custom_variable_path(
        customer_id: str, conversion_custom_variable_id: str
    ) -> str: ...
    @staticmethod
    def parse_conversion_custom_variable_path(path: str) -> Dict[str, str]: ...
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
        credentials: Optional[ga_credentials.Credentials] = ...,
        transport: Optional[Union[str, ConversionUploadServiceTransport]] = ...,
        client_options: Optional[Union[client_options_lib.ClientOptions, dict]] = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...
    ) -> None: ...
    def upload_click_conversions(
        self,
        request: Optional[
            Union[conversion_upload_service.UploadClickConversionsRequest, dict]
        ] = ...,
        *,
        customer_id: Optional[str] = ...,
        conversions: Optional[
            MutableSequence[conversion_upload_service.ClickConversion]
        ] = ...,
        partial_failure: Optional[bool] = ...,
        retry: Union[retries.Retry, gapic_v1.method._MethodDefault] = ...,
        timeout: Union[float, object] = ...,
        metadata: Sequence[Tuple[str, str]] = ...
    ) -> conversion_upload_service.UploadClickConversionsResponse: ...
    def upload_call_conversions(
        self,
        request: Optional[
            Union[conversion_upload_service.UploadCallConversionsRequest, dict]
        ] = ...,
        *,
        customer_id: Optional[str] = ...,
        conversions: Optional[
            MutableSequence[conversion_upload_service.CallConversion]
        ] = ...,
        partial_failure: Optional[bool] = ...,
        retry: Union[retries.Retry, gapic_v1.method._MethodDefault] = ...,
        timeout: Union[float, object] = ...,
        metadata: Sequence[Tuple[str, str]] = ...
    ) -> conversion_upload_service.UploadCallConversionsResponse: ...
