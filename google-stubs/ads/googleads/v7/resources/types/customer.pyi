from typing import Any

import proto

from google.ads.googleads.v7.enums.types import (
    customer_pay_per_conversion_eligibility_failure_reason as customer_pay_per_conversion_eligibility_failure_reason,
)

__protobuf__: Any

class Customer(proto.Message):
    resource_name: Any
    id: Any
    descriptive_name: Any
    currency_code: Any
    time_zone: Any
    tracking_url_template: Any
    final_url_suffix: Any
    auto_tagging_enabled: Any
    has_partners_badge: Any
    manager: Any
    test_account: Any
    call_reporting_setting: Any
    conversion_tracking_setting: Any
    remarketing_setting: Any
    pay_per_conversion_eligibility_failure_reasons: Any
    optimization_score: Any
    optimization_score_weight: Any

class CallReportingSetting(proto.Message):
    call_reporting_enabled: Any
    call_conversion_reporting_enabled: Any
    call_conversion_action: Any

class ConversionTrackingSetting(proto.Message):
    conversion_tracking_id: Any
    cross_account_conversion_tracking_id: Any

class RemarketingSetting(proto.Message):
    google_global_site_tag: Any
