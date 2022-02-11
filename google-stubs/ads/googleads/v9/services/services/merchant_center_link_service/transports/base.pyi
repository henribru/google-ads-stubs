import abc
import typing
from typing import Any

from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials

from google.ads.googleads.v9.resources.types import merchant_center_link
from google.ads.googleads.v9.services.types import merchant_center_link_service

class MerchantCenterLinkServiceTransport(metaclass=abc.ABCMeta):
    AUTH_SCOPES: Any
    def __init__(
        self,
        *,
        host: str = ...,
        credentials: ga_credentials.Credentials = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...
    ) -> None: ...
    def close(self) -> None: ...
    @property
    def list_merchant_center_links(
        self,
    ) -> typing.Callable[
        [merchant_center_link_service.ListMerchantCenterLinksRequest],
        merchant_center_link_service.ListMerchantCenterLinksResponse,
    ]: ...
    @property
    def get_merchant_center_link(
        self,
    ) -> typing.Callable[
        [merchant_center_link_service.GetMerchantCenterLinkRequest],
        merchant_center_link.MerchantCenterLink,
    ]: ...
    @property
    def mutate_merchant_center_link(
        self,
    ) -> typing.Callable[
        [merchant_center_link_service.MutateMerchantCenterLinkRequest],
        merchant_center_link_service.MutateMerchantCenterLinkResponse,
    ]: ...
