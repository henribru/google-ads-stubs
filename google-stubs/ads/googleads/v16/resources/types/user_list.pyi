from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v16.common.types.user_lists import (
    BasicUserListInfo,
    CrmBasedUserListInfo,
    LogicalUserListInfo,
    LookalikeUserListInfo,
    RuleBasedUserListInfo,
    SimilarUserListInfo,
)
from google.ads.googleads.v16.enums.types.access_reason import AccessReasonEnum
from google.ads.googleads.v16.enums.types.user_list_access_status import (
    UserListAccessStatusEnum,
)
from google.ads.googleads.v16.enums.types.user_list_closing_reason import (
    UserListClosingReasonEnum,
)
from google.ads.googleads.v16.enums.types.user_list_membership_status import (
    UserListMembershipStatusEnum,
)
from google.ads.googleads.v16.enums.types.user_list_size_range import (
    UserListSizeRangeEnum,
)
from google.ads.googleads.v16.enums.types.user_list_type import UserListTypeEnum

_M = TypeVar("_M")

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
    lookalike_user_list: LookalikeUserListInfo
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
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
        basic_user_list: BasicUserListInfo = ...,
        lookalike_user_list: LookalikeUserListInfo = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "resource_name",
            "id",
            "read_only",
            "name",
            "description",
            "membership_status",
            "integration_code",
            "membership_life_span",
            "size_for_display",
            "size_range_for_display",
            "size_for_search",
            "size_range_for_search",
            "type_",
            "closing_reason",
            "access_reason",
            "account_user_list_status",
            "eligible_for_search",
            "eligible_for_display",
            "match_rate_percentage",
            "crm_based_user_list",
            "similar_user_list",
            "rule_based_user_list",
            "logical_user_list",
            "basic_user_list",
            "lookalike_user_list",
        ],
    ) -> bool: ...
