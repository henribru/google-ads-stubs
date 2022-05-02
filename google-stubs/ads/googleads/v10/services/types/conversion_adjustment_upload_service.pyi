import proto
from _typeshed import Incomplete
from google.rpc import status_pb2 as status_pb2

from google.ads.googleads.v10.common.types import offline_user_data as offline_user_data
from google.ads.googleads.v10.enums.types import (
    conversion_adjustment_type as conversion_adjustment_type,
)

__protobuf__: Incomplete

class UploadConversionAdjustmentsRequest(proto.Message):
    customer_id: Incomplete
    conversion_adjustments: Incomplete
    partial_failure: Incomplete
    validate_only: Incomplete

class UploadConversionAdjustmentsResponse(proto.Message):
    partial_failure_error: Incomplete
    results: Incomplete

class ConversionAdjustment(proto.Message):
    gclid_date_time_pair: Incomplete
    order_id: Incomplete
    conversion_action: Incomplete
    adjustment_date_time: Incomplete
    adjustment_type: Incomplete
    restatement_value: Incomplete
    user_identifiers: Incomplete
    user_agent: Incomplete

class RestatementValue(proto.Message):
    adjusted_value: Incomplete
    currency_code: Incomplete

class GclidDateTimePair(proto.Message):
    gclid: Incomplete
    conversion_date_time: Incomplete

class ConversionAdjustmentResult(proto.Message):
    gclid_date_time_pair: Incomplete
    order_id: Incomplete
    conversion_action: Incomplete
    adjustment_date_time: Incomplete
    adjustment_type: Incomplete
