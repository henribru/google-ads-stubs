import proto
from _typeshed import Incomplete
from google.ads.googleads.v20.enums.types import advertising_channel_sub_type as gage_advertising_channel_sub_type, advertising_channel_type as gage_advertising_channel_type, criterion_category_channel_availability_mode, criterion_category_locale_availability_mode
from typing import MutableSequence

__protobuf__: Incomplete

class CriterionCategoryAvailability(proto.Message):
    channel: CriterionCategoryChannelAvailability
    locale: MutableSequence['CriterionCategoryLocaleAvailability']

class CriterionCategoryChannelAvailability(proto.Message):
    availability_mode: criterion_category_channel_availability_mode.CriterionCategoryChannelAvailabilityModeEnum.CriterionCategoryChannelAvailabilityMode
    advertising_channel_type: gage_advertising_channel_type.AdvertisingChannelTypeEnum.AdvertisingChannelType
    advertising_channel_sub_type: MutableSequence[gage_advertising_channel_sub_type.AdvertisingChannelSubTypeEnum.AdvertisingChannelSubType]
    include_default_channel_sub_type: bool

class CriterionCategoryLocaleAvailability(proto.Message):
    availability_mode: criterion_category_locale_availability_mode.CriterionCategoryLocaleAvailabilityModeEnum.CriterionCategoryLocaleAvailabilityMode
    country_code: str
    language_code: str
