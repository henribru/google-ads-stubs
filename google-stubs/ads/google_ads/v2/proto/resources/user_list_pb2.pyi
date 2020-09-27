# @generated by mypy-protobuf.  Do not edit manually!
import sys
from typing import Optional as typing___Optional, Text as typing___Text

from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    FileDescriptor as google___protobuf___descriptor___FileDescriptor,
)
from google.protobuf.message import Message as google___protobuf___message___Message
from google.protobuf.wrappers_pb2 import (
    BoolValue as google___protobuf___wrappers_pb2___BoolValue,
    Int64Value as google___protobuf___wrappers_pb2___Int64Value,
    StringValue as google___protobuf___wrappers_pb2___StringValue,
)
from typing_extensions import Literal as typing_extensions___Literal

from google.ads.google_ads.v2.proto.common.user_lists_pb2 import (
    BasicUserListInfo as google___ads___googleads___v2___common___user_lists_pb2___BasicUserListInfo,
    CrmBasedUserListInfo as google___ads___googleads___v2___common___user_lists_pb2___CrmBasedUserListInfo,
    LogicalUserListInfo as google___ads___googleads___v2___common___user_lists_pb2___LogicalUserListInfo,
    RuleBasedUserListInfo as google___ads___googleads___v2___common___user_lists_pb2___RuleBasedUserListInfo,
    SimilarUserListInfo as google___ads___googleads___v2___common___user_lists_pb2___SimilarUserListInfo,
)
from google.ads.google_ads.v2.proto.enums.access_reason_pb2 import (
    AccessReasonEnum as google___ads___googleads___v2___enums___access_reason_pb2___AccessReasonEnum,
)
from google.ads.google_ads.v2.proto.enums.user_list_access_status_pb2 import (
    UserListAccessStatusEnum as google___ads___googleads___v2___enums___user_list_access_status_pb2___UserListAccessStatusEnum,
)
from google.ads.google_ads.v2.proto.enums.user_list_closing_reason_pb2 import (
    UserListClosingReasonEnum as google___ads___googleads___v2___enums___user_list_closing_reason_pb2___UserListClosingReasonEnum,
)
from google.ads.google_ads.v2.proto.enums.user_list_membership_status_pb2 import (
    UserListMembershipStatusEnum as google___ads___googleads___v2___enums___user_list_membership_status_pb2___UserListMembershipStatusEnum,
)
from google.ads.google_ads.v2.proto.enums.user_list_size_range_pb2 import (
    UserListSizeRangeEnum as google___ads___googleads___v2___enums___user_list_size_range_pb2___UserListSizeRangeEnum,
)
from google.ads.google_ads.v2.proto.enums.user_list_type_pb2 import (
    UserListTypeEnum as google___ads___googleads___v2___enums___user_list_type_pb2___UserListTypeEnum,
)

builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int

DESCRIPTOR: google___protobuf___descriptor___FileDescriptor = ...

