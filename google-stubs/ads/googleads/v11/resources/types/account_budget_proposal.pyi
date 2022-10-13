from typing import Any

import proto

from google.ads.googleads.v11.enums.types.account_budget_proposal_status import (
    AccountBudgetProposalStatusEnum,
)
from google.ads.googleads.v11.enums.types.account_budget_proposal_type import (
    AccountBudgetProposalTypeEnum,
)
from google.ads.googleads.v11.enums.types.spending_limit_type import (
    SpendingLimitTypeEnum,
)
from google.ads.googleads.v11.enums.types.time_type import TimeTypeEnum

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
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
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
        approved_spending_limit_type: SpendingLimitTypeEnum.SpendingLimitType = ...
    ) -> None: ...
