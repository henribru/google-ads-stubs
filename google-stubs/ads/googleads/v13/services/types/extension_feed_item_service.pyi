from collections.abc import Mapping, MutableSequence
from typing import Any, TypeVar

import google.protobuf.message
import proto
from google.protobuf.field_mask_pb2 import FieldMask
from google.rpc.status_pb2 import Status

from google.ads.googleads.v13.enums.types.response_content_type import (
    ResponseContentTypeEnum,
)
from google.ads.googleads.v13.resources.types.extension_feed_item import (
    ExtensionFeedItem,
)

_M = TypeVar("_M")

class ExtensionFeedItemOperation(proto.Message):
    update_mask: FieldMask
    create: ExtensionFeedItem
    update: ExtensionFeedItem
    remove: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        update_mask: FieldMask = ...,
        create: ExtensionFeedItem = ...,
        update: ExtensionFeedItem = ...,
        remove: str = ...
    ) -> None: ...

class MutateExtensionFeedItemResult(proto.Message):
    resource_name: str
    extension_feed_item: ExtensionFeedItem
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        extension_feed_item: ExtensionFeedItem = ...
    ) -> None: ...

class MutateExtensionFeedItemsRequest(proto.Message):
    customer_id: str
    operations: MutableSequence[ExtensionFeedItemOperation]
    partial_failure: bool
    validate_only: bool
    response_content_type: ResponseContentTypeEnum.ResponseContentType
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        customer_id: str = ...,
        operations: MutableSequence[ExtensionFeedItemOperation] = ...,
        partial_failure: bool = ...,
        validate_only: bool = ...,
        response_content_type: ResponseContentTypeEnum.ResponseContentType = ...
    ) -> None: ...

class MutateExtensionFeedItemsResponse(proto.Message):
    partial_failure_error: Status
    results: MutableSequence[MutateExtensionFeedItemResult]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        partial_failure_error: Status = ...,
        results: MutableSequence[MutateExtensionFeedItemResult] = ...
    ) -> None: ...
