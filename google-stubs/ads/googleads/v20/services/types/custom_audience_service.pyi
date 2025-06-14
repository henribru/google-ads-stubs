from collections.abc import MutableSequence
from collections.abc import MutableSequence
from google.ads.googleads.v20.resources.types.custom_audience import CustomAudience
from google.ads.googleads.v20.resources.types.custom_audience import CustomAudience
from google.protobuf.field_mask_pb2 import FieldMask
import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class CustomAudienceOperation(proto.Message):
    update_mask: FieldMask
    create: CustomAudience
    update: CustomAudience
    remove: str
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, update_mask: FieldMask = ..., create: CustomAudience = ..., update: CustomAudience = ..., remove: str = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["update_mask", "create", "update", "remove"]) -> bool: ...
class MutateCustomAudienceResult(proto.Message):
    resource_name: str
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, resource_name: str = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["resource_name"]) -> bool: ...
class MutateCustomAudiencesRequest(proto.Message):
    customer_id: str
    operations: MutableSequence[CustomAudienceOperation]
    validate_only: bool
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, customer_id: str = ..., operations: MutableSequence[CustomAudienceOperation] = ..., validate_only: bool = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["customer_id", "operations", "validate_only"]) -> bool: ...
class MutateCustomAudiencesResponse(proto.Message):
    results: MutableSequence[MutateCustomAudienceResult]
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, results: MutableSequence[MutateCustomAudienceResult] = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["results"]) -> bool: ...
