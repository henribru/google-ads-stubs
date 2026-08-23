from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v25.enums.types.conversion_action_category import (
    ConversionActionCategoryEnum,
)
from google.ads.googleads.v25.enums.types.conversion_origin import ConversionOriginEnum

_M = TypeVar("_M")

class EffectiveAutomaticGoal(proto.Message):
    category: ConversionActionCategoryEnum.ConversionActionCategory
    origin: ConversionOriginEnum.ConversionOrigin
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        category: ConversionActionCategoryEnum.ConversionActionCategory = ...,
        origin: ConversionOriginEnum.ConversionOrigin = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["category", "origin"]
    ) -> bool: ...
