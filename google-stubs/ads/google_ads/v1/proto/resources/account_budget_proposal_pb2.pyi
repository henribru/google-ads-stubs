# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.ads.google_ads.v1.proto.enums.account_budget_proposal_status_pb2 import (
    AccountBudgetProposalStatusEnum as google___ads___googleads___v1___enums___account_budget_proposal_status_pb2___AccountBudgetProposalStatusEnum,
)

from google.ads.google_ads.v1.proto.enums.account_budget_proposal_type_pb2 import (
    AccountBudgetProposalTypeEnum as google___ads___googleads___v1___enums___account_budget_proposal_type_pb2___AccountBudgetProposalTypeEnum,
)

from google.ads.google_ads.v1.proto.enums.spending_limit_type_pb2 import (
    SpendingLimitTypeEnum as google___ads___googleads___v1___enums___spending_limit_type_pb2___SpendingLimitTypeEnum,
)

from google.ads.google_ads.v1.proto.enums.time_type_pb2 import (
    TimeTypeEnum as google___ads___googleads___v1___enums___time_type_pb2___TimeTypeEnum,
)

from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from google.protobuf.wrappers_pb2 import (
    Int64Value as google___protobuf___wrappers_pb2___Int64Value,
    StringValue as google___protobuf___wrappers_pb2___StringValue,
)

