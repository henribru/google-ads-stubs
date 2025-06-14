from collections.abc import MutableSequence
from google.rpc.status_pb2 import Status
from collections.abc import MutableSequence
from google.ads.googleads.v20.resources.types.ad_group_label import AdGroupLabel
import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class AdGroupLabelOperation(proto.Message):
    create: AdGroupLabel
    remove: str
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, create: AdGroupLabel = ..., remove: str = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["create", "remove"]) -> bool: ...
class MutateAdGroupLabelResult(proto.Message):
    resource_name: str
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, resource_name: str = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["resource_name"]) -> bool: ...
class MutateAdGroupLabelsRequest(proto.Message):
    customer_id: str
    operations: MutableSequence[AdGroupLabelOperation]
    partial_failure: bool
    validate_only: bool
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, customer_id: str = ..., operations: MutableSequence[AdGroupLabelOperation] = ..., partial_failure: bool = ..., validate_only: bool = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["customer_id", "operations", "partial_failure", "validate_only"]) -> bool: ...
class MutateAdGroupLabelsResponse(proto.Message):
    partial_failure_error: Status
    results: MutableSequence[MutateAdGroupLabelResult]
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, partial_failure_error: Status = ..., results: MutableSequence[MutateAdGroupLabelResult] = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["partial_failure_error", "results"]) -> bool: ...
