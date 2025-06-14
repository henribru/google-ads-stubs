import proto
from _typeshed import Incomplete
from google.ads.googleads.v18.common.types import criterion_category_availability
from typing import MutableSequence

__protobuf__: Incomplete

class DetailedDemographic(proto.Message):
    resource_name: str
    id: int
    name: str
    parent: str
    launched_to_all: bool
    availabilities: MutableSequence[criterion_category_availability.CriterionCategoryAvailability]
