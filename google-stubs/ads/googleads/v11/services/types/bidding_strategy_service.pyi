from typing import Any

import proto
from google.protobuf.field_mask_pb2 import FieldMask
from google.rpc.status_pb2 import Status

from google.ads.googleads.v11.enums.types.response_content_type import (
    ResponseContentTypeEnum,
)
from google.ads.googleads.v11.resources.types.bidding_strategy import BiddingStrategy

class BiddingStrategyOperation(proto.Message):
    update_mask: FieldMask
    create: BiddingStrategy
    update: BiddingStrategy
    remove: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        update_mask: FieldMask = ...,
        create: BiddingStrategy = ...,
        update: BiddingStrategy = ...,
        remove: str = ...
    ) -> None: ...

class MutateBiddingStrategiesRequest(proto.Message):
    customer_id: str
    operations: list[BiddingStrategyOperation]
    partial_failure: bool
    validate_only: bool
    response_content_type: ResponseContentTypeEnum.ResponseContentType
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        customer_id: str = ...,
        operations: list[BiddingStrategyOperation] = ...,
        partial_failure: bool = ...,
        validate_only: bool = ...,
        response_content_type: ResponseContentTypeEnum.ResponseContentType = ...
    ) -> None: ...

class MutateBiddingStrategiesResponse(proto.Message):
    partial_failure_error: Status
    results: list[MutateBiddingStrategyResult]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        partial_failure_error: Status = ...,
        results: list[MutateBiddingStrategyResult] = ...
    ) -> None: ...

class MutateBiddingStrategyResult(proto.Message):
    resource_name: str
    bidding_strategy: BiddingStrategy
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        bidding_strategy: BiddingStrategy = ...
    ) -> None: ...
