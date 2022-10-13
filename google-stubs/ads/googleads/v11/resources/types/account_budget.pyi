from typing import Any

import proto

from google.ads.googleads.v11.enums.types.account_budget_proposal_type import (
    AccountBudgetProposalTypeEnum,
)
from google.ads.googleads.v11.enums.types.account_budget_status import (
    AccountBudgetStatusEnum,
)
from google.ads.googleads.v11.enums.types.spending_limit_type import (
    SpendingLimitTypeEnum,
)
from google.ads.googleads.v11.enums.types.time_type import TimeTypeEnum

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
            self,
            mapping: Any | None = ...,
            *,
            ignore_unknown_fields: bool = ...,
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
            spending_limit_type: SpendingLimitTypeEnum.SpendingLimitType = ...
        ) -> None: ...
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
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
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
        adjusted_spending_limit_type: SpendingLimitTypeEnum.SpendingLimitType = ...
    ) -> None: ...
