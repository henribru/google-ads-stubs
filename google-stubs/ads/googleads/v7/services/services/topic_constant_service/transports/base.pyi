import abc
import typing
from typing import Any

from google.api_core import gapic_v1
from google.auth import credentials

from google.ads.googleads.v7.resources.types import topic_constant
from google.ads.googleads.v7.services.types import topic_constant_service

class TopicConstantServiceTransport(metaclass=abc.ABCMeta):
    AUTH_SCOPES: Any
    def __init__(
        self,
        *,
        host: str = ...,
        credentials: credentials.Credentials = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...
    ) -> None: ...
    @property
    def get_topic_constant(
        self,
    ) -> typing.Callable[
        [topic_constant_service.GetTopicConstantRequest], topic_constant.TopicConstant
    ]: ...
