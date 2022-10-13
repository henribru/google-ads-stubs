from typing import Any

import proto

from google.ads.googleads.v11.common.types.user_lists import (
    BasicUserListInfo,
    CrmBasedUserListInfo,
    LogicalUserListInfo,
    RuleBasedUserListInfo,
    SimilarUserListInfo,
)
from google.ads.googleads.v11.enums.types.access_reason import AccessReasonEnum
from google.ads.googleads.v11.enums.types.user_list_access_status import (
    UserListAccessStatusEnum,
)
from google.ads.googleads.v11.enums.types.user_list_closing_reason import (
    UserListClosingReasonEnum,
)
from google.ads.googleads.v11.enums.types.user_list_membership_status import (
    UserListMembershipStatusEnum,
)
from google.ads.googleads.v11.enums.types.user_list_size_range import (
    UserListSizeRangeEnum,
)
from google.ads.googleads.v11.enums.types.user_list_type import UserListTypeEnum

class UserList(proto.Message):
    resource_name: str
    id: int
    read_only: bool
    name: str
    description: str
    membership_status: UserListMembershipStatusEnum.UserListMembershipStatus
    integration_code: str
    membership_life_span: int
    size_for_display: int
    size_range_for_display: UserListSizeRangeEnum.UserListSizeRange
    size_for_search: int
    size_range_for_search: UserListSizeRangeEnum.UserListSizeRange
    type_: UserListTypeEnum.UserListType
    closing_reason: UserListClosingReasonEnum.UserListClosingReason
    access_reason: AccessReasonEnum.AccessReason
    account_user_list_status: UserListAccessStatusEnum.UserListAccessStatus
    eligible_for_search: bool
    eligible_for_display: bool
    match_rate_percentage: int
    crm_based_user_list: CrmBasedUserListInfo
    similar_user_list: SimilarUserListInfo
    rule_based_user_list: RuleBasedUserListInfo
    logical_user_list: LogicalUserListInfo
    basic_user_list: BasicUserListInfo
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        id: int = ...,
        read_only: bool = ...,
        name: str = ...,
        description: str = ...,
        membership_status: UserListMembershipStatusEnum.UserListMembershipStatus = ...,
        integration_code: str = ...,
        membership_life_span: int = ...,
        size_for_display: int = ...,
        size_range_for_display: UserListSizeRangeEnum.UserListSizeRange = ...,
        size_for_search: int = ...,
        size_range_for_search: UserListSizeRangeEnum.UserListSizeRange = ...,
        type_: UserListTypeEnum.UserListType = ...,
        closing_reason: UserListClosingReasonEnum.UserListClosingReason = ...,
        access_reason: AccessReasonEnum.AccessReason = ...,
        account_user_list_status: UserListAccessStatusEnum.UserListAccessStatus = ...,
        eligible_for_search: bool = ...,
        eligible_for_display: bool = ...,
        match_rate_percentage: int = ...,
        crm_based_user_list: CrmBasedUserListInfo = ...,
        similar_user_list: SimilarUserListInfo = ...,
        rule_based_user_list: RuleBasedUserListInfo = ...,
        logical_user_list: LogicalUserListInfo = ...,
        basic_user_list: BasicUserListInfo = ...
    ) -> None: ...
