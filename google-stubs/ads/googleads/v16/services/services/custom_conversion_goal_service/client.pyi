import types
from typing import Dict, MutableSequence, Sequence, Tuple, Type

from _typeshed import Incomplete
from google.api_core import (
    client_options as client_options_lib,
    gapic_v1,
    retry as retries,
)
from google.auth import credentials as ga_credentials

from google.ads.googleads.v16.services.types import custom_conversion_goal_service

from .transports.base import CustomConversionGoalServiceTransport

__all__ = ["CustomConversionGoalServiceClient"]

class CustomConversionGoalServiceClientMeta(type):
    def get_transport_class(
        cls, label: str | None = None
    ) -> type[CustomConversionGoalServiceTransport]: ...

class CustomConversionGoalServiceClient(
    metaclass=CustomConversionGoalServiceClientMeta
):
    DEFAULT_ENDPOINT: str
    DEFAULT_MTLS_ENDPOINT: Incomplete
    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs): ...
    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs): ...
    from_service_account_json = from_service_account_file
    @property
    def transport(self) -> CustomConversionGoalServiceTransport: ...
    def __enter__(self) -> CustomConversionGoalServiceClient: ...
    def __exit__(
        self,
        type: type[BaseException] | None,
        value: BaseException | None,
        traceback: types.TracebackType | None,
    ) -> None: ...
    @staticmethod
    def conversion_action_path(customer_id: str, conversion_action_id: str) -> str: ...
    @staticmethod
    def parse_conversion_action_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def custom_conversion_goal_path(customer_id: str, goal_id: str) -> str: ...
    @staticmethod
    def parse_custom_conversion_goal_path(path: str) -> dict[str, str]: ...
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
        transport: str | CustomConversionGoalServiceTransport | None = None,
        client_options: client_options_lib.ClientOptions | dict | None = None,
        client_info: gapic_v1.client_info.ClientInfo = ...,
    ) -> None: ...
    def mutate_custom_conversion_goals(
        self,
        request: custom_conversion_goal_service.MutateCustomConversionGoalsRequest
        | dict
        | None = None,
        *,
        customer_id: str | None = None,
        operations: MutableSequence[
            custom_conversion_goal_service.CustomConversionGoalOperation
        ]
        | None = None,
        retry: retries.Retry | gapic_v1.method._MethodDefault = ...,
        timeout: float | object = ...,
        metadata: Sequence[tuple[str, str]] = (),
    ) -> custom_conversion_goal_service.MutateCustomConversionGoalsResponse: ...
