import abc
import typing
from typing import Any

from google.api_core import gapic_v1
from google.auth import credentials

from google.ads.googleads.v7.resources.types import ad_group_ad_label
from google.ads.googleads.v7.services.types import ad_group_ad_label_service

class AdGroupAdLabelServiceTransport(metaclass=abc.ABCMeta):
    AUTH_SCOPES: Any
    def __init__(
        self,
        *,
        host: str = ...,
        credentials: credentials.Credentials = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...
    ) -> None: ...
    @property
    def get_ad_group_ad_label(
        self,
    ) -> typing.Callable[
        [ad_group_ad_label_service.GetAdGroupAdLabelRequest],
        ad_group_ad_label.AdGroupAdLabel,
    ]: ...
    @property
    def mutate_ad_group_ad_labels(
        self,
    ) -> typing.Callable[
        [ad_group_ad_label_service.MutateAdGroupAdLabelsRequest],
        ad_group_ad_label_service.MutateAdGroupAdLabelsResponse,
    ]: ...
