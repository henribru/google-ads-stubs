import proto
from _typeshed import Incomplete

from google.ads.googleads.v10.enums.types import (
    conversion_tracking_status_enum as conversion_tracking_status_enum,
    customer_pay_per_conversion_eligibility_failure_reason as customer_pay_per_conversion_eligibility_failure_reason,
    customer_status as customer_status,
)

__protobuf__: Incomplete

class Customer(proto.Message):
    resource_name: Incomplete
    id: Incomplete
    descriptive_name: Incomplete
    currency_code: Incomplete
    time_zone: Incomplete
    tracking_url_template: Incomplete
    final_url_suffix: Incomplete
    auto_tagging_enabled: Incomplete
    has_partners_badge: Incomplete
    manager: Incomplete
    test_account: Incomplete
    call_reporting_setting: Incomplete
    conversion_tracking_setting: Incomplete
    remarketing_setting: Incomplete
    pay_per_conversion_eligibility_failure_reasons: Incomplete
    optimization_score: Incomplete
    optimization_score_weight: Incomplete
    status: Incomplete

class CallReportingSetting(proto.Message):
    call_reporting_enabled: Incomplete
    call_conversion_reporting_enabled: Incomplete
    call_conversion_action: Incomplete

class ConversionTrackingSetting(proto.Message):
    conversion_tracking_id: Incomplete
    cross_account_conversion_tracking_id: Incomplete
    accepted_customer_data_terms: Incomplete
    conversion_tracking_status: Incomplete
    enhanced_conversions_for_leads_enabled: Incomplete
    google_ads_conversion_customer: Incomplete

class RemarketingSetting(proto.Message):
    google_global_site_tag: Incomplete
