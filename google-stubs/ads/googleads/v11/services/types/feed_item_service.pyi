from typing import Any

import proto
from google.protobuf.field_mask_pb2 import FieldMask
from google.rpc.status_pb2 import Status

from google.ads.googleads.v11.enums.types.response_content_type import (
    ResponseContentTypeEnum,
)
from google.ads.googleads.v11.resources.types.feed_item import FeedItem

class FeedItemOperation(proto.Message):
    update_mask: FieldMask
    create: FeedItem
    update: FeedItem
    remove: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        update_mask: FieldMask = ...,
        create: FeedItem = ...,
        update: FeedItem = ...,
        remove: str = ...
    ) -> None: ...

class MutateFeedItemResult(proto.Message):
    resource_name: str
    feed_item: FeedItem
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        feed_item: FeedItem = ...
    ) -> None: ...

class MutateFeedItemsRequest(proto.Message):
    customer_id: str
    operations: list[FeedItemOperation]
    partial_failure: bool
    validate_only: bool
    response_content_type: ResponseContentTypeEnum.ResponseContentType
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        customer_id: str = ...,
        operations: list[FeedItemOperation] = ...,
        partial_failure: bool = ...,
        validate_only: bool = ...,
        response_content_type: ResponseContentTypeEnum.ResponseContentType = ...
    ) -> None: ...

class MutateFeedItemsResponse(proto.Message):
    partial_failure_error: Status
    results: list[MutateFeedItemResult]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        partial_failure_error: Status = ...,
        results: list[MutateFeedItemResult] = ...
    ) -> None: ...
