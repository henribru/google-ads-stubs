# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.ads.google_ads.v1.proto.common.user_lists_pb2 import (
    BasicUserListInfo as google___ads___googleads___v1___common___user_lists_pb2___BasicUserListInfo,
    CrmBasedUserListInfo as google___ads___googleads___v1___common___user_lists_pb2___CrmBasedUserListInfo,
    LogicalUserListInfo as google___ads___googleads___v1___common___user_lists_pb2___LogicalUserListInfo,
    RuleBasedUserListInfo as google___ads___googleads___v1___common___user_lists_pb2___RuleBasedUserListInfo,
    SimilarUserListInfo as google___ads___googleads___v1___common___user_lists_pb2___SimilarUserListInfo,
)

from google.ads.google_ads.v1.proto.enums.access_reason_pb2 import (
    AccessReasonEnum as google___ads___googleads___v1___enums___access_reason_pb2___AccessReasonEnum,
)

from google.ads.google_ads.v1.proto.enums.user_list_access_status_pb2 import (
    UserListAccessStatusEnum as google___ads___googleads___v1___enums___user_list_access_status_pb2___UserListAccessStatusEnum,
)

from google.ads.google_ads.v1.proto.enums.user_list_closing_reason_pb2 import (
    UserListClosingReasonEnum as google___ads___googleads___v1___enums___user_list_closing_reason_pb2___UserListClosingReasonEnum,
)

from google.ads.google_ads.v1.proto.enums.user_list_membership_status_pb2 import (
    UserListMembershipStatusEnum as google___ads___googleads___v1___enums___user_list_membership_status_pb2___UserListMembershipStatusEnum,
)

from google.ads.google_ads.v1.proto.enums.user_list_size_range_pb2 import (
    UserListSizeRangeEnum as google___ads___googleads___v1___enums___user_list_size_range_pb2___UserListSizeRangeEnum,
)

from google.ads.google_ads.v1.proto.enums.user_list_type_pb2 import (
    UserListTypeEnum as google___ads___googleads___v1___enums___user_list_type_pb2___UserListTypeEnum,
)

from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from google.protobuf.wrappers_pb2 import (
    BoolValue as google___protobuf___wrappers_pb2___BoolValue,
    Int64Value as google___protobuf___wrappers_pb2___Int64Value,
    StringValue as google___protobuf___wrappers_pb2___StringValue,
)

