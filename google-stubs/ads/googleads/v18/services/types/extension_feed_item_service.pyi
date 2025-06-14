from collections.abc import MutableSequence
from google.rpc.status_pb2 import Status
from google.ads.googleads.v18.enums.types.response_content_type import ResponseContentTypeEnum
from collections.abc import MutableSequence
from google.ads.googleads.v18.resources.types.extension_feed_item import ExtensionFeedItem
from google.ads.googleads.v18.resources.types.extension_feed_item import ExtensionFeedItem
from google.ads.googleads.v18.resources.types.extension_feed_item import ExtensionFeedItem
from google.protobuf.field_mask_pb2 import FieldMask
import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class ExtensionFeedItemOperation(proto.Message):
    update_mask: FieldMask
    create: ExtensionFeedItem
    update: ExtensionFeedItem
    remove: str
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., update_mask: FieldMask = ..., create: ExtensionFeedItem = ..., update: ExtensionFeedItem = ..., remove: str = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["update_mask", "create", "update", "remove"]) -> bool: ...
class MutateExtensionFeedItemResult(proto.Message):
    resource_name: str
    extension_feed_item: ExtensionFeedItem
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., resource_name: str = ..., extension_feed_item: ExtensionFeedItem = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["resource_name", "extension_feed_item"]) -> bool: ...
class MutateExtensionFeedItemsRequest(proto.Message):
    customer_id: str
    operations: MutableSequence[ExtensionFeedItemOperation]
    partial_failure: bool
    validate_only: bool
    response_content_type: ResponseContentTypeEnum.ResponseContentType
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., customer_id: str = ..., operations: MutableSequence[ExtensionFeedItemOperation] = ..., partial_failure: bool = ..., validate_only: bool = ..., response_content_type: ResponseContentTypeEnum.ResponseContentType = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["customer_id", "operations", "partial_failure", "validate_only", "response_content_type"]) -> bool: ...
class MutateExtensionFeedItemsResponse(proto.Message):
    partial_failure_error: Status
    results: MutableSequence[MutateExtensionFeedItemResult]
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., partial_failure_error: Status = ..., results: MutableSequence[MutateExtensionFeedItemResult] = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["partial_failure_error", "results"]) -> bool: ...
