from collections.abc import Mapping, MutableSequence
from typing import Any, TypeVar

import google.protobuf.message
import proto
from google.protobuf.field_mask_pb2 import FieldMask
from google.rpc.status_pb2 import Status

from google.ads.googleads.v13.enums.types.response_content_type import (
    ResponseContentTypeEnum,
)
from google.ads.googleads.v13.resources.types.bidding_strategy import BiddingStrategy

_M = TypeVar("_M")

class BiddingStrategyOperation(proto.Message):
    update_mask: FieldMask
    create: BiddingStrategy
    update: BiddingStrategy
    remove: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        update_mask: FieldMask = ...,
        create: BiddingStrategy = ...,
        update: BiddingStrategy = ...,
        remove: str = ...
    ) -> None: ...

class MutateBiddingStrategiesRequest(proto.Message):
    customer_id: str
    operations: MutableSequence[BiddingStrategyOperation]
    partial_failure: bool
    validate_only: bool
    response_content_type: ResponseContentTypeEnum.ResponseContentType
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        customer_id: str = ...,
        operations: MutableSequence[BiddingStrategyOperation] = ...,
        partial_failure: bool = ...,
        validate_only: bool = ...,
        response_content_type: ResponseContentTypeEnum.ResponseContentType = ...
    ) -> None: ...

class MutateBiddingStrategiesResponse(proto.Message):
    partial_failure_error: Status
    results: MutableSequence[MutateBiddingStrategyResult]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        partial_failure_error: Status = ...,
        results: MutableSequence[MutateBiddingStrategyResult] = ...
    ) -> None: ...

class MutateBiddingStrategyResult(proto.Message):
    resource_name: str
    bidding_strategy: BiddingStrategy
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        bidding_strategy: BiddingStrategy = ...
    ) -> None: ...
