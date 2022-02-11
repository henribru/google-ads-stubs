from typing import Any

import proto
from google.rpc import status_pb2 as status_pb2

from google.ads.googleads.v9.common.types import offline_user_data as offline_user_data

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
    gbraid: Any
    wbraid: Any
    conversion_action: Any
    conversion_date_time: Any
    conversion_value: Any
    currency_code: Any
    order_id: Any
    external_attribution_data: Any
    custom_variables: Any
    cart_data: Any
    user_identifiers: Any

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
    gbraid: Any
    wbraid: Any
    conversion_action: Any
    conversion_date_time: Any
    user_identifiers: Any

class CallConversionResult(proto.Message):
    caller_id: Any
    call_start_date_time: Any
    conversion_action: Any
    conversion_date_time: Any

class CustomVariable(proto.Message):
    conversion_custom_variable: Any
    value: Any

class CartData(proto.Message):
    class Item(proto.Message):
        product_id: Any
        quantity: Any
        unit_price: Any
    merchant_id: Any
    feed_country_code: Any
    feed_language_code: Any
    local_transaction_cost: Any
    items: Any
