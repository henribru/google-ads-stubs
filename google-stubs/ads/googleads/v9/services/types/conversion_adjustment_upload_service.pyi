from typing import Any

import proto
from google.rpc import status_pb2 as status_pb2

from google.ads.googleads.v9.common.types import offline_user_data as offline_user_data
from google.ads.googleads.v9.enums.types import (
    conversion_adjustment_type as conversion_adjustment_type,
)

__protobuf__: Any

class UploadConversionAdjustmentsRequest(proto.Message):
    customer_id: Any
    conversion_adjustments: Any
    partial_failure: Any
    validate_only: Any

class UploadConversionAdjustmentsResponse(proto.Message):
    partial_failure_error: Any
    results: Any

class ConversionAdjustment(proto.Message):
    gclid_date_time_pair: Any
    order_id: Any
    conversion_action: Any
    adjustment_date_time: Any
    adjustment_type: Any
    restatement_value: Any
    user_identifiers: Any
    user_agent: Any

class RestatementValue(proto.Message):
    adjusted_value: Any
    currency_code: Any

class GclidDateTimePair(proto.Message):
    gclid: Any
    conversion_date_time: Any

class ConversionAdjustmentResult(proto.Message):
    gclid_date_time_pair: Any
    order_id: Any
    conversion_action: Any
    adjustment_date_time: Any
    adjustment_type: Any
