from typing import Any

import proto

from google.ads.googleads.v9.enums.types import (
    geo_target_constant_status as geo_target_constant_status,
)

__protobuf__: Any

class GeoTargetConstant(proto.Message):
    resource_name: Any
    id: Any
    name: Any
    country_code: Any
    target_type: Any
    status: Any
    canonical_name: Any
    parent_geo_target: Any
