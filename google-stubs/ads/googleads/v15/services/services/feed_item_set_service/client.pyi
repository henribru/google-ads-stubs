from typing import Dict, MutableSequence, Optional, Sequence, Tuple, Type, Union

from _typeshed import Incomplete
from google.api_core import (
    client_options as client_options_lib,
    gapic_v1,
    retry as retries,
)
from google.auth import credentials as ga_credentials

from google.ads.googleads.v15.services.types import feed_item_set_service

from .transports.base import FeedItemSetServiceTransport

class FeedItemSetServiceClientMeta(type):
    def get_transport_class(
        cls, label: str | None = None
    ) -> type[FeedItemSetServiceTransport]: ...

class FeedItemSetServiceClient(metaclass=FeedItemSetServiceClientMeta):
    DEFAULT_ENDPOINT: str
    DEFAULT_MTLS_ENDPOINT: Incomplete
    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs): ...
    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs): ...
    from_service_account_json = from_service_account_file
    @property
    def transport(self) -> FeedItemSetServiceTransport: ...
    def __enter__(self) -> FeedItemSetServiceClient: ...
    def __exit__(self, type, value, traceback) -> None: ...
    @staticmethod
    def feed_path(customer_id: str, feed_id: str) -> str: ...
    @staticmethod
    def parse_feed_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def feed_item_set_path(
        customer_id: str, feed_id: str, feed_item_set_id: str
    ) -> str: ...
    @staticmethod
    def parse_feed_item_set_path(path: str) -> dict[str, str]: ...
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
        transport: str | FeedItemSetServiceTransport | None = None,
        client_options: client_options_lib.ClientOptions | dict | None = None,
        client_info: gapic_v1.client_info.ClientInfo = ...
    ) -> None: ...
    def mutate_feed_item_sets(
        self,
        request: feed_item_set_service.MutateFeedItemSetsRequest | dict | None = None,
        *,
        customer_id: str | None = None,
        operations: MutableSequence[feed_item_set_service.FeedItemSetOperation]
        | None = None,
        retry: retries.Retry | gapic_v1.method._MethodDefault = ...,
        timeout: float | object = ...,
        metadata: Sequence[tuple[str, str]] = ()
    ) -> feed_item_set_service.MutateFeedItemSetsResponse: ...
