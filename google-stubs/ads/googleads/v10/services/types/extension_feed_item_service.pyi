from typing import Any

import proto
from google.protobuf.field_mask_pb2 import FieldMask
from google.rpc.status_pb2 import Status

from google.ads.googleads.v10.enums.types.response_content_type import (
    ResponseContentTypeEnum,
)
from google.ads.googleads.v10.resources.types.extension_feed_item import (
    ExtensionFeedItem,
)

class ExtensionFeedItemOperation(proto.Message):
    update_mask: FieldMask
    create: ExtensionFeedItem
    update: ExtensionFeedItem
    remove: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        update_mask: FieldMask = ...,
        create: ExtensionFeedItem = ...,
        update: ExtensionFeedItem = ...,
        remove: str = ...
    ) -> None: ...

class MutateExtensionFeedItemResult(proto.Message):
    resource_name: str
    extension_feed_item: ExtensionFeedItem
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        extension_feed_item: ExtensionFeedItem = ...
    ) -> None: ...

class MutateExtensionFeedItemsRequest(proto.Message):
    customer_id: str
    operations: list[ExtensionFeedItemOperation]
    partial_failure: bool
    validate_only: bool
    response_content_type: ResponseContentTypeEnum.ResponseContentType
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        customer_id: str = ...,
        operations: list[ExtensionFeedItemOperation] = ...,
        partial_failure: bool = ...,
        validate_only: bool = ...,
        response_content_type: ResponseContentTypeEnum.ResponseContentType = ...
    ) -> None: ...

class MutateExtensionFeedItemsResponse(proto.Message):
    partial_failure_error: Status
    results: list[MutateExtensionFeedItemResult]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        partial_failure_error: Status = ...,
        results: list[MutateExtensionFeedItemResult] = ...
    ) -> None: ...
