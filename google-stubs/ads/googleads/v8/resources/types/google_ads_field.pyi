from typing import Any

import proto

from google.ads.googleads.v8.enums.types import (
    google_ads_field_category as google_ads_field_category,
    google_ads_field_data_type as google_ads_field_data_type,
)

__protobuf__: Any

class GoogleAdsField(proto.Message):
    resource_name: Any
    name: Any
    category: Any
    selectable: Any
    filterable: Any
    sortable: Any
    selectable_with: Any
    attribute_resources: Any
    metrics: Any
    segments: Any
    enum_values: Any
    data_type: Any
    type_url: Any
    is_repeated: Any
