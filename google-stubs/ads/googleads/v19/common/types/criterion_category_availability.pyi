from google.ads.googleads.v19.enums.types.criterion_category_locale_availability_mode import CriterionCategoryLocaleAvailabilityModeEnum
from collections.abc import MutableSequence
from google.ads.googleads.v19.enums.types.advertising_channel_sub_type import AdvertisingChannelSubTypeEnum
from google.ads.googleads.v19.enums.types.advertising_channel_type import AdvertisingChannelTypeEnum
from google.ads.googleads.v19.enums.types.criterion_category_channel_availability_mode import CriterionCategoryChannelAvailabilityModeEnum
from collections.abc import MutableSequence
import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class CriterionCategoryAvailability(proto.Message):
    channel: CriterionCategoryChannelAvailability
    locale: MutableSequence[CriterionCategoryLocaleAvailability]
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., channel: CriterionCategoryChannelAvailability = ..., locale: MutableSequence[CriterionCategoryLocaleAvailability] = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["channel", "locale"]) -> bool: ...
class CriterionCategoryChannelAvailability(proto.Message):
    availability_mode: CriterionCategoryChannelAvailabilityModeEnum.CriterionCategoryChannelAvailabilityMode
    advertising_channel_type: AdvertisingChannelTypeEnum.AdvertisingChannelType
    advertising_channel_sub_type: MutableSequence[AdvertisingChannelSubTypeEnum.AdvertisingChannelSubType]
    include_default_channel_sub_type: bool
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., availability_mode: CriterionCategoryChannelAvailabilityModeEnum.CriterionCategoryChannelAvailabilityMode = ..., advertising_channel_type: AdvertisingChannelTypeEnum.AdvertisingChannelType = ..., advertising_channel_sub_type: MutableSequence[AdvertisingChannelSubTypeEnum.AdvertisingChannelSubType] = ..., include_default_channel_sub_type: bool = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["availability_mode", "advertising_channel_type", "advertising_channel_sub_type", "include_default_channel_sub_type"]) -> bool: ...
class CriterionCategoryLocaleAvailability(proto.Message):
    availability_mode: CriterionCategoryLocaleAvailabilityModeEnum.CriterionCategoryLocaleAvailabilityMode
    country_code: str
    language_code: str
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., availability_mode: CriterionCategoryLocaleAvailabilityModeEnum.CriterionCategoryLocaleAvailabilityMode = ..., country_code: str = ..., language_code: str = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["availability_mode", "country_code", "language_code"]) -> bool: ...
