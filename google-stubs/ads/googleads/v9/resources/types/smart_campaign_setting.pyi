from typing import Any

import proto

__protobuf__: Any

class SmartCampaignSetting(proto.Message):
    class PhoneNumber(proto.Message):
        phone_number: Any
        country_code: Any
    resource_name: Any
    campaign: Any
    phone_number: Any
    final_url: Any
    advertising_language_code: Any
    business_name: Any
    business_location_id: Any
