from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class SmartCampaignSetting(proto.Message):
    class AdOptimizedBusinessProfileSetting(proto.Message):
        include_lead_form: bool
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
            include_lead_form: bool = ...,
        ) -> None: ...
        def __contains__(  # type: ignore[override]
            self, key: Literal["include_lead_form"]
        ) -> bool: ...

    class PhoneNumber(proto.Message):
        phone_number: str
        country_code: str
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
            phone_number: str = ...,
            country_code: str = ...,
        ) -> None: ...
        def __contains__(  # type: ignore[override]
            self, key: Literal["phone_number", "country_code"]
        ) -> bool: ...

    resource_name: str
    campaign: str
    phone_number: SmartCampaignSetting.PhoneNumber
    advertising_language_code: str
    final_url: str
    ad_optimized_business_profile_setting: (
        SmartCampaignSetting.AdOptimizedBusinessProfileSetting
    )
    business_name: str
    business_profile_location: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        campaign: str = ...,
        phone_number: SmartCampaignSetting.PhoneNumber = ...,
        advertising_language_code: str = ...,
        final_url: str = ...,
        ad_optimized_business_profile_setting: SmartCampaignSetting.AdOptimizedBusinessProfileSetting = ...,
        business_name: str = ...,
        business_profile_location: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "resource_name",
            "campaign",
            "phone_number",
            "advertising_language_code",
            "final_url",
            "ad_optimized_business_profile_setting",
            "business_name",
            "business_profile_location",
        ],
    ) -> bool: ...
