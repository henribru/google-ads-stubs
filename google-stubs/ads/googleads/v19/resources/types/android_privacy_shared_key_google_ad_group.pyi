from google.ads.googleads.v19.enums.types.android_privacy_network_type import AndroidPrivacyNetworkTypeEnum
from google.ads.googleads.v19.enums.types.android_privacy_interaction_type import AndroidPrivacyInteractionTypeEnum
import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class AndroidPrivacySharedKeyGoogleAdGroup(proto.Message):
    resource_name: str
    campaign_id: int
    android_privacy_interaction_type: AndroidPrivacyInteractionTypeEnum.AndroidPrivacyInteractionType
    android_privacy_interaction_date: str
    android_privacy_network_type: AndroidPrivacyNetworkTypeEnum.AndroidPrivacyNetworkType
    ad_group_id: int
    shared_ad_group_key: str
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, resource_name: str = ..., campaign_id: int = ..., android_privacy_interaction_type: AndroidPrivacyInteractionTypeEnum.AndroidPrivacyInteractionType = ..., android_privacy_interaction_date: str = ..., android_privacy_network_type: AndroidPrivacyNetworkTypeEnum.AndroidPrivacyNetworkType = ..., ad_group_id: int = ..., shared_ad_group_key: str = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["resource_name", "campaign_id", "android_privacy_interaction_type", "android_privacy_interaction_date", "android_privacy_network_type", "ad_group_id", "shared_ad_group_key"]) -> bool: ...
