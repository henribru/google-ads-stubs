from collections.abc import Mapping, MutableSequence
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v16.common.types.criterion_category_availability import (
    CriterionCategoryAvailability,
)

_M = TypeVar("_M")

class LifeEvent(proto.Message):
    resource_name: str
    id: int
    name: str
    parent: str
    launched_to_all: bool
    availabilities: MutableSequence[CriterionCategoryAvailability]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        id: int = ...,
        name: str = ...,
        parent: str = ...,
        launched_to_all: bool = ...,
        availabilities: MutableSequence[CriterionCategoryAvailability] = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "resource_name", "id", "name", "parent", "launched_to_all", "availabilities"
        ],
    ) -> bool: ...
