import types
from typing import Dict, Sequence, Tuple, Type

from _typeshed import Incomplete
from google.api_core import (
    client_options as client_options_lib,
    gapic_v1,
    retry as retries,
)
from google.auth import credentials as ga_credentials

from google.ads.googleads.v16.enums.types import identity_verification_program
from google.ads.googleads.v16.services.types import identity_verification_service

from .transports.base import IdentityVerificationServiceTransport

__all__ = ["IdentityVerificationServiceClient"]

class IdentityVerificationServiceClientMeta(type):
    def get_transport_class(
        cls, label: str | None = None
    ) -> type[IdentityVerificationServiceTransport]: ...

class IdentityVerificationServiceClient(
    metaclass=IdentityVerificationServiceClientMeta
):
    DEFAULT_ENDPOINT: str
    DEFAULT_MTLS_ENDPOINT: Incomplete
    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs): ...
    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs): ...
    from_service_account_json = from_service_account_file
    @property
    def transport(self) -> IdentityVerificationServiceTransport: ...
    def __enter__(self) -> IdentityVerificationServiceClient: ...
    def __exit__(
        self,
        type: type[BaseException] | None,
        value: BaseException | None,
        traceback: types.TracebackType | None,
    ) -> None: ...
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
        transport: str | IdentityVerificationServiceTransport | None = None,
        client_options: client_options_lib.ClientOptions | dict | None = None,
        client_info: gapic_v1.client_info.ClientInfo = ...,
    ) -> None: ...
    def start_identity_verification(
        self,
        request: identity_verification_service.StartIdentityVerificationRequest
        | dict
        | None = None,
        *,
        customer_id: str | None = None,
        verification_program: identity_verification_program.IdentityVerificationProgramEnum.IdentityVerificationProgram
        | None = None,
        retry: retries.Retry | gapic_v1.method._MethodDefault = ...,
        timeout: float | object = ...,
        metadata: Sequence[tuple[str, str]] = (),
    ) -> None: ...
    def get_identity_verification(
        self,
        request: identity_verification_service.GetIdentityVerificationRequest
        | dict
        | None = None,
        *,
        customer_id: str | None = None,
        retry: retries.Retry | gapic_v1.method._MethodDefault = ...,
        timeout: float | object = ...,
        metadata: Sequence[tuple[str, str]] = (),
    ) -> identity_verification_service.GetIdentityVerificationResponse: ...
