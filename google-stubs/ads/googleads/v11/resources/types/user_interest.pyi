from typing import Any

import proto

from google.ads.googleads.v11.common.types.criterion_category_availability import (
    CriterionCategoryAvailability,
)
from google.ads.googleads.v11.enums.types.user_interest_taxonomy_type import (
    UserInterestTaxonomyTypeEnum,
)

class UserInterest(proto.Message):
    resource_name: str
    taxonomy_type: UserInterestTaxonomyTypeEnum.UserInterestTaxonomyType
    user_interest_id: int
    name: str
    user_interest_parent: str
    launched_to_all: bool
    availabilities: list[CriterionCategoryAvailability]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        taxonomy_type: UserInterestTaxonomyTypeEnum.UserInterestTaxonomyType = ...,
        user_interest_id: int = ...,
        name: str = ...,
        user_interest_parent: str = ...,
        launched_to_all: bool = ...,
        availabilities: list[CriterionCategoryAvailability] = ...
    ) -> None: ...
