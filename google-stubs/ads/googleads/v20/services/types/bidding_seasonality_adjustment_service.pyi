from google.ads.googleads.v20.resources.types.bidding_seasonality_adjustment import BiddingSeasonalityAdjustment
from collections.abc import MutableSequence
from google.rpc.status_pb2 import Status
from google.ads.googleads.v20.enums.types.response_content_type import ResponseContentTypeEnum
from collections.abc import MutableSequence
from google.ads.googleads.v20.resources.types.bidding_seasonality_adjustment import BiddingSeasonalityAdjustment
from google.ads.googleads.v20.resources.types.bidding_seasonality_adjustment import BiddingSeasonalityAdjustment
from google.protobuf.field_mask_pb2 import FieldMask
import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class BiddingSeasonalityAdjustmentOperation(proto.Message):
    update_mask: FieldMask
    create: BiddingSeasonalityAdjustment
    update: BiddingSeasonalityAdjustment
    remove: str
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., update_mask: FieldMask = ..., create: BiddingSeasonalityAdjustment = ..., update: BiddingSeasonalityAdjustment = ..., remove: str = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["update_mask", "create", "update", "remove"]) -> bool: ...
class MutateBiddingSeasonalityAdjustmentsRequest(proto.Message):
    customer_id: str
    operations: MutableSequence[BiddingSeasonalityAdjustmentOperation]
    partial_failure: bool
    validate_only: bool
    response_content_type: ResponseContentTypeEnum.ResponseContentType
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., customer_id: str = ..., operations: MutableSequence[BiddingSeasonalityAdjustmentOperation] = ..., partial_failure: bool = ..., validate_only: bool = ..., response_content_type: ResponseContentTypeEnum.ResponseContentType = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["customer_id", "operations", "partial_failure", "validate_only", "response_content_type"]) -> bool: ...
class MutateBiddingSeasonalityAdjustmentsResponse(proto.Message):
    partial_failure_error: Status
    results: MutableSequence[MutateBiddingSeasonalityAdjustmentsResult]
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., partial_failure_error: Status = ..., results: MutableSequence[MutateBiddingSeasonalityAdjustmentsResult] = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["partial_failure_error", "results"]) -> bool: ...
class MutateBiddingSeasonalityAdjustmentsResult(proto.Message):
    resource_name: str
    bidding_seasonality_adjustment: BiddingSeasonalityAdjustment
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., resource_name: str = ..., bidding_seasonality_adjustment: BiddingSeasonalityAdjustment = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["resource_name", "bidding_seasonality_adjustment"]) -> bool: ...