class UserList(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    resource_name: typing___Text = ...
    membership_status: google___ads___googleads___v2___enums___user_list_membership_status_pb2___UserListMembershipStatusEnum.UserListMembershipStatusValue = ...
    size_range_for_display: google___ads___googleads___v2___enums___user_list_size_range_pb2___UserListSizeRangeEnum.UserListSizeRangeValue = ...
    size_range_for_search: google___ads___googleads___v2___enums___user_list_size_range_pb2___UserListSizeRangeEnum.UserListSizeRangeValue = ...
    type: google___ads___googleads___v2___enums___user_list_type_pb2___UserListTypeEnum.UserListTypeValue = ...
    closing_reason: google___ads___googleads___v2___enums___user_list_closing_reason_pb2___UserListClosingReasonEnum.UserListClosingReasonValue = ...
    access_reason: google___ads___googleads___v2___enums___access_reason_pb2___AccessReasonEnum.AccessReasonValue = ...
    account_user_list_status: google___ads___googleads___v2___enums___user_list_access_status_pb2___UserListAccessStatusEnum.UserListAccessStatusValue = ...
    @property
    def id(self) -> google___protobuf___wrappers_pb2___Int64Value: ...
    @property
    def read_only(self) -> google___protobuf___wrappers_pb2___BoolValue: ...
    @property
    def name(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def description(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def integration_code(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def membership_life_span(self) -> google___protobuf___wrappers_pb2___Int64Value: ...
    @property
    def size_for_display(self) -> google___protobuf___wrappers_pb2___Int64Value: ...
    @property
    def size_for_search(self) -> google___protobuf___wrappers_pb2___Int64Value: ...
    @property
    def eligible_for_search(self) -> google___protobuf___wrappers_pb2___BoolValue: ...
    @property
    def eligible_for_display(self) -> google___protobuf___wrappers_pb2___BoolValue: ...
    @property
    def crm_based_user_list(
        self,
    ) -> google___ads___googleads___v2___common___user_lists_pb2___CrmBasedUserListInfo: ...
    @property
    def similar_user_list(
        self,
    ) -> google___ads___googleads___v2___common___user_lists_pb2___SimilarUserListInfo: ...
    @property
    def rule_based_user_list(
        self,
    ) -> google___ads___googleads___v2___common___user_lists_pb2___RuleBasedUserListInfo: ...
    @property
    def logical_user_list(
        self,
    ) -> google___ads___googleads___v2___common___user_lists_pb2___LogicalUserListInfo: ...
    @property
    def basic_user_list(
        self,
    ) -> google___ads___googleads___v2___common___user_lists_pb2___BasicUserListInfo: ...
    def __init__(
        self,
        *,
        resource_name: typing___Optional[typing___Text] = None,
        id: typing___Optional[google___protobuf___wrappers_pb2___Int64Value] = None,
        read_only: typing___Optional[
            google___protobuf___wrappers_pb2___BoolValue
        ] = None,
        name: typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        description: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        membership_status: typing___Optional[
            google___ads___googleads___v2___enums___user_list_membership_status_pb2___UserListMembershipStatusEnum.UserListMembershipStatusValue
        ] = None,
        integration_code: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        membership_life_span: typing___Optional[
            google___protobuf___wrappers_pb2___Int64Value
        ] = None,
        size_for_display: typing___Optional[
            google___protobuf___wrappers_pb2___Int64Value
        ] = None,
        size_range_for_display: typing___Optional[
            google___ads___googleads___v2___enums___user_list_size_range_pb2___UserListSizeRangeEnum.UserListSizeRangeValue
        ] = None,
        size_for_search: typing___Optional[
            google___protobuf___wrappers_pb2___Int64Value
        ] = None,
        size_range_for_search: typing___Optional[
            google___ads___googleads___v2___enums___user_list_size_range_pb2___UserListSizeRangeEnum.UserListSizeRangeValue
        ] = None,
        type: typing___Optional[
            google___ads___googleads___v2___enums___user_list_type_pb2___UserListTypeEnum.UserListTypeValue
        ] = None,
        closing_reason: typing___Optional[
            google___ads___googleads___v2___enums___user_list_closing_reason_pb2___UserListClosingReasonEnum.UserListClosingReasonValue
        ] = None,
        access_reason: typing___Optional[
            google___ads___googleads___v2___enums___access_reason_pb2___AccessReasonEnum.AccessReasonValue
        ] = None,
        account_user_list_status: typing___Optional[
            google___ads___googleads___v2___enums___user_list_access_status_pb2___UserListAccessStatusEnum.UserListAccessStatusValue
        ] = None,
        eligible_for_search: typing___Optional[
            google___protobuf___wrappers_pb2___BoolValue
        ] = None,
        eligible_for_display: typing___Optional[
            google___protobuf___wrappers_pb2___BoolValue
        ] = None,
        crm_based_user_list: typing___Optional[
            google___ads___googleads___v2___common___user_lists_pb2___CrmBasedUserListInfo
        ] = None,
        similar_user_list: typing___Optional[
            google___ads___googleads___v2___common___user_lists_pb2___SimilarUserListInfo
        ] = None,
        rule_based_user_list: typing___Optional[
            google___ads___googleads___v2___common___user_lists_pb2___RuleBasedUserListInfo
        ] = None,
        logical_user_list: typing___Optional[
            google___ads___googleads___v2___common___user_lists_pb2___LogicalUserListInfo
        ] = None,
        basic_user_list: typing___Optional[
            google___ads___googleads___v2___common___user_lists_pb2___BasicUserListInfo
        ] = None,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "basic_user_list",
            b"basic_user_list",
            "crm_based_user_list",
            b"crm_based_user_list",
            "description",
            b"description",
            "eligible_for_display",
            b"eligible_for_display",
            "eligible_for_search",
            b"eligible_for_search",
            "id",
            b"id",
            "integration_code",
            b"integration_code",
            "logical_user_list",
            b"logical_user_list",
            "membership_life_span",
            b"membership_life_span",
            "name",
            b"name",
            "read_only",
            b"read_only",
            "rule_based_user_list",
            b"rule_based_user_list",
            "similar_user_list",
            b"similar_user_list",
            "size_for_display",
            b"size_for_display",
            "size_for_search",
            b"size_for_search",
            "user_list",
            b"user_list",
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "access_reason",
            b"access_reason",
            "account_user_list_status",
            b"account_user_list_status",
            "basic_user_list",
            b"basic_user_list",
            "closing_reason",
            b"closing_reason",
            "crm_based_user_list",
            b"crm_based_user_list",
            "description",
            b"description",
            "eligible_for_display",
            b"eligible_for_display",
            "eligible_for_search",
            b"eligible_for_search",
            "id",
            b"id",
            "integration_code",
            b"integration_code",
            "logical_user_list",
            b"logical_user_list",
            "membership_life_span",
            b"membership_life_span",
            "membership_status",
            b"membership_status",
            "name",
            b"name",
            "read_only",
            b"read_only",
            "resource_name",
            b"resource_name",
            "rule_based_user_list",
            b"rule_based_user_list",
            "similar_user_list",
            b"similar_user_list",
            "size_for_display",
            b"size_for_display",
            "size_for_search",
            b"size_for_search",
            "size_range_for_display",
            b"size_range_for_display",
            "size_range_for_search",
            b"size_range_for_search",
            "type",
            b"type",
            "user_list",
            b"user_list",
        ],
    ) -> None: ...
    def WhichOneof(
        self, oneof_group: typing_extensions___Literal["user_list", b"user_list"]
    ) -> typing_extensions___Literal[
        "crm_based_user_list",
        "similar_user_list",
        "rule_based_user_list",
        "logical_user_list",
        "basic_user_list",
    ]: ...

type___UserList = UserList
