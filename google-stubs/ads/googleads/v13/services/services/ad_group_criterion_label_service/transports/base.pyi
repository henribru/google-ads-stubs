import abc
from typing import Awaitable, Callable, Optional, Sequence, Union

from _typeshed import Incomplete
from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials

from google.ads.googleads.v13.services.types import ad_group_criterion_label_service

class AdGroupCriterionLabelServiceTransport(abc.ABC):
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
    def mutate_ad_group_criterion_labels(
        self,
    ) -> Callable[
        [ad_group_criterion_label_service.MutateAdGroupCriterionLabelsRequest],
        Union[
            ad_group_criterion_label_service.MutateAdGroupCriterionLabelsResponse,
            Awaitable[
                ad_group_criterion_label_service.MutateAdGroupCriterionLabelsResponse
            ],
        ],
    ]: ...