from typing import (
    Optional as typing___Optional,
    Text as typing___Text,
    overload as typing___overload,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


class AccountBudgetProposal(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    resource_name = ... # type: typing___Text
    proposal_type = ... # type: google___ads___googleads___v1___enums___account_budget_proposal_type_pb2___AccountBudgetProposalTypeEnum.AccountBudgetProposalType
    status = ... # type: google___ads___googleads___v1___enums___account_budget_proposal_status_pb2___AccountBudgetProposalStatusEnum.AccountBudgetProposalStatus
    proposed_start_time_type = ... # type: google___ads___googleads___v1___enums___time_type_pb2___TimeTypeEnum.TimeType
    proposed_end_time_type = ... # type: google___ads___googleads___v1___enums___time_type_pb2___TimeTypeEnum.TimeType
    approved_end_time_type = ... # type: google___ads___googleads___v1___enums___time_type_pb2___TimeTypeEnum.TimeType
    proposed_spending_limit_type = ... # type: google___ads___googleads___v1___enums___spending_limit_type_pb2___SpendingLimitTypeEnum.SpendingLimitType
    approved_spending_limit_type = ... # type: google___ads___googleads___v1___enums___spending_limit_type_pb2___SpendingLimitTypeEnum.SpendingLimitType

    @property
    def id(self) -> google___protobuf___wrappers_pb2___Int64Value: ...

    @property
    def billing_setup(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    @property
    def account_budget(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    @property
    def proposed_name(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    @property
    def approved_start_date_time(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    @property
    def proposed_purchase_order_number(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    @property
    def proposed_notes(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    @property
    def creation_date_time(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    @property
    def approval_date_time(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    @property
    def proposed_start_date_time(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    @property
    def proposed_end_date_time(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    @property
    def approved_end_date_time(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    @property
    def proposed_spending_limit_micros(self) -> google___protobuf___wrappers_pb2___Int64Value: ...

    @property
    def approved_spending_limit_micros(self) -> google___protobuf___wrappers_pb2___Int64Value: ...

    def __init__(self,
        *,
        resource_name : typing___Optional[typing___Text] = None,
        id : typing___Optional[google___protobuf___wrappers_pb2___Int64Value] = None,
        billing_setup : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        account_budget : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        proposal_type : typing___Optional[google___ads___googleads___v1___enums___account_budget_proposal_type_pb2___AccountBudgetProposalTypeEnum.AccountBudgetProposalType] = None,
        status : typing___Optional[google___ads___googleads___v1___enums___account_budget_proposal_status_pb2___AccountBudgetProposalStatusEnum.AccountBudgetProposalStatus] = None,
        proposed_name : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        approved_start_date_time : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        proposed_purchase_order_number : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        proposed_notes : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        creation_date_time : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        approval_date_time : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        proposed_start_date_time : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        proposed_start_time_type : typing___Optional[google___ads___googleads___v1___enums___time_type_pb2___TimeTypeEnum.TimeType] = None,
        proposed_end_date_time : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        proposed_end_time_type : typing___Optional[google___ads___googleads___v1___enums___time_type_pb2___TimeTypeEnum.TimeType] = None,
        approved_end_date_time : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        approved_end_time_type : typing___Optional[google___ads___googleads___v1___enums___time_type_pb2___TimeTypeEnum.TimeType] = None,
        proposed_spending_limit_micros : typing___Optional[google___protobuf___wrappers_pb2___Int64Value] = None,
        proposed_spending_limit_type : typing___Optional[google___ads___googleads___v1___enums___spending_limit_type_pb2___SpendingLimitTypeEnum.SpendingLimitType] = None,
        approved_spending_limit_micros : typing___Optional[google___protobuf___wrappers_pb2___Int64Value] = None,
        approved_spending_limit_type : typing___Optional[google___ads___googleads___v1___enums___spending_limit_type_pb2___SpendingLimitTypeEnum.SpendingLimitType] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> AccountBudgetProposal: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"account_budget",u"approval_date_time",u"approved_end_date_time",u"approved_end_time",u"approved_end_time_type",u"approved_spending_limit",u"approved_spending_limit_micros",u"approved_spending_limit_type",u"approved_start_date_time",u"billing_setup",u"creation_date_time",u"id",u"proposed_end_date_time",u"proposed_end_time",u"proposed_end_time_type",u"proposed_name",u"proposed_notes",u"proposed_purchase_order_number",u"proposed_spending_limit",u"proposed_spending_limit_micros",u"proposed_spending_limit_type",u"proposed_start_date_time",u"proposed_start_time",u"proposed_start_time_type"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"account_budget",u"approval_date_time",u"approved_end_date_time",u"approved_end_time",u"approved_end_time_type",u"approved_spending_limit",u"approved_spending_limit_micros",u"approved_spending_limit_type",u"approved_start_date_time",u"billing_setup",u"creation_date_time",u"id",u"proposal_type",u"proposed_end_date_time",u"proposed_end_time",u"proposed_end_time_type",u"proposed_name",u"proposed_notes",u"proposed_purchase_order_number",u"proposed_spending_limit",u"proposed_spending_limit_micros",u"proposed_spending_limit_type",u"proposed_start_date_time",u"proposed_start_time",u"proposed_start_time_type",u"resource_name",u"status"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"account_budget",b"account_budget",u"approval_date_time",b"approval_date_time",u"approved_end_date_time",b"approved_end_date_time",u"approved_end_time",b"approved_end_time",u"approved_end_time_type",b"approved_end_time_type",u"approved_spending_limit",b"approved_spending_limit",u"approved_spending_limit_micros",b"approved_spending_limit_micros",u"approved_spending_limit_type",b"approved_spending_limit_type",u"approved_start_date_time",b"approved_start_date_time",u"billing_setup",b"billing_setup",u"creation_date_time",b"creation_date_time",u"id",b"id",u"proposed_end_date_time",b"proposed_end_date_time",u"proposed_end_time",b"proposed_end_time",u"proposed_end_time_type",b"proposed_end_time_type",u"proposed_name",b"proposed_name",u"proposed_notes",b"proposed_notes",u"proposed_purchase_order_number",b"proposed_purchase_order_number",u"proposed_spending_limit",b"proposed_spending_limit",u"proposed_spending_limit_micros",b"proposed_spending_limit_micros",u"proposed_spending_limit_type",b"proposed_spending_limit_type",u"proposed_start_date_time",b"proposed_start_date_time",u"proposed_start_time",b"proposed_start_time",u"proposed_start_time_type",b"proposed_start_time_type"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"account_budget",b"account_budget",u"approval_date_time",b"approval_date_time",u"approved_end_date_time",b"approved_end_date_time",u"approved_end_time",b"approved_end_time",u"approved_end_time_type",b"approved_end_time_type",u"approved_spending_limit",b"approved_spending_limit",u"approved_spending_limit_micros",b"approved_spending_limit_micros",u"approved_spending_limit_type",b"approved_spending_limit_type",u"approved_start_date_time",b"approved_start_date_time",u"billing_setup",b"billing_setup",u"creation_date_time",b"creation_date_time",u"id",b"id",u"proposal_type",b"proposal_type",u"proposed_end_date_time",b"proposed_end_date_time",u"proposed_end_time",b"proposed_end_time",u"proposed_end_time_type",b"proposed_end_time_type",u"proposed_name",b"proposed_name",u"proposed_notes",b"proposed_notes",u"proposed_purchase_order_number",b"proposed_purchase_order_number",u"proposed_spending_limit",b"proposed_spending_limit",u"proposed_spending_limit_micros",b"proposed_spending_limit_micros",u"proposed_spending_limit_type",b"proposed_spending_limit_type",u"proposed_start_date_time",b"proposed_start_date_time",u"proposed_start_time",b"proposed_start_time",u"proposed_start_time_type",b"proposed_start_time_type",u"resource_name",b"resource_name",u"status",b"status"]) -> None: ...
    @typing___overload
    def WhichOneof(self, oneof_group: typing_extensions___Literal[u"approved_end_time",b"approved_end_time"]) -> typing_extensions___Literal["approved_end_date_time","approved_end_time_type"]: ...
    @typing___overload
    def WhichOneof(self, oneof_group: typing_extensions___Literal[u"approved_spending_limit",b"approved_spending_limit"]) -> typing_extensions___Literal["approved_spending_limit_micros","approved_spending_limit_type"]: ...
    @typing___overload
    def WhichOneof(self, oneof_group: typing_extensions___Literal[u"proposed_end_time",b"proposed_end_time"]) -> typing_extensions___Literal["proposed_end_date_time","proposed_end_time_type"]: ...
    @typing___overload
    def WhichOneof(self, oneof_group: typing_extensions___Literal[u"proposed_spending_limit",b"proposed_spending_limit"]) -> typing_extensions___Literal["proposed_spending_limit_micros","proposed_spending_limit_type"]: ...
    @typing___overload
    def WhichOneof(self, oneof_group: typing_extensions___Literal[u"proposed_start_time",b"proposed_start_time"]) -> typing_extensions___Literal["proposed_start_date_time","proposed_start_time_type"]: ...
