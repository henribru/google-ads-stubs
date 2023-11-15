from collections.abc import Mapping, MutableSequence
from typing import Any, TypeVar

import google.protobuf.message
import proto
from google.protobuf.field_mask_pb2 import FieldMask
from google.rpc.status_pb2 import Status

from google.ads.googleads.v14.resources.types.experiment import Experiment

_M = TypeVar("_M")

class CampaignBudgetMapping(proto.Message):
    experiment_campaign: str
    campaign_budget: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        experiment_campaign: str = ...,
        campaign_budget: str = ...
    ) -> None: ...

class EndExperimentRequest(proto.Message):
    experiment: str
    validate_only: bool
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        experiment: str = ...,
        validate_only: bool = ...
    ) -> None: ...

class ExperimentOperation(proto.Message):
    update_mask: FieldMask
    create: Experiment
    update: Experiment
    remove: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        update_mask: FieldMask = ...,
        create: Experiment = ...,
        update: Experiment = ...,
        remove: str = ...
    ) -> None: ...

class GraduateExperimentRequest(proto.Message):
    experiment: str
    campaign_budget_mappings: MutableSequence[CampaignBudgetMapping]
    validate_only: bool
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        experiment: str = ...,
        campaign_budget_mappings: MutableSequence[CampaignBudgetMapping] = ...,
        validate_only: bool = ...
    ) -> None: ...

class ListExperimentAsyncErrorsRequest(proto.Message):
    resource_name: str
    page_token: str
    page_size: int
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        page_token: str = ...,
        page_size: int = ...
    ) -> None: ...

class ListExperimentAsyncErrorsResponse(proto.Message):
    errors: MutableSequence[Status]
    next_page_token: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        errors: MutableSequence[Status] = ...,
        next_page_token: str = ...
    ) -> None: ...

class MutateExperimentResult(proto.Message):
    resource_name: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...
    ) -> None: ...

class MutateExperimentsRequest(proto.Message):
    customer_id: str
    operations: MutableSequence[ExperimentOperation]
    partial_failure: bool
    validate_only: bool
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        customer_id: str = ...,
        operations: MutableSequence[ExperimentOperation] = ...,
        partial_failure: bool = ...,
        validate_only: bool = ...
    ) -> None: ...

class MutateExperimentsResponse(proto.Message):
    partial_failure_error: Status
    results: MutableSequence[MutateExperimentResult]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        partial_failure_error: Status = ...,
        results: MutableSequence[MutateExperimentResult] = ...
    ) -> None: ...

class PromoteExperimentMetadata(proto.Message):
    experiment: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        experiment: str = ...
    ) -> None: ...

class PromoteExperimentRequest(proto.Message):
    resource_name: str
    validate_only: bool
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        validate_only: bool = ...
    ) -> None: ...

class ScheduleExperimentMetadata(proto.Message):
    experiment: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        experiment: str = ...
    ) -> None: ...

class ScheduleExperimentRequest(proto.Message):
    resource_name: str
    validate_only: bool
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        validate_only: bool = ...
    ) -> None: ...
