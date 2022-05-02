import proto
from _typeshed import Incomplete

from google.ads.googleads.v10.enums.types import (
    criterion_category_channel_availability_mode as criterion_category_channel_availability_mode,
    criterion_category_locale_availability_mode as criterion_category_locale_availability_mode,
)

__protobuf__: Incomplete

class CriterionCategoryAvailability(proto.Message):
    channel: Incomplete
    locale: Incomplete

class CriterionCategoryChannelAvailability(proto.Message):
    availability_mode: Incomplete
    advertising_channel_type: Incomplete
    advertising_channel_sub_type: Incomplete
    include_default_channel_sub_type: Incomplete

class CriterionCategoryLocaleAvailability(proto.Message):
    availability_mode: Incomplete
    country_code: Incomplete
    language_code: Incomplete
