import abc
import typing
from typing import Any

from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials

from google.ads.googleads.v8.resources.types import label
from google.ads.googleads.v8.services.types import label_service

class LabelServiceTransport(metaclass=abc.ABCMeta):
    AUTH_SCOPES: Any
    def __init__(
        self,
        *,
        host: str = ...,
        credentials: ga_credentials.Credentials = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...
    ) -> None: ...
    @property
    def get_label(
        self,
    ) -> typing.Callable[[label_service.GetLabelRequest], label.Label]: ...
    @property
    def mutate_labels(
        self,
    ) -> typing.Callable[
        [label_service.MutateLabelsRequest], label_service.MutateLabelsResponse
    ]: ...
