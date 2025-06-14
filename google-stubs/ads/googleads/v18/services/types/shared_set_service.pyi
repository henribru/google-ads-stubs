from google.ads.googleads.v18.resources.types.shared_set import SharedSet
from google.ads.googleads.v18.resources.types.shared_set import SharedSet
from google.protobuf.field_mask_pb2 import FieldMask
from collections.abc import MutableSequence
from google.rpc.status_pb2 import Status
from google.ads.googleads.v18.enums.types.response_content_type import ResponseContentTypeEnum
from collections.abc import MutableSequence
from google.ads.googleads.v18.resources.types.shared_set import SharedSet
import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class MutateSharedSetResult(proto.Message):
    resource_name: str
    shared_set: SharedSet
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., resource_name: str = ..., shared_set: SharedSet = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["resource_name", "shared_set"]) -> bool: ...
class MutateSharedSetsRequest(proto.Message):
    customer_id: str
    operations: MutableSequence[SharedSetOperation]
    partial_failure: bool
    validate_only: bool
    response_content_type: ResponseContentTypeEnum.ResponseContentType
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., customer_id: str = ..., operations: MutableSequence[SharedSetOperation] = ..., partial_failure: bool = ..., validate_only: bool = ..., response_content_type: ResponseContentTypeEnum.ResponseContentType = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["customer_id", "operations", "partial_failure", "validate_only", "response_content_type"]) -> bool: ...
class MutateSharedSetsResponse(proto.Message):
    partial_failure_error: Status
    results: MutableSequence[MutateSharedSetResult]
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., partial_failure_error: Status = ..., results: MutableSequence[MutateSharedSetResult] = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["partial_failure_error", "results"]) -> bool: ...
class SharedSetOperation(proto.Message):
    update_mask: FieldMask
    create: SharedSet
    update: SharedSet
    remove: str
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., update_mask: FieldMask = ..., create: SharedSet = ..., update: SharedSet = ..., remove: str = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["update_mask", "create", "update", "remove"]) -> bool: ...
