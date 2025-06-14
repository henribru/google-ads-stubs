import proto
from _typeshed import Incomplete
from google.ads.googleads.v19.common.types import user_lists
from google.ads.googleads.v19.enums.types import access_reason as gage_access_reason, user_list_access_status, user_list_closing_reason, user_list_membership_status, user_list_size_range, user_list_type

__protobuf__: Incomplete

class UserList(proto.Message):
    resource_name: str
    id: int
    read_only: bool
    name: str
    description: str
    membership_status: user_list_membership_status.UserListMembershipStatusEnum.UserListMembershipStatus
    integration_code: str
    membership_life_span: int
    size_for_display: int
    size_range_for_display: user_list_size_range.UserListSizeRangeEnum.UserListSizeRange
    size_for_search: int
    size_range_for_search: user_list_size_range.UserListSizeRangeEnum.UserListSizeRange
    type_: user_list_type.UserListTypeEnum.UserListType
    closing_reason: user_list_closing_reason.UserListClosingReasonEnum.UserListClosingReason
    access_reason: gage_access_reason.AccessReasonEnum.AccessReason
    account_user_list_status: user_list_access_status.UserListAccessStatusEnum.UserListAccessStatus
    eligible_for_search: bool
    eligible_for_display: bool
    match_rate_percentage: int
    crm_based_user_list: user_lists.CrmBasedUserListInfo
    similar_user_list: user_lists.SimilarUserListInfo
    rule_based_user_list: user_lists.RuleBasedUserListInfo
    logical_user_list: user_lists.LogicalUserListInfo
    basic_user_list: user_lists.BasicUserListInfo
    lookalike_user_list: user_lists.LookalikeUserListInfo