from typing import (
    Optional as typing___Optional,
    Text as typing___Text,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


class UserList(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    resource_name = ... # type: typing___Text
    membership_status = ... # type: google___ads___googleads___v1___enums___user_list_membership_status_pb2___UserListMembershipStatusEnum.UserListMembershipStatus
    size_range_for_display = ... # type: google___ads___googleads___v1___enums___user_list_size_range_pb2___UserListSizeRangeEnum.UserListSizeRange
    size_range_for_search = ... # type: google___ads___googleads___v1___enums___user_list_size_range_pb2___UserListSizeRangeEnum.UserListSizeRange
    type = ... # type: google___ads___googleads___v1___enums___user_list_type_pb2___UserListTypeEnum.UserListType
    closing_reason = ... # type: google___ads___googleads___v1___enums___user_list_closing_reason_pb2___UserListClosingReasonEnum.UserListClosingReason
    access_reason = ... # type: google___ads___googleads___v1___enums___access_reason_pb2___AccessReasonEnum.AccessReason
    account_user_list_status = ... # type: google___ads___googleads___v1___enums___user_list_access_status_pb2___UserListAccessStatusEnum.UserListAccessStatus

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
    def crm_based_user_list(self) -> google___ads___googleads___v1___common___user_lists_pb2___CrmBasedUserListInfo: ...

    @property
    def similar_user_list(self) -> google___ads___googleads___v1___common___user_lists_pb2___SimilarUserListInfo: ...

    @property
    def rule_based_user_list(self) -> google___ads___googleads___v1___common___user_lists_pb2___RuleBasedUserListInfo: ...

    @property
    def logical_user_list(self) -> google___ads___googleads___v1___common___user_lists_pb2___LogicalUserListInfo: ...

    @property
    def basic_user_list(self) -> google___ads___googleads___v1___common___user_lists_pb2___BasicUserListInfo: ...

    def __init__(self,
        *,
        resource_name : typing___Optional[typing___Text] = None,
        id : typing___Optional[google___protobuf___wrappers_pb2___Int64Value] = None,
        read_only : typing___Optional[google___protobuf___wrappers_pb2___BoolValue] = None,
        name : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        description : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        membership_status : typing___Optional[google___ads___googleads___v1___enums___user_list_membership_status_pb2___UserListMembershipStatusEnum.UserListMembershipStatus] = None,
        integration_code : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        membership_life_span : typing___Optional[google___protobuf___wrappers_pb2___Int64Value] = None,
        size_for_display : typing___Optional[google___protobuf___wrappers_pb2___Int64Value] = None,
        size_range_for_display : typing___Optional[google___ads___googleads___v1___enums___user_list_size_range_pb2___UserListSizeRangeEnum.UserListSizeRange] = None,
        size_for_search : typing___Optional[google___protobuf___wrappers_pb2___Int64Value] = None,
        size_range_for_search : typing___Optional[google___ads___googleads___v1___enums___user_list_size_range_pb2___UserListSizeRangeEnum.UserListSizeRange] = None,
        type : typing___Optional[google___ads___googleads___v1___enums___user_list_type_pb2___UserListTypeEnum.UserListType] = None,
        closing_reason : typing___Optional[google___ads___googleads___v1___enums___user_list_closing_reason_pb2___UserListClosingReasonEnum.UserListClosingReason] = None,
        access_reason : typing___Optional[google___ads___googleads___v1___enums___access_reason_pb2___AccessReasonEnum.AccessReason] = None,
        account_user_list_status : typing___Optional[google___ads___googleads___v1___enums___user_list_access_status_pb2___UserListAccessStatusEnum.UserListAccessStatus] = None,
        eligible_for_search : typing___Optional[google___protobuf___wrappers_pb2___BoolValue] = None,
        eligible_for_display : typing___Optional[google___protobuf___wrappers_pb2___BoolValue] = None,
        crm_based_user_list : typing___Optional[google___ads___googleads___v1___common___user_lists_pb2___CrmBasedUserListInfo] = None,
        similar_user_list : typing___Optional[google___ads___googleads___v1___common___user_lists_pb2___SimilarUserListInfo] = None,
        rule_based_user_list : typing___Optional[google___ads___googleads___v1___common___user_lists_pb2___RuleBasedUserListInfo] = None,
        logical_user_list : typing___Optional[google___ads___googleads___v1___common___user_lists_pb2___LogicalUserListInfo] = None,
        basic_user_list : typing___Optional[google___ads___googleads___v1___common___user_lists_pb2___BasicUserListInfo] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> UserList: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"basic_user_list",u"crm_based_user_list",u"description",u"eligible_for_display",u"eligible_for_search",u"id",u"integration_code",u"logical_user_list",u"membership_life_span",u"name",u"read_only",u"rule_based_user_list",u"similar_user_list",u"size_for_display",u"size_for_search",u"user_list"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"access_reason",u"account_user_list_status",u"basic_user_list",u"closing_reason",u"crm_based_user_list",u"description",u"eligible_for_display",u"eligible_for_search",u"id",u"integration_code",u"logical_user_list",u"membership_life_span",u"membership_status",u"name",u"read_only",u"resource_name",u"rule_based_user_list",u"similar_user_list",u"size_for_display",u"size_for_search",u"size_range_for_display",u"size_range_for_search",u"type",u"user_list"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"basic_user_list",b"basic_user_list",u"crm_based_user_list",b"crm_based_user_list",u"description",b"description",u"eligible_for_display",b"eligible_for_display",u"eligible_for_search",b"eligible_for_search",u"id",b"id",u"integration_code",b"integration_code",u"logical_user_list",b"logical_user_list",u"membership_life_span",b"membership_life_span",u"name",b"name",u"read_only",b"read_only",u"rule_based_user_list",b"rule_based_user_list",u"similar_user_list",b"similar_user_list",u"size_for_display",b"size_for_display",u"size_for_search",b"size_for_search",u"user_list",b"user_list"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"access_reason",b"access_reason",u"account_user_list_status",b"account_user_list_status",u"basic_user_list",b"basic_user_list",u"closing_reason",b"closing_reason",u"crm_based_user_list",b"crm_based_user_list",u"description",b"description",u"eligible_for_display",b"eligible_for_display",u"eligible_for_search",b"eligible_for_search",u"id",b"id",u"integration_code",b"integration_code",u"logical_user_list",b"logical_user_list",u"membership_life_span",b"membership_life_span",u"membership_status",b"membership_status",u"name",b"name",u"read_only",b"read_only",u"resource_name",b"resource_name",u"rule_based_user_list",b"rule_based_user_list",u"similar_user_list",b"similar_user_list",u"size_for_display",b"size_for_display",u"size_for_search",b"size_for_search",u"size_range_for_display",b"size_range_for_display",u"size_range_for_search",b"size_range_for_search",u"type",b"type",u"user_list",b"user_list"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions___Literal[u"user_list",b"user_list"]) -> typing_extensions___Literal["crm_based_user_list","similar_user_list","rule_based_user_list","logical_user_list","basic_user_list"]: ...
