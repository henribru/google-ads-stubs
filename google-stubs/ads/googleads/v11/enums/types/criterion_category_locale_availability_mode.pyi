from typing import Any

import proto

class CriterionCategoryLocaleAvailabilityModeEnum(proto.Message):
    class CriterionCategoryLocaleAvailabilityMode(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        ALL_LOCALES = 2
        COUNTRY_AND_ALL_LANGUAGES = 3
        LANGUAGE_AND_ALL_COUNTRIES = 4
        COUNTRY_AND_LANGUAGE = 5
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
