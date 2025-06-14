import proto
from _typeshed import Incomplete
from google.ads.googleads.v20.common.types import criterion_category_availability
from typing import MutableSequence

__protobuf__: Incomplete

class LifeEvent(proto.Message):
    resource_name: str
    id: int
    name: str
    parent: str
    launched_to_all: bool
    availabilities: MutableSequence[criterion_category_availability.CriterionCategoryAvailability]
