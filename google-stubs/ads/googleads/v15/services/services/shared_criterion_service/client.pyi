from typing import Dict, MutableSequence, Optional, Sequence, Tuple, Type, Union

from _typeshed import Incomplete
from google.api_core import (
    client_options as client_options_lib,
    gapic_v1,
    retry as retries,
)
from google.auth import credentials as ga_credentials

from google.ads.googleads.v15.services.types import shared_criterion_service

from .transports.base import SharedCriterionServiceTransport

class SharedCriterionServiceClientMeta(type):
    def get_transport_class(
        cls, label: str | None = None
    ) -> type[SharedCriterionServiceTransport]: ...

class SharedCriterionServiceClient(metaclass=SharedCriterionServiceClientMeta):
    DEFAULT_ENDPOINT: str
    DEFAULT_MTLS_ENDPOINT: Incomplete
    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs): ...
    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs): ...
    from_service_account_json = from_service_account_file
    @property
    def transport(self) -> SharedCriterionServiceTransport: ...
    def __enter__(self) -> SharedCriterionServiceClient: ...
    def __exit__(self, type, value, traceback) -> None: ...
    @staticmethod
    def mobile_app_category_constant_path(mobile_app_category_id: str) -> str: ...
    @staticmethod
    def parse_mobile_app_category_constant_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def shared_criterion_path(
        customer_id: str, shared_set_id: str, criterion_id: str
    ) -> str: ...
    @staticmethod
    def parse_shared_criterion_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def shared_set_path(customer_id: str, shared_set_id: str) -> str: ...
    @staticmethod
    def parse_shared_set_path(path: str) -> dict[str, str]: ...
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
        transport: str | SharedCriterionServiceTransport | None = None,
        client_options: client_options_lib.ClientOptions | dict | None = None,
        client_info: gapic_v1.client_info.ClientInfo = ...
    ) -> None: ...
    def mutate_shared_criteria(
        self,
        request: shared_criterion_service.MutateSharedCriteriaRequest
        | dict
        | None = None,
        *,
        customer_id: str | None = None,
        operations: MutableSequence[shared_criterion_service.SharedCriterionOperation]
        | None = None,
        retry: retries.Retry | gapic_v1.method._MethodDefault = ...,
        timeout: float | object = ...,
        metadata: Sequence[tuple[str, str]] = ()
    ) -> shared_criterion_service.MutateSharedCriteriaResponse: ...
