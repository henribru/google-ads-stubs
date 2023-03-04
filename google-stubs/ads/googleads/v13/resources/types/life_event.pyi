from collections.abc import MutableSequence
from typing import Any

import proto

from google.ads.googleads.v13.common.types.criterion_category_availability import (
    CriterionCategoryAvailability,
)

class LifeEvent(proto.Message):
    resource_name: str
    id: int
    name: str
    parent: str
    launched_to_all: bool
    availabilities: MutableSequence[CriterionCategoryAvailability]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        id: int = ...,
        name: str = ...,
        parent: str = ...,
        launched_to_all: bool = ...,
        availabilities: MutableSequence[CriterionCategoryAvailability] = ...
    ) -> None: ...
