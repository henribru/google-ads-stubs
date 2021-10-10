import abc
import typing
from typing import Any

from google.api_core import gapic_v1
from google.auth import credentials

from google.ads.googleads.v7.resources.types import user_list
from google.ads.googleads.v7.services.types import user_list_service

class UserListServiceTransport(metaclass=abc.ABCMeta):
    AUTH_SCOPES: Any
    def __init__(
        self,
        *,
        host: str = ...,
        credentials: credentials.Credentials = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...
    ) -> None: ...
    @property
    def get_user_list(
        self,
    ) -> typing.Callable[
        [user_list_service.GetUserListRequest], user_list.UserList
    ]: ...
    @property
    def mutate_user_lists(
        self,
    ) -> typing.Callable[
        [user_list_service.MutateUserListsRequest],
        user_list_service.MutateUserListsResponse,
    ]: ...
