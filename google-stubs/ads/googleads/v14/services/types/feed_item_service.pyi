from collections.abc import Mapping, MutableSequence
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from google.protobuf.field_mask_pb2 import FieldMask
from google.rpc.status_pb2 import Status
from typing_extensions import Literal

from google.ads.googleads.v14.enums.types.response_content_type import (
    ResponseContentTypeEnum,
)
from google.ads.googleads.v14.resources.types.feed_item import FeedItem

_M = TypeVar("_M")

class FeedItemOperation(proto.Message):
    update_mask: FieldMask
    create: FeedItem
    update: FeedItem
    remove: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        update_mask: FieldMask = ...,
        create: FeedItem = ...,
        update: FeedItem = ...,
        remove: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["update_mask", "create", "update", "remove"]
    ) -> bool: ...

class MutateFeedItemResult(proto.Message):
    resource_name: str
    feed_item: FeedItem
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        feed_item: FeedItem = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["resource_name", "feed_item"]
    ) -> bool: ...

class MutateFeedItemsRequest(proto.Message):
    customer_id: str
    operations: MutableSequence[FeedItemOperation]
    partial_failure: bool
    validate_only: bool
    response_content_type: ResponseContentTypeEnum.ResponseContentType
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        customer_id: str = ...,
        operations: MutableSequence[FeedItemOperation] = ...,
        partial_failure: bool = ...,
        validate_only: bool = ...,
        response_content_type: ResponseContentTypeEnum.ResponseContentType = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "customer_id",
            "operations",
            "partial_failure",
            "validate_only",
            "response_content_type",
        ],
    ) -> bool: ...

class MutateFeedItemsResponse(proto.Message):
    partial_failure_error: Status
    results: MutableSequence[MutateFeedItemResult]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        partial_failure_error: Status = ...,
        results: MutableSequence[MutateFeedItemResult] = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["partial_failure_error", "results"]
    ) -> bool: ...
