from typing import Any

import proto

from google.ads.googleads.v9.enums.types import (
    custom_conversion_goal_status as custom_conversion_goal_status,
)

__protobuf__: Any

class CustomConversionGoal(proto.Message):
    resource_name: Any
    id: Any
    name: Any
    conversion_actions: Any
    status: Any
