import types
from typing import Dict, MutableSequence, Sequence, Tuple, Type

from _typeshed import Incomplete
from google.api_core import (
    client_options as client_options_lib,
    gapic_v1,
    retry as retries,
)
from google.auth import credentials as ga_credentials

from google.ads.googleads.v16.enums.types import (
    advertising_channel_type as gage_advertising_channel_type,
    recommendation_type,
)
from google.ads.googleads.v16.services.types import recommendation_service

from .transports.base import RecommendationServiceTransport

__all__ = ["RecommendationServiceClient"]

class RecommendationServiceClientMeta(type):
    def get_transport_class(
        cls, label: str | None = None
    ) -> type[RecommendationServiceTransport]: ...

class RecommendationServiceClient(metaclass=RecommendationServiceClientMeta):
    DEFAULT_ENDPOINT: str
    DEFAULT_MTLS_ENDPOINT: Incomplete
    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs): ...
    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs): ...
    from_service_account_json = from_service_account_file
    @property
    def transport(self) -> RecommendationServiceTransport: ...
    def __enter__(self) -> RecommendationServiceClient: ...
    def __exit__(
        self,
        type: type[BaseException] | None,
        value: BaseException | None,
        traceback: types.TracebackType | None,
    ) -> None: ...
    @staticmethod
    def ad_path(customer_id: str, ad_id: str) -> str: ...
    @staticmethod
    def parse_ad_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def ad_group_path(customer_id: str, ad_group_id: str) -> str: ...
    @staticmethod
    def parse_ad_group_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def asset_path(customer_id: str, asset_id: str) -> str: ...
    @staticmethod
    def parse_asset_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def campaign_path(customer_id: str, campaign_id: str) -> str: ...
    @staticmethod
    def parse_campaign_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def campaign_budget_path(customer_id: str, campaign_budget_id: str) -> str: ...
    @staticmethod
    def parse_campaign_budget_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def conversion_action_path(customer_id: str, conversion_action_id: str) -> str: ...
    @staticmethod
    def parse_conversion_action_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def recommendation_path(customer_id: str, recommendation_id: str) -> str: ...
    @staticmethod
    def parse_recommendation_path(path: str) -> dict[str, str]: ...
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
        transport: str | RecommendationServiceTransport | None = None,
        client_options: client_options_lib.ClientOptions | dict | None = None,
        client_info: gapic_v1.client_info.ClientInfo = ...,
    ) -> None: ...
    def apply_recommendation(
        self,
        request: recommendation_service.ApplyRecommendationRequest | dict | None = None,
        *,
        customer_id: str | None = None,
        operations: MutableSequence[recommendation_service.ApplyRecommendationOperation]
        | None = None,
        retry: retries.Retry | gapic_v1.method._MethodDefault = ...,
        timeout: float | object = ...,
        metadata: Sequence[tuple[str, str]] = (),
    ) -> recommendation_service.ApplyRecommendationResponse: ...
    def dismiss_recommendation(
        self,
        request: recommendation_service.DismissRecommendationRequest
        | dict
        | None = None,
        *,
        customer_id: str | None = None,
        operations: MutableSequence[
            recommendation_service.DismissRecommendationRequest.DismissRecommendationOperation
        ]
        | None = None,
        retry: retries.Retry | gapic_v1.method._MethodDefault = ...,
        timeout: float | object = ...,
        metadata: Sequence[tuple[str, str]] = (),
    ) -> recommendation_service.DismissRecommendationResponse: ...
    def generate_recommendations(
        self,
        request: recommendation_service.GenerateRecommendationsRequest
        | dict
        | None = None,
        *,
        customer_id: str | None = None,
        recommendation_types: MutableSequence[
            recommendation_type.RecommendationTypeEnum.RecommendationType
        ]
        | None = None,
        advertising_channel_type: gage_advertising_channel_type.AdvertisingChannelTypeEnum.AdvertisingChannelType
        | None = None,
        retry: retries.Retry | gapic_v1.method._MethodDefault = ...,
        timeout: float | object = ...,
        metadata: Sequence[tuple[str, str]] = (),
    ) -> recommendation_service.GenerateRecommendationsResponse: ...
