import proto
from _typeshed import Incomplete

from google.ads.googleads.v11.enums.types import (
    account_budget_proposal_status as account_budget_proposal_status,
    account_budget_proposal_type as account_budget_proposal_type,
    spending_limit_type as spending_limit_type,
    time_type as time_type,
)

__protobuf__: Incomplete

class AccountBudgetProposal(proto.Message):
    resource_name: Incomplete
    id: Incomplete
    billing_setup: Incomplete
    account_budget: Incomplete
    proposal_type: Incomplete
    status: Incomplete
    proposed_name: Incomplete
    approved_start_date_time: Incomplete
    proposed_purchase_order_number: Incomplete
    proposed_notes: Incomplete
    creation_date_time: Incomplete
    approval_date_time: Incomplete
    proposed_start_date_time: Incomplete
    proposed_start_time_type: Incomplete
    proposed_end_date_time: Incomplete
    proposed_end_time_type: Incomplete
    approved_end_date_time: Incomplete
    approved_end_time_type: Incomplete
    proposed_spending_limit_micros: Incomplete
    proposed_spending_limit_type: Incomplete
    approved_spending_limit_micros: Incomplete
    approved_spending_limit_type: Incomplete
