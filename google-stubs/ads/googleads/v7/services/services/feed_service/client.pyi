from typing import Any, Dict, Optional, Sequence, Tuple, Type, Union

from google.api_core import (
    client_options as client_options_lib,
    gapic_v1,
    retry as retries,
)
from google.auth import credentials

from google.ads.googleads.v7.resources.types import feed
from google.ads.googleads.v7.services.types import feed_service

from .transports.base import FeedServiceTransport

class FeedServiceClientMeta(type):
    def get_transport_class(cls, label: str = ...) -> Type[FeedServiceTransport]: ...

class FeedServiceClient(metaclass=FeedServiceClientMeta):
    DEFAULT_ENDPOINT: str
    DEFAULT_MTLS_ENDPOINT: Any
    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs): ...
    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs): ...
    from_service_account_json: Any
    @property
    def transport(self) -> FeedServiceTransport: ...
    @staticmethod
    def feed_path(customer_id: str, feed_id: str) -> str: ...
    @staticmethod
    def parse_feed_path(path: str) -> Dict[str, str]: ...
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
        credentials: Optional[credentials.Credentials] = ...,
        transport: Union[str, FeedServiceTransport, None] = ...,
        client_options: Optional[client_options_lib.ClientOptions] = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...
    ) -> None: ...
    def get_feed(
        self,
        request: feed_service.GetFeedRequest = ...,
        *,
        resource_name: str = ...,
        retry: retries.Retry = ...,
        timeout: float = ...,
        metadata: Sequence[Tuple[str, str]] = ...
    ) -> feed.Feed: ...
    def mutate_feeds(
        self,
        request: feed_service.MutateFeedsRequest = ...,
        *,
        customer_id: str = ...,
        operations: Sequence[feed_service.FeedOperation] = ...,
        retry: retries.Retry = ...,
        timeout: float = ...,
        metadata: Sequence[Tuple[str, str]] = ...
    ) -> feed_service.MutateFeedsResponse: ...
