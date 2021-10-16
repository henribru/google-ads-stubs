import abc
import typing
from typing import Any

from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials

from google.ads.googleads.v8.resources.types import product_bidding_category_constant
from google.ads.googleads.v8.services.types import (
    product_bidding_category_constant_service,
)

class ProductBiddingCategoryConstantServiceTransport(metaclass=abc.ABCMeta):
    AUTH_SCOPES: Any
    def __init__(
        self,
        *,
        host: str = ...,
        credentials: ga_credentials.Credentials = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...
    ) -> None: ...
    @property
    def get_product_bidding_category_constant(
        self,
    ) -> typing.Callable[
        [
            product_bidding_category_constant_service.GetProductBiddingCategoryConstantRequest
        ],
        product_bidding_category_constant.ProductBiddingCategoryConstant,
    ]: ...
