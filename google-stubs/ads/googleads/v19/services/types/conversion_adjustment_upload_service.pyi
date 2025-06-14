from collections.abc import MutableSequence
from google.rpc.status_pb2 import Status
from collections.abc import MutableSequence
from google.ads.googleads.v19.enums.types.conversion_adjustment_type import ConversionAdjustmentTypeEnum
from collections.abc import MutableSequence
from google.ads.googleads.v19.common.types.offline_user_data import UserIdentifier
from google.ads.googleads.v19.enums.types.conversion_adjustment_type import ConversionAdjustmentTypeEnum
import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class ConversionAdjustment(proto.Message):
    gclid_date_time_pair: GclidDateTimePair
    order_id: str
    conversion_action: str
    adjustment_date_time: str
    adjustment_type: ConversionAdjustmentTypeEnum.ConversionAdjustmentType
    restatement_value: RestatementValue
    user_identifiers: MutableSequence[UserIdentifier]
    user_agent: str
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., gclid_date_time_pair: GclidDateTimePair = ..., order_id: str = ..., conversion_action: str = ..., adjustment_date_time: str = ..., adjustment_type: ConversionAdjustmentTypeEnum.ConversionAdjustmentType = ..., restatement_value: RestatementValue = ..., user_identifiers: MutableSequence[UserIdentifier] = ..., user_agent: str = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["gclid_date_time_pair", "order_id", "conversion_action", "adjustment_date_time", "adjustment_type", "restatement_value", "user_identifiers", "user_agent"]) -> bool: ...
class ConversionAdjustmentResult(proto.Message):
    gclid_date_time_pair: GclidDateTimePair
    order_id: str
    conversion_action: str
    adjustment_date_time: str
    adjustment_type: ConversionAdjustmentTypeEnum.ConversionAdjustmentType
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., gclid_date_time_pair: GclidDateTimePair = ..., order_id: str = ..., conversion_action: str = ..., adjustment_date_time: str = ..., adjustment_type: ConversionAdjustmentTypeEnum.ConversionAdjustmentType = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["gclid_date_time_pair", "order_id", "conversion_action", "adjustment_date_time", "adjustment_type"]) -> bool: ...
class GclidDateTimePair(proto.Message):
    gclid: str
    conversion_date_time: str
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., gclid: str = ..., conversion_date_time: str = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["gclid", "conversion_date_time"]) -> bool: ...
class RestatementValue(proto.Message):
    adjusted_value: float
    currency_code: str
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., adjusted_value: float = ..., currency_code: str = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["adjusted_value", "currency_code"]) -> bool: ...
class UploadConversionAdjustmentsRequest(proto.Message):
    customer_id: str
    conversion_adjustments: MutableSequence[ConversionAdjustment]
    partial_failure: bool
    validate_only: bool
    job_id: int
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., customer_id: str = ..., conversion_adjustments: MutableSequence[ConversionAdjustment] = ..., partial_failure: bool = ..., validate_only: bool = ..., job_id: int = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["customer_id", "conversion_adjustments", "partial_failure", "validate_only", "job_id"]) -> bool: ...
class UploadConversionAdjustmentsResponse(proto.Message):
    partial_failure_error: Status
    results: MutableSequence[ConversionAdjustmentResult]
    job_id: int
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., partial_failure_error: Status = ..., results: MutableSequence[ConversionAdjustmentResult] = ..., job_id: int = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["partial_failure_error", "results", "job_id"]) -> bool: ...
