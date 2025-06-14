from collections.abc import MutableSequence
from google.rpc.status_pb2 import Status
from collections.abc import MutableSequence
from collections.abc import MutableSequence
from google.rpc.status_pb2 import Status
from collections.abc import MutableSequence
from google.ads.googleads.v19.resources.types.experiment import Experiment
from google.ads.googleads.v19.resources.types.experiment import Experiment
from google.protobuf.field_mask_pb2 import FieldMask
import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class CampaignBudgetMapping(proto.Message):
    experiment_campaign: str
    campaign_budget: str
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, experiment_campaign: str = ..., campaign_budget: str = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["experiment_campaign", "campaign_budget"]) -> bool: ...
class EndExperimentRequest(proto.Message):
    experiment: str
    validate_only: bool
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, experiment: str = ..., validate_only: bool = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["experiment", "validate_only"]) -> bool: ...
class ExperimentOperation(proto.Message):
    update_mask: FieldMask
    create: Experiment
    update: Experiment
    remove: str
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, update_mask: FieldMask = ..., create: Experiment = ..., update: Experiment = ..., remove: str = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["update_mask", "create", "update", "remove"]) -> bool: ...
class GraduateExperimentRequest(proto.Message):
    experiment: str
    campaign_budget_mappings: MutableSequence[CampaignBudgetMapping]
    validate_only: bool
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, experiment: str = ..., campaign_budget_mappings: MutableSequence[CampaignBudgetMapping] = ..., validate_only: bool = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["experiment", "campaign_budget_mappings", "validate_only"]) -> bool: ...
class ListExperimentAsyncErrorsRequest(proto.Message):
    resource_name: str
    page_token: str
    page_size: int
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, resource_name: str = ..., page_token: str = ..., page_size: int = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["resource_name", "page_token", "page_size"]) -> bool: ...
class ListExperimentAsyncErrorsResponse(proto.Message):
    errors: MutableSequence[Status]
    next_page_token: str
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, errors: MutableSequence[Status] = ..., next_page_token: str = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["errors", "next_page_token"]) -> bool: ...
class MutateExperimentResult(proto.Message):
    resource_name: str
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, resource_name: str = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["resource_name"]) -> bool: ...
class MutateExperimentsRequest(proto.Message):
    customer_id: str
    operations: MutableSequence[ExperimentOperation]
    partial_failure: bool
    validate_only: bool
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, customer_id: str = ..., operations: MutableSequence[ExperimentOperation] = ..., partial_failure: bool = ..., validate_only: bool = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["customer_id", "operations", "partial_failure", "validate_only"]) -> bool: ...
class MutateExperimentsResponse(proto.Message):
    partial_failure_error: Status
    results: MutableSequence[MutateExperimentResult]
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, partial_failure_error: Status = ..., results: MutableSequence[MutateExperimentResult] = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["partial_failure_error", "results"]) -> bool: ...
class PromoteExperimentMetadata(proto.Message):
    experiment: str
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, experiment: str = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["experiment"]) -> bool: ...
class PromoteExperimentRequest(proto.Message):
    resource_name: str
    validate_only: bool
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, resource_name: str = ..., validate_only: bool = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["resource_name", "validate_only"]) -> bool: ...
class ScheduleExperimentMetadata(proto.Message):
    experiment: str
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, experiment: str = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["experiment"]) -> bool: ...
class ScheduleExperimentRequest(proto.Message):
    resource_name: str
    validate_only: bool
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, resource_name: str = ..., validate_only: bool = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["resource_name", "validate_only"]) -> bool: ...
