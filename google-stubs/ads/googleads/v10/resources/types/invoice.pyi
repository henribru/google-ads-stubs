import proto
from _typeshed import Incomplete

from google.ads.googleads.v10.common.types import dates as dates
from google.ads.googleads.v10.enums.types import invoice_type as invoice_type

__protobuf__: Incomplete

class Invoice(proto.Message):
    class AccountBudgetSummary(proto.Message):
        customer: Incomplete
        customer_descriptive_name: Incomplete
        account_budget: Incomplete
        account_budget_name: Incomplete
        purchase_order_number: Incomplete
        subtotal_amount_micros: Incomplete
        tax_amount_micros: Incomplete
        total_amount_micros: Incomplete
        billable_activity_date_range: Incomplete
    resource_name: Incomplete
    id: Incomplete
    type_: Incomplete
    billing_setup: Incomplete
    payments_account_id: Incomplete
    payments_profile_id: Incomplete
    issue_date: Incomplete
    due_date: Incomplete
    service_date_range: Incomplete
    currency_code: Incomplete
    adjustments_subtotal_amount_micros: Incomplete
    adjustments_tax_amount_micros: Incomplete
    adjustments_total_amount_micros: Incomplete
    regulatory_costs_subtotal_amount_micros: Incomplete
    regulatory_costs_tax_amount_micros: Incomplete
    regulatory_costs_total_amount_micros: Incomplete
    subtotal_amount_micros: Incomplete
    tax_amount_micros: Incomplete
    total_amount_micros: Incomplete
    corrected_invoice: Incomplete
    replaced_invoices: Incomplete
    pdf_url: Incomplete
    account_budget_summaries: Incomplete
