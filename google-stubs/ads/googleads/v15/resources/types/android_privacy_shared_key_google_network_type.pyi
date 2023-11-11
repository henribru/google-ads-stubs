from typing import Any

import proto

from google.ads.googleads.v15.enums.types.android_privacy_interaction_type import (
    AndroidPrivacyInteractionTypeEnum,
)
from google.ads.googleads.v15.enums.types.android_privacy_network_type import (
    AndroidPrivacyNetworkTypeEnum,
)

class AndroidPrivacySharedKeyGoogleNetworkType(proto.Message):
    resource_name: str
    campaign_id: int
    android_privacy_interaction_type: AndroidPrivacyInteractionTypeEnum.AndroidPrivacyInteractionType
    android_privacy_interaction_date: str
    android_privacy_network_type: AndroidPrivacyNetworkTypeEnum.AndroidPrivacyNetworkType
    shared_network_type_key: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        campaign_id: int = ...,
        android_privacy_interaction_type: AndroidPrivacyInteractionTypeEnum.AndroidPrivacyInteractionType = ...,
        android_privacy_interaction_date: str = ...,
        android_privacy_network_type: AndroidPrivacyNetworkTypeEnum.AndroidPrivacyNetworkType = ...,
        shared_network_type_key: str = ...
    ) -> None: ...
