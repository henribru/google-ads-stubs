from typing import Any

import proto

from google.ads.googleads.v9.common.types import user_lists as user_lists
from google.ads.googleads.v9.enums.types import (
    user_list_access_status as user_list_access_status,
    user_list_closing_reason as user_list_closing_reason,
    user_list_membership_status as user_list_membership_status,
    user_list_size_range as user_list_size_range,
    user_list_type as user_list_type,
)

__protobuf__: Any

class UserList(proto.Message):
    resource_name: Any
    id: Any
    read_only: Any
    name: Any
    description: Any
    membership_status: Any
    integration_code: Any
    membership_life_span: Any
    size_for_display: Any
    size_range_for_display: Any
    size_for_search: Any
    size_range_for_search: Any
    type_: Any
    closing_reason: Any
    access_reason: Any
    account_user_list_status: Any
    eligible_for_search: Any
    eligible_for_display: Any
    match_rate_percentage: Any
    crm_based_user_list: Any
    similar_user_list: Any
    rule_based_user_list: Any
    logical_user_list: Any
    basic_user_list: Any
