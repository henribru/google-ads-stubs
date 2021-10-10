from typing import Any

import proto

from google.ads.googleads.v7.common.types import (
    criterion_category_availability as criterion_category_availability,
)
from google.ads.googleads.v7.enums.types import (
    user_interest_taxonomy_type as user_interest_taxonomy_type,
)

__protobuf__: Any

class UserInterest(proto.Message):
    resource_name: Any
    taxonomy_type: Any
    user_interest_id: Any
    name: Any
    user_interest_parent: Any
    launched_to_all: Any
    availabilities: Any
