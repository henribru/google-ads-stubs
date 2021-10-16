from typing import Any

import proto

from google.ads.googleads.v8.enums.types import (
    custom_audience_member_type as custom_audience_member_type,
    custom_audience_status as custom_audience_status,
    custom_audience_type as custom_audience_type,
)

__protobuf__: Any

class CustomAudience(proto.Message):
    resource_name: Any
    id: Any
    status: Any
    name: Any
    type_: Any
    description: Any
    members: Any

class CustomAudienceMember(proto.Message):
    member_type: Any
    keyword: Any
    url: Any
    place_category: Any
    app: Any
