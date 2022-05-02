import proto
from _typeshed import Incomplete

from google.ads.googleads.v10.common.types import user_lists as user_lists
from google.ads.googleads.v10.enums.types import (
    user_list_access_status as user_list_access_status,
    user_list_closing_reason as user_list_closing_reason,
    user_list_membership_status as user_list_membership_status,
    user_list_size_range as user_list_size_range,
    user_list_type as user_list_type,
)

__protobuf__: Incomplete

class UserList(proto.Message):
    resource_name: Incomplete
    id: Incomplete
    read_only: Incomplete
    name: Incomplete
    description: Incomplete
    membership_status: Incomplete
    integration_code: Incomplete
    membership_life_span: Incomplete
    size_for_display: Incomplete
    size_range_for_display: Incomplete
    size_for_search: Incomplete
    size_range_for_search: Incomplete
    type_: Incomplete
    closing_reason: Incomplete
    access_reason: Incomplete
    account_user_list_status: Incomplete
    eligible_for_search: Incomplete
    eligible_for_display: Incomplete
    match_rate_percentage: Incomplete
    crm_based_user_list: Incomplete
    similar_user_list: Incomplete
    rule_based_user_list: Incomplete
    logical_user_list: Incomplete
    basic_user_list: Incomplete
