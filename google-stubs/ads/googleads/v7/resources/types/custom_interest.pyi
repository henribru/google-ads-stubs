from typing import Any

import proto

from google.ads.googleads.v7.enums.types import (
    custom_interest_member_type as custom_interest_member_type,
    custom_interest_status as custom_interest_status,
    custom_interest_type as custom_interest_type,
)

__protobuf__: Any

class CustomInterest(proto.Message):
    resource_name: Any
    id: Any
    status: Any
    name: Any
    type_: Any
    description: Any
    members: Any

class CustomInterestMember(proto.Message):
    member_type: Any
    parameter: Any
