import proto
from _typeshed import Incomplete

from google.ads.googleads.v10.enums.types import (
    custom_audience_member_type as custom_audience_member_type,
    custom_audience_status as custom_audience_status,
    custom_audience_type as custom_audience_type,
)

__protobuf__: Incomplete

class CustomAudience(proto.Message):
    resource_name: Incomplete
    id: Incomplete
    status: Incomplete
    name: Incomplete
    type_: Incomplete
    description: Incomplete
    members: Incomplete

class CustomAudienceMember(proto.Message):
    member_type: Incomplete
    keyword: Incomplete
    url: Incomplete
    place_category: Incomplete
    app: Incomplete
