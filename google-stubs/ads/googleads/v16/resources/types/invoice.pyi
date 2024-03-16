from collections.abc import Mapping, MutableSequence
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v16.common.types.dates import DateRange
from google.ads.googleads.v16.enums.types.invoice_type import InvoiceTypeEnum
from google.ads.googleads.v16.enums.types.month_of_year import MonthOfYearEnum

_M = TypeVar("_M")

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
        invalid_activity_summaries: MutableSequence[Invoice.InvalidActivitySummary]
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
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
            invalid_activity_amount_micros: int = ...,
            invalid_activity_summaries: MutableSequence[
                Invoice.InvalidActivitySummary
            ] = ...,
        ) -> None: ...
        def __contains__(  # type: ignore[override]
            self,
            key: Literal[
                "customer",
                "customer_descriptive_name",
                "account_budget",
                "account_budget_name",
                "purchase_order_number",
                "subtotal_amount_micros",
                "tax_amount_micros",
                "total_amount_micros",
                "billable_activity_date_range",
                "served_amount_micros",
                "billed_amount_micros",
                "overdelivery_amount_micros",
                "invalid_activity_amount_micros",
                "invalid_activity_summaries",
            ],
        ) -> bool: ...

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
        export_charge_subtotal_amount_micros: int
        export_charge_tax_amount_micros: int
        export_charge_total_amount_micros: int
        subtotal_amount_micros: int
        tax_amount_micros: int
        total_amount_micros: int
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
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
            export_charge_subtotal_amount_micros: int = ...,
            export_charge_tax_amount_micros: int = ...,
            export_charge_total_amount_micros: int = ...,
            subtotal_amount_micros: int = ...,
            tax_amount_micros: int = ...,
            total_amount_micros: int = ...,
        ) -> None: ...
        def __contains__(  # type: ignore[override]
            self,
            key: Literal[
                "customer",
                "billing_correction_subtotal_amount_micros",
                "billing_correction_tax_amount_micros",
                "billing_correction_total_amount_micros",
                "coupon_adjustment_subtotal_amount_micros",
                "coupon_adjustment_tax_amount_micros",
                "coupon_adjustment_total_amount_micros",
                "excess_credit_adjustment_subtotal_amount_micros",
                "excess_credit_adjustment_tax_amount_micros",
                "excess_credit_adjustment_total_amount_micros",
                "regulatory_costs_subtotal_amount_micros",
                "regulatory_costs_tax_amount_micros",
                "regulatory_costs_total_amount_micros",
                "export_charge_subtotal_amount_micros",
                "export_charge_tax_amount_micros",
                "export_charge_total_amount_micros",
                "subtotal_amount_micros",
                "tax_amount_micros",
                "total_amount_micros",
            ],
        ) -> bool: ...

    class InvalidActivitySummary(proto.Message):
        original_month_of_service: MonthOfYearEnum.MonthOfYear
        original_year_of_service: str
        original_invoice_id: str
        original_account_budget_name: str
        original_purchase_order_number: str
        amount_micros: int
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
            original_month_of_service: MonthOfYearEnum.MonthOfYear = ...,
            original_year_of_service: str = ...,
            original_invoice_id: str = ...,
            original_account_budget_name: str = ...,
            original_purchase_order_number: str = ...,
            amount_micros: int = ...,
        ) -> None: ...
        def __contains__(  # type: ignore[override]
            self,
            key: Literal[
                "original_month_of_service",
                "original_year_of_service",
                "original_invoice_id",
                "original_account_budget_name",
                "original_purchase_order_number",
                "amount_micros",
            ],
        ) -> bool: ...

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
    export_charge_subtotal_amount_micros: int
    export_charge_tax_amount_micros: int
    export_charge_total_amount_micros: int
    subtotal_amount_micros: int
    tax_amount_micros: int
    total_amount_micros: int
    corrected_invoice: str
    replaced_invoices: MutableSequence[str]
    pdf_url: str
    account_budget_summaries: MutableSequence[Invoice.AccountBudgetSummary]
    account_summaries: MutableSequence[Invoice.AccountSummary]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
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
        export_charge_subtotal_amount_micros: int = ...,
        export_charge_tax_amount_micros: int = ...,
        export_charge_total_amount_micros: int = ...,
        subtotal_amount_micros: int = ...,
        tax_amount_micros: int = ...,
        total_amount_micros: int = ...,
        corrected_invoice: str = ...,
        replaced_invoices: MutableSequence[str] = ...,
        pdf_url: str = ...,
        account_budget_summaries: MutableSequence[Invoice.AccountBudgetSummary] = ...,
        account_summaries: MutableSequence[Invoice.AccountSummary] = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "resource_name",
            "id",
            "type_",
            "billing_setup",
            "payments_account_id",
            "payments_profile_id",
            "issue_date",
            "due_date",
            "service_date_range",
            "currency_code",
            "adjustments_subtotal_amount_micros",
            "adjustments_tax_amount_micros",
            "adjustments_total_amount_micros",
            "regulatory_costs_subtotal_amount_micros",
            "regulatory_costs_tax_amount_micros",
            "regulatory_costs_total_amount_micros",
            "export_charge_subtotal_amount_micros",
            "export_charge_tax_amount_micros",
            "export_charge_total_amount_micros",
            "subtotal_amount_micros",
            "tax_amount_micros",
            "total_amount_micros",
            "corrected_invoice",
            "replaced_invoices",
            "pdf_url",
            "account_budget_summaries",
            "account_summaries",
        ],
    ) -> bool: ...
