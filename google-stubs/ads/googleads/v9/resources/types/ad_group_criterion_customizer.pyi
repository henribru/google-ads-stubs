from typing import Any

import proto

from google.ads.googleads.v9.common.types import customizer_value as customizer_value
from google.ads.googleads.v9.enums.types import (
    customizer_value_status as customizer_value_status,
)

__protobuf__: Any

class AdGroupCriterionCustomizer(proto.Message):
    resource_name: Any
    ad_group_criterion: Any
    customizer_attribute: Any
    status: Any
    value: Any
