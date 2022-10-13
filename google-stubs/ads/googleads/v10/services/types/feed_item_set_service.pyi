from typing import Any

import proto
from google.protobuf.field_mask_pb2 import FieldMask
from google.rpc.status_pb2 import Status

from google.ads.googleads.v10.resources.types.feed_item_set import FeedItemSet

class FeedItemSetOperation(proto.Message):
    update_mask: FieldMask
    create: FeedItemSet
    update: FeedItemSet
    remove: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        update_mask: FieldMask = ...,
        create: FeedItemSet = ...,
        update: FeedItemSet = ...,
        remove: str = ...
    ) -> None: ...

class MutateFeedItemSetResult(proto.Message):
    resource_name: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...
    ) -> None: ...

class MutateFeedItemSetsRequest(proto.Message):
    customer_id: str
    operations: list[FeedItemSetOperation]
    partial_failure: bool
    validate_only: bool
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        customer_id: str = ...,
        operations: list[FeedItemSetOperation] = ...,
        partial_failure: bool = ...,
        validate_only: bool = ...
    ) -> None: ...

class MutateFeedItemSetsResponse(proto.Message):
    results: list[MutateFeedItemSetResult]
    partial_failure_error: Status
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        results: list[MutateFeedItemSetResult] = ...,
        partial_failure_error: Status = ...
    ) -> None: ...
