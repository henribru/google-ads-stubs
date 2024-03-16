from collections.abc import Mapping, MutableSequence
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v14.common.types.criterion_category_availability import (
    CriterionCategoryAvailability,
)
from google.ads.googleads.v14.enums.types.user_interest_taxonomy_type import (
    UserInterestTaxonomyTypeEnum,
)

_M = TypeVar("_M")

class UserInterest(proto.Message):
    resource_name: str
    taxonomy_type: UserInterestTaxonomyTypeEnum.UserInterestTaxonomyType
    user_interest_id: int
    name: str
    user_interest_parent: str
    launched_to_all: bool
    availabilities: MutableSequence[CriterionCategoryAvailability]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        taxonomy_type: UserInterestTaxonomyTypeEnum.UserInterestTaxonomyType = ...,
        user_interest_id: int = ...,
        name: str = ...,
        user_interest_parent: str = ...,
        launched_to_all: bool = ...,
        availabilities: MutableSequence[CriterionCategoryAvailability] = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "resource_name",
            "taxonomy_type",
            "user_interest_id",
            "name",
            "user_interest_parent",
            "launched_to_all",
            "availabilities",
        ],
    ) -> bool: ...
