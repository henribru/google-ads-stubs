import proto
from _typeshed import Incomplete

from google.ads.googleads.v10.enums.types import (
    account_budget_proposal_type as account_budget_proposal_type,
    account_budget_status as account_budget_status,
    time_type as time_type,
)

__protobuf__: Incomplete

class AccountBudget(proto.Message):
    class PendingAccountBudgetProposal(proto.Message):
        account_budget_proposal: Incomplete
        proposal_type: Incomplete
        name: Incomplete
        start_date_time: Incomplete
        purchase_order_number: Incomplete
        notes: Incomplete
        creation_date_time: Incomplete
        end_date_time: Incomplete
        end_time_type: Incomplete
        spending_limit_micros: Incomplete
        spending_limit_type: Incomplete
    resource_name: Incomplete
    id: Incomplete
    billing_setup: Incomplete
    status: Incomplete
    name: Incomplete
    proposed_start_date_time: Incomplete
    approved_start_date_time: Incomplete
    total_adjustments_micros: Incomplete
    amount_served_micros: Incomplete
    purchase_order_number: Incomplete
    notes: Incomplete
    pending_proposal: Incomplete
    proposed_end_date_time: Incomplete
    proposed_end_time_type: Incomplete
    approved_end_date_time: Incomplete
    approved_end_time_type: Incomplete
    proposed_spending_limit_micros: Incomplete
    proposed_spending_limit_type: Incomplete
    approved_spending_limit_micros: Incomplete
    approved_spending_limit_type: Incomplete
    adjusted_spending_limit_micros: Incomplete
    adjusted_spending_limit_type: Incomplete
