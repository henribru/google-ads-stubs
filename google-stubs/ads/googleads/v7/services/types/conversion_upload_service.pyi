from typing import Any

import proto

__protobuf__: Any

class UploadClickConversionsRequest(proto.Message):
    customer_id: Any
    conversions: Any
    partial_failure: Any
    validate_only: Any

class UploadClickConversionsResponse(proto.Message):
    partial_failure_error: Any
    results: Any

class UploadCallConversionsRequest(proto.Message):
    customer_id: Any
    conversions: Any
    partial_failure: Any
    validate_only: Any

class UploadCallConversionsResponse(proto.Message):
    partial_failure_error: Any
    results: Any

class ClickConversion(proto.Message):
    gclid: Any
    conversion_action: Any
    conversion_date_time: Any
    conversion_value: Any
    currency_code: Any
    order_id: Any
    external_attribution_data: Any
    custom_variables: Any

class CallConversion(proto.Message):
    caller_id: Any
    call_start_date_time: Any
    conversion_action: Any
    conversion_date_time: Any
    conversion_value: Any
    currency_code: Any
    custom_variables: Any

class ExternalAttributionData(proto.Message):
    external_attribution_credit: Any
    external_attribution_model: Any

class ClickConversionResult(proto.Message):
    gclid: Any
    conversion_action: Any
    conversion_date_time: Any

class CallConversionResult(proto.Message):
    caller_id: Any
    call_start_date_time: Any
    conversion_action: Any
    conversion_date_time: Any

class CustomVariable(proto.Message):
    conversion_custom_variable: Any
    value: Any
