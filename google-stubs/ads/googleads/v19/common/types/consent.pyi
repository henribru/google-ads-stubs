import proto
from _typeshed import Incomplete
from google.ads.googleads.v19.enums.types import consent_status

__protobuf__: Incomplete

class Consent(proto.Message):
    ad_user_data: consent_status.ConsentStatusEnum.ConsentStatus
    ad_personalization: consent_status.ConsentStatusEnum.ConsentStatus
