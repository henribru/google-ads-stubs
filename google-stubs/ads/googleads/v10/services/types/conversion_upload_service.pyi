import proto
from _typeshed import Incomplete
from google.rpc import status_pb2 as status_pb2

from google.ads.googleads.v10.common.types import offline_user_data as offline_user_data
from google.ads.googleads.v10.enums.types import (
    conversion_environment_enum as conversion_environment_enum,
)

__protobuf__: Incomplete

class UploadClickConversionsRequest(proto.Message):
    customer_id: Incomplete
    conversions: Incomplete
    partial_failure: Incomplete
    validate_only: Incomplete

class UploadClickConversionsResponse(proto.Message):
    partial_failure_error: Incomplete
    results: Incomplete

class UploadCallConversionsRequest(proto.Message):
    customer_id: Incomplete
    conversions: Incomplete
    partial_failure: Incomplete
    validate_only: Incomplete

class UploadCallConversionsResponse(proto.Message):
    partial_failure_error: Incomplete
    results: Incomplete

class ClickConversion(proto.Message):
    gclid: Incomplete
    gbraid: Incomplete
    wbraid: Incomplete
    conversion_action: Incomplete
    conversion_date_time: Incomplete
    conversion_value: Incomplete
    currency_code: Incomplete
    order_id: Incomplete
    external_attribution_data: Incomplete
    custom_variables: Incomplete
    cart_data: Incomplete
    user_identifiers: Incomplete
    conversion_environment: Incomplete

class CallConversion(proto.Message):
    caller_id: Incomplete
    call_start_date_time: Incomplete
    conversion_action: Incomplete
    conversion_date_time: Incomplete
    conversion_value: Incomplete
    currency_code: Incomplete
    custom_variables: Incomplete

class ExternalAttributionData(proto.Message):
    external_attribution_credit: Incomplete
    external_attribution_model: Incomplete

class ClickConversionResult(proto.Message):
    gclid: Incomplete
    gbraid: Incomplete
    wbraid: Incomplete
    conversion_action: Incomplete
    conversion_date_time: Incomplete
    user_identifiers: Incomplete

class CallConversionResult(proto.Message):
    caller_id: Incomplete
    call_start_date_time: Incomplete
    conversion_action: Incomplete
    conversion_date_time: Incomplete

class CustomVariable(proto.Message):
    conversion_custom_variable: Incomplete
    value: Incomplete

class CartData(proto.Message):
    class Item(proto.Message):
        product_id: Incomplete
        quantity: Incomplete
        unit_price: Incomplete
    merchant_id: Incomplete
    feed_country_code: Incomplete
    feed_language_code: Incomplete
    local_transaction_cost: Incomplete
    items: Incomplete
