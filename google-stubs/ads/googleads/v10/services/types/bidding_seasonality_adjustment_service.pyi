from typing import Any

import proto
from google.protobuf.field_mask_pb2 import FieldMask
from google.rpc.status_pb2 import Status

from google.ads.googleads.v10.enums.types.response_content_type import (
    ResponseContentTypeEnum,
)
from google.ads.googleads.v10.resources.types.bidding_seasonality_adjustment import (
    BiddingSeasonalityAdjustment,
)

class BiddingSeasonalityAdjustmentOperation(proto.Message):
    update_mask: FieldMask
    create: BiddingSeasonalityAdjustment
    update: BiddingSeasonalityAdjustment
    remove: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        update_mask: FieldMask = ...,
        create: BiddingSeasonalityAdjustment = ...,
        update: BiddingSeasonalityAdjustment = ...,
        remove: str = ...
    ) -> None: ...

class MutateBiddingSeasonalityAdjustmentsRequest(proto.Message):
    customer_id: str
    operations: list[BiddingSeasonalityAdjustmentOperation]
    partial_failure: bool
    validate_only: bool
    response_content_type: ResponseContentTypeEnum.ResponseContentType
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        customer_id: str = ...,
        operations: list[BiddingSeasonalityAdjustmentOperation] = ...,
        partial_failure: bool = ...,
        validate_only: bool = ...,
        response_content_type: ResponseContentTypeEnum.ResponseContentType = ...
    ) -> None: ...

class MutateBiddingSeasonalityAdjustmentsResponse(proto.Message):
    partial_failure_error: Status
    results: list[MutateBiddingSeasonalityAdjustmentsResult]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        partial_failure_error: Status = ...,
        results: list[MutateBiddingSeasonalityAdjustmentsResult] = ...
    ) -> None: ...

class MutateBiddingSeasonalityAdjustmentsResult(proto.Message):
    resource_name: str
    bidding_seasonality_adjustment: BiddingSeasonalityAdjustment
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        bidding_seasonality_adjustment: BiddingSeasonalityAdjustment = ...
    ) -> None: ...
