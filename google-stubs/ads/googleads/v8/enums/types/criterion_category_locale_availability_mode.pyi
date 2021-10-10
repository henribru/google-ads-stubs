from typing import Any

import proto

__protobuf__: Any

class CriterionCategoryLocaleAvailabilityModeEnum(proto.Message):
    class CriterionCategoryLocaleAvailabilityMode(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        ALL_LOCALES: int
        COUNTRY_AND_ALL_LANGUAGES: int
        LANGUAGE_AND_ALL_COUNTRIES: int
        COUNTRY_AND_LANGUAGE: int
