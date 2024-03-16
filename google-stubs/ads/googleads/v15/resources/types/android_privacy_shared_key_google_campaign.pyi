from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v15.enums.types.android_privacy_interaction_type import (
    AndroidPrivacyInteractionTypeEnum,
)

_M = TypeVar("_M")

class AndroidPrivacySharedKeyGoogleCampaign(proto.Message):
    resource_name: str
    campaign_id: int
    android_privacy_interaction_type: (
        AndroidPrivacyInteractionTypeEnum.AndroidPrivacyInteractionType
    )
    android_privacy_interaction_date: str
    shared_campaign_key: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        campaign_id: int = ...,
        android_privacy_interaction_type: AndroidPrivacyInteractionTypeEnum.AndroidPrivacyInteractionType = ...,
        android_privacy_interaction_date: str = ...,
        shared_campaign_key: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "resource_name",
            "campaign_id",
            "android_privacy_interaction_type",
            "android_privacy_interaction_date",
            "shared_campaign_key",
        ],
    ) -> bool: ...
