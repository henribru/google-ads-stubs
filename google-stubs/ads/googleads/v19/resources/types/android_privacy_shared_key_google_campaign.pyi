import proto
from _typeshed import Incomplete
from google.ads.googleads.v19.enums.types import android_privacy_interaction_type as gage_android_privacy_interaction_type

__protobuf__: Incomplete

class AndroidPrivacySharedKeyGoogleCampaign(proto.Message):
    resource_name: str
    campaign_id: int
    android_privacy_interaction_type: gage_android_privacy_interaction_type.AndroidPrivacyInteractionTypeEnum.AndroidPrivacyInteractionType
    android_privacy_interaction_date: str
    shared_campaign_key: str
