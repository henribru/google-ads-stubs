import abc
import typing
from typing import Any

from google.api_core import gapic_v1
from google.auth import credentials

from google.ads.googleads.v7.resources.types import topic_view
from google.ads.googleads.v7.services.types import topic_view_service

class TopicViewServiceTransport(metaclass=abc.ABCMeta):
    AUTH_SCOPES: Any
    def __init__(
        self,
        *,
        host: str = ...,
        credentials: credentials.Credentials = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...
    ) -> None: ...
    @property
    def get_topic_view(
        self,
    ) -> typing.Callable[
        [topic_view_service.GetTopicViewRequest], topic_view.TopicView
    ]: ...
