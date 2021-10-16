import abc
import typing
from typing import Any

from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials

from google.ads.googleads.v8.resources.types import domain_category
from google.ads.googleads.v8.services.types import domain_category_service

class DomainCategoryServiceTransport(metaclass=abc.ABCMeta):
    AUTH_SCOPES: Any
    def __init__(
        self,
        *,
        host: str = ...,
        credentials: ga_credentials.Credentials = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...
    ) -> None: ...
    @property
    def get_domain_category(
        self,
    ) -> typing.Callable[
        [domain_category_service.GetDomainCategoryRequest],
        domain_category.DomainCategory,
    ]: ...
