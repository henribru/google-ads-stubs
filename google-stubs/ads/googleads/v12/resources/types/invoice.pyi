from collections.abc import MutableSequence
from typing import Any

import proto

from google.ads.googleads.v12.common.types.dates import DateRange
from google.ads.googleads.v12.enums.types.invoice_type import InvoiceTypeEnum

class Invoice(proto.Message):
    class AccountBudgetSummary(proto.Message):
        customer: str
        customer_descriptive_name: str
        account_budget: str
        account_budget_name: str
        purchase_order_number: str
        subtotal_amount_micros: int
        tax_amount_micros: int
        total_amount_micros: int
        billable_activity_date_range: DateRange
        served_amount_micros: int
        billed_amount_micros: int
        overdelivery_amount_micros: int
        invalid_activity_amount_micros: int
        def __init__(
            self,
            mapping: Any | None = ...,
            *,
            ignore_unknown_fields: bool = ...,
            customer: str = ...,
            customer_descriptive_name: str = ...,
            account_budget: str = ...,
            account_budget_name: str = ...,
            purchase_order_number: str = ...,
            subtotal_amount_micros: int = ...,
            tax_amount_micros: int = ...,
            total_amount_micros: int = ...,
            billable_activity_date_range: DateRange = ...,
            served_amount_micros: int = ...,
            billed_amount_micros: int = ...,
            overdelivery_amount_micros: int = ...,
            invalid_activity_amount_micros: int = ...
        ) -> None: ...

    class AccountSummary(proto.Message):
        customer: str
        billing_correction_subtotal_amount_micros: int
        billing_correction_tax_amount_micros: int
        billing_correction_total_amount_micros: int
        coupon_adjustment_subtotal_amount_micros: int
        coupon_adjustment_tax_amount_micros: int
        coupon_adjustment_total_amount_micros: int
        excess_credit_adjustment_subtotal_amount_micros: int
        excess_credit_adjustment_tax_amount_micros: int
        excess_credit_adjustment_total_amount_micros: int
        regulatory_costs_subtotal_amount_micros: int
        regulatory_costs_tax_amount_micros: int
        regulatory_costs_total_amount_micros: int
        subtotal_amount_micros: int
        tax_amount_micros: int
        total_amount_micros: int
        def __init__(
            self,
            mapping: Any | None = ...,
            *,
            ignore_unknown_fields: bool = ...,
            customer: str = ...,
            billing_correction_subtotal_amount_micros: int = ...,
            billing_correction_tax_amount_micros: int = ...,
            billing_correction_total_amount_micros: int = ...,
            coupon_adjustment_subtotal_amount_micros: int = ...,
            coupon_adjustment_tax_amount_micros: int = ...,
            coupon_adjustment_total_amount_micros: int = ...,
            excess_credit_adjustment_subtotal_amount_micros: int = ...,
            excess_credit_adjustment_tax_amount_micros: int = ...,
            excess_credit_adjustment_total_amount_micros: int = ...,
            regulatory_costs_subtotal_amount_micros: int = ...,
            regulatory_costs_tax_amount_micros: int = ...,
            regulatory_costs_total_amount_micros: int = ...,
            subtotal_amount_micros: int = ...,
            tax_amount_micros: int = ...,
            total_amount_micros: int = ...
        ) -> None: ...
    resource_name: str
    id: str
    type_: InvoiceTypeEnum.InvoiceType
    billing_setup: str
    payments_account_id: str
    payments_profile_id: str
    issue_date: str
    due_date: str
    service_date_range: DateRange
    currency_code: str
    adjustments_subtotal_amount_micros: int
    adjustments_tax_amount_micros: int
    adjustments_total_amount_micros: int
    regulatory_costs_subtotal_amount_micros: int
    regulatory_costs_tax_amount_micros: int
    regulatory_costs_total_amount_micros: int
    subtotal_amount_micros: int
    tax_amount_micros: int
    total_amount_micros: int
    corrected_invoice: str
    replaced_invoices: MutableSequence[str]
    pdf_url: str
    account_budget_summaries: MutableSequence[Invoice.AccountBudgetSummary]
    account_summaries: MutableSequence[Invoice.AccountSummary]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        id: str = ...,
        type_: InvoiceTypeEnum.InvoiceType = ...,
        billing_setup: str = ...,
        payments_account_id: str = ...,
        payments_profile_id: str = ...,
        issue_date: str = ...,
        due_date: str = ...,
        service_date_range: DateRange = ...,
        currency_code: str = ...,
        adjustments_subtotal_amount_micros: int = ...,
        adjustments_tax_amount_micros: int = ...,
        adjustments_total_amount_micros: int = ...,
        regulatory_costs_subtotal_amount_micros: int = ...,
        regulatory_costs_tax_amount_micros: int = ...,
        regulatory_costs_total_amount_micros: int = ...,
        subtotal_amount_micros: int = ...,
        tax_amount_micros: int = ...,
        total_amount_micros: int = ...,
        corrected_invoice: str = ...,
        replaced_invoices: MutableSequence[str] = ...,
        pdf_url: str = ...,
        account_budget_summaries: MutableSequence[Invoice.AccountBudgetSummary] = ...,
        account_summaries: MutableSequence[Invoice.AccountSummary] = ...
    ) -> None: ...
