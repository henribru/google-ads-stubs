import proto
from _typeshed import Incomplete

from google.ads.googleads.v11.enums.types import (
    custom_interest_member_type as custom_interest_member_type,
    custom_interest_status as custom_interest_status,
    custom_interest_type as custom_interest_type,
)

__protobuf__: Incomplete

class CustomInterest(proto.Message):
    resource_name: Incomplete
    id: Incomplete
    status: Incomplete
    name: Incomplete
    type_: Incomplete
    description: Incomplete
    members: Incomplete

class CustomInterestMember(proto.Message):
    member_type: Incomplete
    parameter: Incomplete
