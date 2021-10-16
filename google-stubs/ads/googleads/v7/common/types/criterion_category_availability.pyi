from typing import Any

import proto

from google.ads.googleads.v7.enums.types import (
    criterion_category_channel_availability_mode as criterion_category_channel_availability_mode,
    criterion_category_locale_availability_mode as criterion_category_locale_availability_mode,
)

__protobuf__: Any

class CriterionCategoryAvailability(proto.Message):
    channel: Any
    locale: Any

class CriterionCategoryChannelAvailability(proto.Message):
    availability_mode: Any
    advertising_channel_type: Any
    advertising_channel_sub_type: Any
    include_default_channel_sub_type: Any

class CriterionCategoryLocaleAvailability(proto.Message):
    availability_mode: Any
    country_code: Any
    language_code: Any
