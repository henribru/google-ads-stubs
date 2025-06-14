import proto
from _typeshed import Incomplete
from google.ads.googleads.v19.enums.types import account_budget_proposal_status, account_budget_proposal_type, spending_limit_type, time_type

__protobuf__: Incomplete

class AccountBudgetProposal(proto.Message):
    resource_name: str
    id: int
    billing_setup: str
    account_budget: str
    proposal_type: account_budget_proposal_type.AccountBudgetProposalTypeEnum.AccountBudgetProposalType
    status: account_budget_proposal_status.AccountBudgetProposalStatusEnum.AccountBudgetProposalStatus
    proposed_name: str
    approved_start_date_time: str
    proposed_purchase_order_number: str
    proposed_notes: str
    creation_date_time: str
    approval_date_time: str
    proposed_start_date_time: str
    proposed_start_time_type: time_type.TimeTypeEnum.TimeType
    proposed_end_date_time: str
    proposed_end_time_type: time_type.TimeTypeEnum.TimeType
    approved_end_date_time: str
    approved_end_time_type: time_type.TimeTypeEnum.TimeType
    proposed_spending_limit_micros: int
    proposed_spending_limit_type: spending_limit_type.SpendingLimitTypeEnum.SpendingLimitType
    approved_spending_limit_micros: int
    approved_spending_limit_type: spending_limit_type.SpendingLimitTypeEnum.SpendingLimitType
