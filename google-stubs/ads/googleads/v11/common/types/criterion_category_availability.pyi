from typing import Any

import proto

from google.ads.googleads.v11.enums.types.advertising_channel_sub_type import (
    AdvertisingChannelSubTypeEnum,
)
from google.ads.googleads.v11.enums.types.advertising_channel_type import (
    AdvertisingChannelTypeEnum,
)
from google.ads.googleads.v11.enums.types.criterion_category_channel_availability_mode import (
    CriterionCategoryChannelAvailabilityModeEnum,
)
from google.ads.googleads.v11.enums.types.criterion_category_locale_availability_mode import (
    CriterionCategoryLocaleAvailabilityModeEnum,
)

class CriterionCategoryAvailability(proto.Message):
    channel: CriterionCategoryChannelAvailability
    locale: list[CriterionCategoryLocaleAvailability]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        channel: CriterionCategoryChannelAvailability = ...,
        locale: list[CriterionCategoryLocaleAvailability] = ...
    ) -> None: ...

class CriterionCategoryChannelAvailability(proto.Message):
    availability_mode: CriterionCategoryChannelAvailabilityModeEnum.CriterionCategoryChannelAvailabilityMode
    advertising_channel_type: AdvertisingChannelTypeEnum.AdvertisingChannelType
    advertising_channel_sub_type: list[
        AdvertisingChannelSubTypeEnum.AdvertisingChannelSubType
    ]
    include_default_channel_sub_type: bool
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        availability_mode: CriterionCategoryChannelAvailabilityModeEnum.CriterionCategoryChannelAvailabilityMode = ...,
        advertising_channel_type: AdvertisingChannelTypeEnum.AdvertisingChannelType = ...,
        advertising_channel_sub_type: list[
            AdvertisingChannelSubTypeEnum.AdvertisingChannelSubType
        ] = ...,
        include_default_channel_sub_type: bool = ...
    ) -> None: ...

class CriterionCategoryLocaleAvailability(proto.Message):
    availability_mode: CriterionCategoryLocaleAvailabilityModeEnum.CriterionCategoryLocaleAvailabilityMode
    country_code: str
    language_code: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        availability_mode: CriterionCategoryLocaleAvailabilityModeEnum.CriterionCategoryLocaleAvailabilityMode = ...,
        country_code: str = ...,
        language_code: str = ...
    ) -> None: ...
