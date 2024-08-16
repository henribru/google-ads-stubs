import types
from typing import Dict, MutableSequence, Sequence, Tuple, Type

from _typeshed import Incomplete
from google.api_core import (
    client_options as client_options_lib,
    gapic_v1,
    retry as retries,
)
from google.auth import credentials as ga_credentials

from google.ads.googleads.v17.services.types import user_list_customer_type_service

from .transports.base import UserListCustomerTypeServiceTransport

__all__ = ["UserListCustomerTypeServiceClient"]

class UserListCustomerTypeServiceClientMeta(type):
    def get_transport_class(
        cls, label: str | None = None
    ) -> type[UserListCustomerTypeServiceTransport]: ...

class UserListCustomerTypeServiceClient(
    metaclass=UserListCustomerTypeServiceClientMeta
):
    DEFAULT_ENDPOINT: str
    DEFAULT_MTLS_ENDPOINT: Incomplete
    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs): ...
    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs): ...
    from_service_account_json = from_service_account_file
    @property
    def transport(self) -> UserListCustomerTypeServiceTransport: ...
    def __enter__(self) -> UserListCustomerTypeServiceClient: ...
    def __exit__(
        self,
        type: type[BaseException] | None,
        value: BaseException | None,
        traceback: types.TracebackType | None,
    ) -> None: ...
    @staticmethod
    def user_list_path(customer_id: str, user_list_id: str) -> str: ...
    @staticmethod
    def parse_user_list_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def user_list_customer_type_path(
        customer_id: str, user_list_id: str, semantic_label: str
    ) -> str: ...
    @staticmethod
    def parse_user_list_customer_type_path(path: str) -> dict[str, str]: ...
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
        transport: str | UserListCustomerTypeServiceTransport | None = None,
        client_options: client_options_lib.ClientOptions | dict | None = None,
        client_info: gapic_v1.client_info.ClientInfo = ...,
    ) -> None: ...
    def mutate_user_list_customer_types(
        self,
        request: user_list_customer_type_service.MutateUserListCustomerTypesRequest
        | dict
        | None = None,
        *,
        customer_id: str | None = None,
        operations: MutableSequence[
            user_list_customer_type_service.UserListCustomerTypeOperation
        ]
        | None = None,
        retry: retries.Retry | gapic_v1.method._MethodDefault = ...,
        timeout: float | object = ...,
        metadata: Sequence[tuple[str, str]] = (),
    ) -> user_list_customer_type_service.MutateUserListCustomerTypesResponse: ...
