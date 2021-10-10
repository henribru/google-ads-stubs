from typing import Any

import proto

from google.ads.googleads.v8.enums.types import (
    account_budget_proposal_type as account_budget_proposal_type,
    account_budget_status as account_budget_status,
    time_type as time_type,
)

__protobuf__: Any

class AccountBudget(proto.Message):
    class PendingAccountBudgetProposal(proto.Message):
        account_budget_proposal: Any
        proposal_type: Any
        name: Any
        start_date_time: Any
        purchase_order_number: Any
        notes: Any
        creation_date_time: Any
        end_date_time: Any
        end_time_type: Any
        spending_limit_micros: Any
        spending_limit_type: Any
    resource_name: Any
    id: Any
    billing_setup: Any
    status: Any
    name: Any
    proposed_start_date_time: Any
    approved_start_date_time: Any
    total_adjustments_micros: Any
    amount_served_micros: Any
    purchase_order_number: Any
    notes: Any
    pending_proposal: Any
    proposed_end_date_time: Any
    proposed_end_time_type: Any
    approved_end_date_time: Any
    approved_end_time_type: Any
    proposed_spending_limit_micros: Any
    proposed_spending_limit_type: Any
    approved_spending_limit_micros: Any
    approved_spending_limit_type: Any
    adjusted_spending_limit_micros: Any
    adjusted_spending_limit_type: Any
