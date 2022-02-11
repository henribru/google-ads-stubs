import abc
import typing
from typing import Any

from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials

from google.ads.googleads.v9.resources.types import ad_group_criterion_label
from google.ads.googleads.v9.services.types import ad_group_criterion_label_service

class AdGroupCriterionLabelServiceTransport(metaclass=abc.ABCMeta):
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
    def get_ad_group_criterion_label(
        self,
    ) -> typing.Callable[
        [ad_group_criterion_label_service.GetAdGroupCriterionLabelRequest],
        ad_group_criterion_label.AdGroupCriterionLabel,
    ]: ...
    @property
    def mutate_ad_group_criterion_labels(
        self,
    ) -> typing.Callable[
        [ad_group_criterion_label_service.MutateAdGroupCriterionLabelsRequest],
        ad_group_criterion_label_service.MutateAdGroupCriterionLabelsResponse,
    ]: ...