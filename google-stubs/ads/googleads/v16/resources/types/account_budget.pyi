from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v16.enums.types.account_budget_proposal_type import (
    AccountBudgetProposalTypeEnum,
)
from google.ads.googleads.v16.enums.types.account_budget_status import (
    AccountBudgetStatusEnum,
)
from google.ads.googleads.v16.enums.types.spending_limit_type import (
    SpendingLimitTypeEnum,
)
from google.ads.googleads.v16.enums.types.time_type import TimeTypeEnum

_M = TypeVar("_M")

class AccountBudget(proto.Message):
    class PendingAccountBudgetProposal(proto.Message):
        account_budget_proposal: str
        proposal_type: AccountBudgetProposalTypeEnum.AccountBudgetProposalType
        name: str
        start_date_time: str
        purchase_order_number: str
        notes: str
        creation_date_time: str
        end_date_time: str
        end_time_type: TimeTypeEnum.TimeType
        spending_limit_micros: int
        spending_limit_type: SpendingLimitTypeEnum.SpendingLimitType
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
            account_budget_proposal: str = ...,
            proposal_type: AccountBudgetProposalTypeEnum.AccountBudgetProposalType = ...,
            name: str = ...,
            start_date_time: str = ...,
            purchase_order_number: str = ...,
            notes: str = ...,
            creation_date_time: str = ...,
            end_date_time: str = ...,
            end_time_type: TimeTypeEnum.TimeType = ...,
            spending_limit_micros: int = ...,
            spending_limit_type: SpendingLimitTypeEnum.SpendingLimitType = ...,
        ) -> None: ...
        def __contains__(  # type: ignore[override]
            self,
            key: Literal[
                "account_budget_proposal",
                "proposal_type",
                "name",
                "start_date_time",
                "purchase_order_number",
                "notes",
                "creation_date_time",
                "end_date_time",
                "end_time_type",
                "spending_limit_micros",
                "spending_limit_type",
            ],
        ) -> bool: ...

    resource_name: str
    id: int
    billing_setup: str
    status: AccountBudgetStatusEnum.AccountBudgetStatus
    name: str
    proposed_start_date_time: str
    approved_start_date_time: str
    total_adjustments_micros: int
    amount_served_micros: int
    purchase_order_number: str
    notes: str
    pending_proposal: AccountBudget.PendingAccountBudgetProposal
    proposed_end_date_time: str
    proposed_end_time_type: TimeTypeEnum.TimeType
    approved_end_date_time: str
    approved_end_time_type: TimeTypeEnum.TimeType
    proposed_spending_limit_micros: int
    proposed_spending_limit_type: SpendingLimitTypeEnum.SpendingLimitType
    approved_spending_limit_micros: int
    approved_spending_limit_type: SpendingLimitTypeEnum.SpendingLimitType
    adjusted_spending_limit_micros: int
    adjusted_spending_limit_type: SpendingLimitTypeEnum.SpendingLimitType
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        id: int = ...,
        billing_setup: str = ...,
        status: AccountBudgetStatusEnum.AccountBudgetStatus = ...,
        name: str = ...,
        proposed_start_date_time: str = ...,
        approved_start_date_time: str = ...,
        total_adjustments_micros: int = ...,
        amount_served_micros: int = ...,
        purchase_order_number: str = ...,
        notes: str = ...,
        pending_proposal: AccountBudget.PendingAccountBudgetProposal = ...,
        proposed_end_date_time: str = ...,
        proposed_end_time_type: TimeTypeEnum.TimeType = ...,
        approved_end_date_time: str = ...,
        approved_end_time_type: TimeTypeEnum.TimeType = ...,
        proposed_spending_limit_micros: int = ...,
        proposed_spending_limit_type: SpendingLimitTypeEnum.SpendingLimitType = ...,
        approved_spending_limit_micros: int = ...,
        approved_spending_limit_type: SpendingLimitTypeEnum.SpendingLimitType = ...,
        adjusted_spending_limit_micros: int = ...,
        adjusted_spending_limit_type: SpendingLimitTypeEnum.SpendingLimitType = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "resource_name",
            "id",
            "billing_setup",
            "status",
            "name",
            "proposed_start_date_time",
            "approved_start_date_time",
            "total_adjustments_micros",
            "amount_served_micros",
            "purchase_order_number",
            "notes",
            "pending_proposal",
            "proposed_end_date_time",
            "proposed_end_time_type",
            "approved_end_date_time",
            "approved_end_time_type",
            "proposed_spending_limit_micros",
            "proposed_spending_limit_type",
            "approved_spending_limit_micros",
            "approved_spending_limit_type",
            "adjusted_spending_limit_micros",
            "adjusted_spending_limit_type",
        ],
    ) -> bool: ...
