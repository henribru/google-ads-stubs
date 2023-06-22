import abc
from typing import Awaitable, Callable, Optional, Sequence, Union

from _typeshed import Incomplete
from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials

from google.ads.googleads.v14.services.types import conversion_custom_variable_service

class ConversionCustomVariableServiceTransport(abc.ABC):
    AUTH_SCOPES: Incomplete
    DEFAULT_HOST: str
    def __init__(
        self,
        *,
        host: str = ...,
        credentials: Optional[ga_credentials.Credentials] = ...,
        credentials_file: Optional[str] = ...,
        scopes: Optional[Sequence[str]] = ...,
        quota_project_id: Optional[str] = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...,
        always_use_jwt_access: Optional[bool] = ...,
        **kwargs
    ) -> None: ...
    def close(self) -> None: ...
    @property
    def mutate_conversion_custom_variables(
        self,
    ) -> Callable[
        [conversion_custom_variable_service.MutateConversionCustomVariablesRequest],
        Union[
            conversion_custom_variable_service.MutateConversionCustomVariablesResponse,
            Awaitable[
                conversion_custom_variable_service.MutateConversionCustomVariablesResponse
            ],
        ],
    ]: ...
