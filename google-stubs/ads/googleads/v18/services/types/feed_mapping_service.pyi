from collections.abc import MutableSequence
from google.rpc.status_pb2 import Status
from google.ads.googleads.v18.enums.types.response_content_type import ResponseContentTypeEnum
from collections.abc import MutableSequence
from google.ads.googleads.v18.resources.types.feed_mapping import FeedMapping
from google.ads.googleads.v18.resources.types.feed_mapping import FeedMapping
import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class FeedMappingOperation(proto.Message):
    create: FeedMapping
    remove: str
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., create: FeedMapping = ..., remove: str = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["create", "remove"]) -> bool: ...
class MutateFeedMappingResult(proto.Message):
    resource_name: str
    feed_mapping: FeedMapping
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., resource_name: str = ..., feed_mapping: FeedMapping = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["resource_name", "feed_mapping"]) -> bool: ...
class MutateFeedMappingsRequest(proto.Message):
    customer_id: str
    operations: MutableSequence[FeedMappingOperation]
    partial_failure: bool
    validate_only: bool
    response_content_type: ResponseContentTypeEnum.ResponseContentType
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., customer_id: str = ..., operations: MutableSequence[FeedMappingOperation] = ..., partial_failure: bool = ..., validate_only: bool = ..., response_content_type: ResponseContentTypeEnum.ResponseContentType = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["customer_id", "operations", "partial_failure", "validate_only", "response_content_type"]) -> bool: ...
class MutateFeedMappingsResponse(proto.Message):
    partial_failure_error: Status
    results: MutableSequence[MutateFeedMappingResult]
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., partial_failure_error: Status = ..., results: MutableSequence[MutateFeedMappingResult] = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["partial_failure_error", "results"]) -> bool: ...
