import proto
from _typeshed import Incomplete
from google.ads.googleads.v20.enums.types import android_privacy_interaction_type as gage_android_privacy_interaction_type, android_privacy_network_type as gage_android_privacy_network_type

__protobuf__: Incomplete

class AndroidPrivacySharedKeyGoogleNetworkType(proto.Message):
    resource_name: str
    campaign_id: int
    android_privacy_interaction_type: gage_android_privacy_interaction_type.AndroidPrivacyInteractionTypeEnum.AndroidPrivacyInteractionType
    android_privacy_interaction_date: str
    android_privacy_network_type: gage_android_privacy_network_type.AndroidPrivacyNetworkTypeEnum.AndroidPrivacyNetworkType
    shared_network_type_key: str
