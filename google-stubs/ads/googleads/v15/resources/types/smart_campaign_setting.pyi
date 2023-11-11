from typing import Any

import proto

class SmartCampaignSetting(proto.Message):
    class AdOptimizedBusinessProfileSetting(proto.Message):
        include_lead_form: bool
        def __init__(
            self,
            mapping: Any | None = ...,
            *,
            ignore_unknown_fields: bool = ...,
            include_lead_form: bool = ...
        ) -> None: ...

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
    advertising_language_code: str
    final_url: str
    ad_optimized_business_profile_setting: SmartCampaignSetting.AdOptimizedBusinessProfileSetting
    business_name: str
    business_profile_location: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        campaign: str = ...,
        phone_number: SmartCampaignSetting.PhoneNumber = ...,
        advertising_language_code: str = ...,
        final_url: str = ...,
        ad_optimized_business_profile_setting: SmartCampaignSetting.AdOptimizedBusinessProfileSetting = ...,
        business_name: str = ...,
        business_profile_location: str = ...
    ) -> None: ...
