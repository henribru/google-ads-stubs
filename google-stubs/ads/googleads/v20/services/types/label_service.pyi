from collections.abc import MutableSequence
from google.rpc.status_pb2 import Status
from google.ads.googleads.v20.enums.types.response_content_type import ResponseContentTypeEnum
from collections.abc import MutableSequence
from google.ads.googleads.v20.resources.types.label import Label
from google.ads.googleads.v20.resources.types.label import Label
from google.ads.googleads.v20.resources.types.label import Label
from google.protobuf.field_mask_pb2 import FieldMask
import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class LabelOperation(proto.Message):
    update_mask: FieldMask
    create: Label
    update: Label
    remove: str
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, update_mask: FieldMask = ..., create: Label = ..., update: Label = ..., remove: str = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["update_mask", "create", "update", "remove"]) -> bool: ...
class MutateLabelResult(proto.Message):
    resource_name: str
    label: Label
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, resource_name: str = ..., label: Label = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["resource_name", "label"]) -> bool: ...
class MutateLabelsRequest(proto.Message):
    customer_id: str
    operations: MutableSequence[LabelOperation]
    partial_failure: bool
    validate_only: bool
    response_content_type: ResponseContentTypeEnum.ResponseContentType
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, customer_id: str = ..., operations: MutableSequence[LabelOperation] = ..., partial_failure: bool = ..., validate_only: bool = ..., response_content_type: ResponseContentTypeEnum.ResponseContentType = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["customer_id", "operations", "partial_failure", "validate_only", "response_content_type"]) -> bool: ...
class MutateLabelsResponse(proto.Message):
    partial_failure_error: Status
    results: MutableSequence[MutateLabelResult]
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, partial_failure_error: Status = ..., results: MutableSequence[MutateLabelResult] = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["partial_failure_error", "results"]) -> bool: ...
