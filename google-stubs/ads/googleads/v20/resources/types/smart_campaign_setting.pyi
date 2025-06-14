import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class SmartCampaignSetting(proto.Message):
    class PhoneNumber(proto.Message):
        phone_number: str
        country_code: str
    class AdOptimizedBusinessProfileSetting(proto.Message):
        include_lead_form: bool
    resource_name: str
    campaign: str
    phone_number: PhoneNumber
    advertising_language_code: str
    final_url: str
    ad_optimized_business_profile_setting: AdOptimizedBusinessProfileSetting
    business_name: str
    business_profile_location: str
