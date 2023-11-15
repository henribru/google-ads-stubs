from collections.abc import Mapping, MutableSequence
from typing import Any, TypeVar

import google.protobuf.message
import proto
from google.protobuf.field_mask_pb2 import FieldMask
from google.rpc.status_pb2 import Status

from google.ads.googleads.v14.resources.types.feed_item_set import FeedItemSet

_M = TypeVar("_M")

class FeedItemSetOperation(proto.Message):
    update_mask: FieldMask
    create: FeedItemSet
    update: FeedItemSet
    remove: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        update_mask: FieldMask = ...,
        create: FeedItemSet = ...,
        update: FeedItemSet = ...,
        remove: str = ...
    ) -> None: ...

class MutateFeedItemSetResult(proto.Message):
    resource_name: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...
    ) -> None: ...

class MutateFeedItemSetsRequest(proto.Message):
    customer_id: str
    operations: MutableSequence[FeedItemSetOperation]
    partial_failure: bool
    validate_only: bool
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        customer_id: str = ...,
        operations: MutableSequence[FeedItemSetOperation] = ...,
        partial_failure: bool = ...,
        validate_only: bool = ...
    ) -> None: ...

class MutateFeedItemSetsResponse(proto.Message):
    results: MutableSequence[MutateFeedItemSetResult]
    partial_failure_error: Status
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        results: MutableSequence[MutateFeedItemSetResult] = ...,
        partial_failure_error: Status = ...
    ) -> None: ...
