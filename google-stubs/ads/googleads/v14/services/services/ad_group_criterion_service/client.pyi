import types
from typing import Dict, MutableSequence, Sequence, Tuple, Type

from _typeshed import Incomplete
from google.api_core import (
    client_options as client_options_lib,
    gapic_v1,
    retry as retries,
)
from google.auth import credentials as ga_credentials

from google.ads.googleads.v14.services.types import ad_group_criterion_service

from .transports.base import AdGroupCriterionServiceTransport

__all__ = ["AdGroupCriterionServiceClient"]

class AdGroupCriterionServiceClientMeta(type):
    def get_transport_class(
        cls, label: str | None = None
    ) -> type[AdGroupCriterionServiceTransport]: ...

class AdGroupCriterionServiceClient(metaclass=AdGroupCriterionServiceClientMeta):
    DEFAULT_ENDPOINT: str
    DEFAULT_MTLS_ENDPOINT: Incomplete
    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs): ...
    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs): ...
    from_service_account_json = from_service_account_file
    @property
    def transport(self) -> AdGroupCriterionServiceTransport: ...
    def __enter__(self) -> AdGroupCriterionServiceClient: ...
    def __exit__(
        self,
        type: type[BaseException] | None,
        value: BaseException | None,
        traceback: types.TracebackType | None,
    ) -> None: ...
    @staticmethod
    def ad_group_path(customer_id: str, ad_group_id: str) -> str: ...
    @staticmethod
    def parse_ad_group_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def ad_group_criterion_path(
        customer_id: str, ad_group_id: str, criterion_id: str
    ) -> str: ...
    @staticmethod
    def parse_ad_group_criterion_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def ad_group_criterion_label_path(
        customer_id: str, ad_group_id: str, criterion_id: str, label_id: str
    ) -> str: ...
    @staticmethod
    def parse_ad_group_criterion_label_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def combined_audience_path(customer_id: str, combined_audience_id: str) -> str: ...
    @staticmethod
    def parse_combined_audience_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def mobile_app_category_constant_path(mobile_app_category_id: str) -> str: ...
    @staticmethod
    def parse_mobile_app_category_constant_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def topic_constant_path(topic_id: str) -> str: ...
    @staticmethod
    def parse_topic_constant_path(path: str) -> dict[str, str]: ...
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
        transport: str | AdGroupCriterionServiceTransport | None = None,
        client_options: client_options_lib.ClientOptions | dict | None = None,
        client_info: gapic_v1.client_info.ClientInfo = ...,
    ) -> None: ...
    def mutate_ad_group_criteria(
        self,
        request: ad_group_criterion_service.MutateAdGroupCriteriaRequest
        | dict
        | None = None,
        *,
        customer_id: str | None = None,
        operations: MutableSequence[
            ad_group_criterion_service.AdGroupCriterionOperation
        ]
        | None = None,
        retry: retries.Retry | gapic_v1.method._MethodDefault = ...,
        timeout: float | object = ...,
        metadata: Sequence[tuple[str, str]] = (),
    ) -> ad_group_criterion_service.MutateAdGroupCriteriaResponse: ...
