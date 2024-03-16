import types
from typing import Dict, MutableSequence, Sequence, Tuple, Type

from _typeshed import Incomplete
from google.api_core import (
    client_options as client_options_lib,
    gapic_v1,
    retry as retries,
)
from google.auth import credentials as ga_credentials

from google.ads.googleads.v14.services.types import (
    ad_group_criterion_customizer_service,
)

from .transports.base import AdGroupCriterionCustomizerServiceTransport

__all__ = ["AdGroupCriterionCustomizerServiceClient"]

class AdGroupCriterionCustomizerServiceClientMeta(type):
    def get_transport_class(
        cls, label: str | None = None
    ) -> type[AdGroupCriterionCustomizerServiceTransport]: ...

class AdGroupCriterionCustomizerServiceClient(
    metaclass=AdGroupCriterionCustomizerServiceClientMeta
):
    DEFAULT_ENDPOINT: str
    DEFAULT_MTLS_ENDPOINT: Incomplete
    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs): ...
    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs): ...
    from_service_account_json = from_service_account_file
    @property
    def transport(self) -> AdGroupCriterionCustomizerServiceTransport: ...
    def __enter__(self) -> AdGroupCriterionCustomizerServiceClient: ...
    def __exit__(
        self,
        type: type[BaseException] | None,
        value: BaseException | None,
        traceback: types.TracebackType | None,
    ) -> None: ...
    @staticmethod
    def ad_group_criterion_path(
        customer_id: str, ad_group_id: str, criterion_id: str
    ) -> str: ...
    @staticmethod
    def parse_ad_group_criterion_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def ad_group_criterion_customizer_path(
        customer_id: str,
        ad_group_id: str,
        criterion_id: str,
        customizer_attribute_id: str,
    ) -> str: ...
    @staticmethod
    def parse_ad_group_criterion_customizer_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def customizer_attribute_path(
        customer_id: str, customizer_attribute_id: str
    ) -> str: ...
    @staticmethod
    def parse_customizer_attribute_path(path: str) -> dict[str, str]: ...
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
        transport: str | AdGroupCriterionCustomizerServiceTransport | None = None,
        client_options: client_options_lib.ClientOptions | dict | None = None,
        client_info: gapic_v1.client_info.ClientInfo = ...,
    ) -> None: ...
    def mutate_ad_group_criterion_customizers(
        self,
        request: ad_group_criterion_customizer_service.MutateAdGroupCriterionCustomizersRequest
        | dict
        | None = None,
        *,
        customer_id: str | None = None,
        operations: MutableSequence[
            ad_group_criterion_customizer_service.AdGroupCriterionCustomizerOperation
        ]
        | None = None,
        retry: retries.Retry | gapic_v1.method._MethodDefault = ...,
        timeout: float | object = ...,
        metadata: Sequence[tuple[str, str]] = (),
    ) -> (
        ad_group_criterion_customizer_service.MutateAdGroupCriterionCustomizersResponse
    ): ...
