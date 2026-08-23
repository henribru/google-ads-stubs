from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class CriterionCategoryLocaleAvailabilityModeEnum(proto.Message):
    class CriterionCategoryLocaleAvailabilityMode(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        ALL_LOCALES = 2
        COUNTRY_AND_ALL_LANGUAGES = 3
        LANGUAGE_AND_ALL_COUNTRIES = 4
        COUNTRY_AND_LANGUAGE = 5

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...
