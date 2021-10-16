import abc
import typing
from typing import Any

from google.api_core import gapic_v1
from google.auth import credentials

from google.ads.googleads.v7.resources.types import product_bidding_category_constant
from google.ads.googleads.v7.services.types import (
    product_bidding_category_constant_service,
)

class ProductBiddingCategoryConstantServiceTransport(metaclass=abc.ABCMeta):
    AUTH_SCOPES: Any
    def __init__(
        self,
        *,
        host: str = ...,
        credentials: credentials.Credentials = ...,
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
