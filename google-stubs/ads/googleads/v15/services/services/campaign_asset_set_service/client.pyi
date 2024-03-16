import types
from typing import Dict, MutableSequence, Sequence, Tuple, Type

from _typeshed import Incomplete
from google.api_core import (
    client_options as client_options_lib,
    gapic_v1,
    retry as retries,
)
from google.auth import credentials as ga_credentials

from google.ads.googleads.v15.services.types import campaign_asset_set_service

from .transports.base import CampaignAssetSetServiceTransport

__all__ = ["CampaignAssetSetServiceClient"]

class CampaignAssetSetServiceClientMeta(type):
    def get_transport_class(
        cls, label: str | None = None
    ) -> type[CampaignAssetSetServiceTransport]: ...

class CampaignAssetSetServiceClient(metaclass=CampaignAssetSetServiceClientMeta):
    DEFAULT_ENDPOINT: str
    DEFAULT_MTLS_ENDPOINT: Incomplete
    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs): ...
    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs): ...
    from_service_account_json = from_service_account_file
    @property
    def transport(self) -> CampaignAssetSetServiceTransport: ...
    def __enter__(self) -> CampaignAssetSetServiceClient: ...
    def __exit__(
        self,
        type: type[BaseException] | None,
        value: BaseException | None,
        traceback: types.TracebackType | None,
    ) -> None: ...
    @staticmethod
    def asset_set_path(customer_id: str, asset_set_id: str) -> str: ...
    @staticmethod
    def parse_asset_set_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def campaign_path(customer_id: str, campaign_id: str) -> str: ...
    @staticmethod
    def parse_campaign_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def campaign_asset_set_path(
        customer_id: str, campaign_id: str, asset_set_id: str
    ) -> str: ...
    @staticmethod
    def parse_campaign_asset_set_path(path: str) -> dict[str, str]: ...
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
        transport: str | CampaignAssetSetServiceTransport | None = None,
        client_options: client_options_lib.ClientOptions | dict | None = None,
        client_info: gapic_v1.client_info.ClientInfo = ...,
    ) -> None: ...
    def mutate_campaign_asset_sets(
        self,
        request: campaign_asset_set_service.MutateCampaignAssetSetsRequest
        | dict
        | None = None,
        *,
        customer_id: str | None = None,
        operations: MutableSequence[
            campaign_asset_set_service.CampaignAssetSetOperation
        ]
        | None = None,
        retry: retries.Retry | gapic_v1.method._MethodDefault = ...,
        timeout: float | object = ...,
        metadata: Sequence[tuple[str, str]] = (),
    ) -> campaign_asset_set_service.MutateCampaignAssetSetsResponse: ...
