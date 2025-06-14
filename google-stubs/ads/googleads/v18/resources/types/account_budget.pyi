import proto
from _typeshed import Incomplete
from google.ads.googleads.v18.enums.types import account_budget_proposal_type, account_budget_status, spending_limit_type as gage_spending_limit_type, time_type

__protobuf__: Incomplete

class AccountBudget(proto.Message):
    class PendingAccountBudgetProposal(proto.Message):
        account_budget_proposal: str
        proposal_type: account_budget_proposal_type.AccountBudgetProposalTypeEnum.AccountBudgetProposalType
        name: str
        start_date_time: str
        purchase_order_number: str
        notes: str
        creation_date_time: str
        end_date_time: str
        end_time_type: time_type.TimeTypeEnum.TimeType
        spending_limit_micros: int
        spending_limit_type: gage_spending_limit_type.SpendingLimitTypeEnum.SpendingLimitType
    resource_name: str
    id: int
    billing_setup: str
    status: account_budget_status.AccountBudgetStatusEnum.AccountBudgetStatus
    name: str
    proposed_start_date_time: str
    approved_start_date_time: str
    total_adjustments_micros: int
    amount_served_micros: int
    purchase_order_number: str
    notes: str
    pending_proposal: PendingAccountBudgetProposal
    proposed_end_date_time: str
    proposed_end_time_type: time_type.TimeTypeEnum.TimeType
    approved_end_date_time: str
    approved_end_time_type: time_type.TimeTypeEnum.TimeType
    proposed_spending_limit_micros: int
    proposed_spending_limit_type: gage_spending_limit_type.SpendingLimitTypeEnum.SpendingLimitType
    approved_spending_limit_micros: int
    approved_spending_limit_type: gage_spending_limit_type.SpendingLimitTypeEnum.SpendingLimitType
    adjusted_spending_limit_micros: int
    adjusted_spending_limit_type: gage_spending_limit_type.SpendingLimitTypeEnum.SpendingLimitType
