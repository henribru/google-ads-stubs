from typing import Any

import proto

from google.ads.googleads.v8.common.types import dates as dates
from google.ads.googleads.v8.enums.types import invoice_type as invoice_type

__protobuf__: Any

class Invoice(proto.Message):
    class AccountBudgetSummary(proto.Message):
        customer: Any
        customer_descriptive_name: Any
        account_budget: Any
        account_budget_name: Any
        purchase_order_number: Any
        subtotal_amount_micros: Any
        tax_amount_micros: Any
        total_amount_micros: Any
        billable_activity_date_range: Any
    resource_name: Any
    id: Any
    type_: Any
    billing_setup: Any
    payments_account_id: Any
    payments_profile_id: Any
    issue_date: Any
    due_date: Any
    service_date_range: Any
    currency_code: Any
    adjustments_subtotal_amount_micros: Any
    adjustments_tax_amount_micros: Any
    adjustments_total_amount_micros: Any
    regulatory_costs_subtotal_amount_micros: Any
    regulatory_costs_tax_amount_micros: Any
    regulatory_costs_total_amount_micros: Any
    subtotal_amount_micros: Any
    tax_amount_micros: Any
    total_amount_micros: Any
    corrected_invoice: Any
    replaced_invoices: Any
    pdf_url: Any
    account_budget_summaries: Any
