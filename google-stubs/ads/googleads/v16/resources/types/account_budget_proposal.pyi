from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v16.enums.types.account_budget_proposal_status import (
    AccountBudgetProposalStatusEnum,
)
from google.ads.googleads.v16.enums.types.account_budget_proposal_type import (
    AccountBudgetProposalTypeEnum,
)
from google.ads.googleads.v16.enums.types.spending_limit_type import (
    SpendingLimitTypeEnum,
)
from google.ads.googleads.v16.enums.types.time_type import TimeTypeEnum

_M = TypeVar("_M")

class AccountBudgetProposal(proto.Message):
    resource_name: str
    id: int
    billing_setup: str
    account_budget: str
    proposal_type: AccountBudgetProposalTypeEnum.AccountBudgetProposalType
    status: AccountBudgetProposalStatusEnum.AccountBudgetProposalStatus
    proposed_name: str
    approved_start_date_time: str
    proposed_purchase_order_number: str
    proposed_notes: str
    creation_date_time: str
    approval_date_time: str
    proposed_start_date_time: str
    proposed_start_time_type: TimeTypeEnum.TimeType
    proposed_end_date_time: str
    proposed_end_time_type: TimeTypeEnum.TimeType
    approved_end_date_time: str
    approved_end_time_type: TimeTypeEnum.TimeType
    proposed_spending_limit_micros: int
    proposed_spending_limit_type: SpendingLimitTypeEnum.SpendingLimitType
    approved_spending_limit_micros: int
    approved_spending_limit_type: SpendingLimitTypeEnum.SpendingLimitType
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        id: int = ...,
        billing_setup: str = ...,
        account_budget: str = ...,
        proposal_type: AccountBudgetProposalTypeEnum.AccountBudgetProposalType = ...,
        status: AccountBudgetProposalStatusEnum.AccountBudgetProposalStatus = ...,
        proposed_name: str = ...,
        approved_start_date_time: str = ...,
        proposed_purchase_order_number: str = ...,
        proposed_notes: str = ...,
        creation_date_time: str = ...,
        approval_date_time: str = ...,
        proposed_start_date_time: str = ...,
        proposed_start_time_type: TimeTypeEnum.TimeType = ...,
        proposed_end_date_time: str = ...,
        proposed_end_time_type: TimeTypeEnum.TimeType = ...,
        approved_end_date_time: str = ...,
        approved_end_time_type: TimeTypeEnum.TimeType = ...,
        proposed_spending_limit_micros: int = ...,
        proposed_spending_limit_type: SpendingLimitTypeEnum.SpendingLimitType = ...,
        approved_spending_limit_micros: int = ...,
        approved_spending_limit_type: SpendingLimitTypeEnum.SpendingLimitType = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "resource_name",
            "id",
            "billing_setup",
            "account_budget",
            "proposal_type",
            "status",
            "proposed_name",
            "approved_start_date_time",
            "proposed_purchase_order_number",
            "proposed_notes",
            "creation_date_time",
            "approval_date_time",
            "proposed_start_date_time",
            "proposed_start_time_type",
            "proposed_end_date_time",
            "proposed_end_time_type",
            "approved_end_date_time",
            "approved_end_time_type",
            "proposed_spending_limit_micros",
            "proposed_spending_limit_type",
            "approved_spending_limit_micros",
            "approved_spending_limit_type",
        ],
    ) -> bool: ...
