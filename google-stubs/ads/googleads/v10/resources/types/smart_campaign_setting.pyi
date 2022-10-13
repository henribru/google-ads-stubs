from typing import Any

import proto

class SmartCampaignSetting(proto.Message):
    class PhoneNumber(proto.Message):
        phone_number: str
        country_code: str
        def __init__(
            self,
            mapping: Any | None = ...,
            *,
            ignore_unknown_fields: bool = ...,
            phone_number: str = ...,
            country_code: str = ...
        ) -> None: ...
    resource_name: str
    campaign: str
    phone_number: SmartCampaignSetting.PhoneNumber
    final_url: str
    advertising_language_code: str
    business_name: str
    business_location_id: int
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        campaign: str = ...,
        phone_number: SmartCampaignSetting.PhoneNumber = ...,
        final_url: str = ...,
        advertising_language_code: str = ...,
        business_name: str = ...,
        business_location_id: int = ...
    ) -> None: ...
