from typing import Any

import proto

from google.ads.googleads.v7.enums.types import (
    account_budget_proposal_status as account_budget_proposal_status,
    account_budget_proposal_type as account_budget_proposal_type,
    spending_limit_type as spending_limit_type,
    time_type as time_type,
)

__protobuf__: Any

class AccountBudgetProposal(proto.Message):
    resource_name: Any
    id: Any
    billing_setup: Any
    account_budget: Any
    proposal_type: Any
    status: Any
    proposed_name: Any
    approved_start_date_time: Any
    proposed_purchase_order_number: Any
    proposed_notes: Any
    creation_date_time: Any
    approval_date_time: Any
    proposed_start_date_time: Any
    proposed_start_time_type: Any
    proposed_end_date_time: Any
    proposed_end_time_type: Any
    approved_end_date_time: Any
    approved_end_time_type: Any
    proposed_spending_limit_micros: Any
    proposed_spending_limit_type: Any
    approved_spending_limit_micros: Any
    approved_spending_limit_type: Any
