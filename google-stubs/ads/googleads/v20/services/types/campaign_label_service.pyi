from collections.abc import MutableSequence
from google.rpc.status_pb2 import Status
from collections.abc import MutableSequence
from google.ads.googleads.v20.resources.types.campaign_label import CampaignLabel
import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class CampaignLabelOperation(proto.Message):
    create: CampaignLabel
    remove: str
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, create: CampaignLabel = ..., remove: str = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["create", "remove"]) -> bool: ...
class MutateCampaignLabelResult(proto.Message):
    resource_name: str
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, resource_name: str = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["resource_name"]) -> bool: ...
class MutateCampaignLabelsRequest(proto.Message):
    customer_id: str
    operations: MutableSequence[CampaignLabelOperation]
    partial_failure: bool
    validate_only: bool
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, customer_id: str = ..., operations: MutableSequence[CampaignLabelOperation] = ..., partial_failure: bool = ..., validate_only: bool = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["customer_id", "operations", "partial_failure", "validate_only"]) -> bool: ...
class MutateCampaignLabelsResponse(proto.Message):
    partial_failure_error: Status
    results: MutableSequence[MutateCampaignLabelResult]
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, partial_failure_error: Status = ..., results: MutableSequence[MutateCampaignLabelResult] = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["partial_failure_error", "results"]) -> bool: ...
