import proto
from _typeshed import Incomplete
from google.ads.googleads.v20.common.types import criterion_category_availability
from google.ads.googleads.v20.enums.types import user_interest_taxonomy_type
from typing import MutableSequence

__protobuf__: Incomplete

class UserInterest(proto.Message):
    resource_name: str
    taxonomy_type: user_interest_taxonomy_type.UserInterestTaxonomyTypeEnum.UserInterestTaxonomyType
    user_interest_id: int
    name: str
    user_interest_parent: str
    launched_to_all: bool
    availabilities: MutableSequence[criterion_category_availability.CriterionCategoryAvailability]
