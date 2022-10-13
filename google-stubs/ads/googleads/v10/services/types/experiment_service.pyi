from typing import Any

import proto
from google.protobuf.field_mask_pb2 import FieldMask
from google.rpc.status_pb2 import Status

from google.ads.googleads.v10.resources.types.experiment import Experiment

class CampaignBudgetMapping(proto.Message):
    experiment_campaign: str
    campaign_budget: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        experiment_campaign: str = ...,
        campaign_budget: str = ...
    ) -> None: ...

class EndExperimentRequest(proto.Message):
    experiment: str
    validate_only: bool
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        experiment: str = ...,
        validate_only: bool = ...
    ) -> None: ...

class ExperimentOperation(proto.Message):
    update_mask: FieldMask
    create: Experiment
    update: Experiment
    remove: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        update_mask: FieldMask = ...,
        create: Experiment = ...,
        update: Experiment = ...,
        remove: str = ...
    ) -> None: ...

class GraduateExperimentRequest(proto.Message):
    experiment: str
    campaign_budget_mappings: list[CampaignBudgetMapping]
    validate_only: bool
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        experiment: str = ...,
        campaign_budget_mappings: list[CampaignBudgetMapping] = ...,
        validate_only: bool = ...
    ) -> None: ...

class ListExperimentAsyncErrorsRequest(proto.Message):
    resource_name: str
    page_token: str
    page_size: int
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        page_token: str = ...,
        page_size: int = ...
    ) -> None: ...

class ListExperimentAsyncErrorsResponse(proto.Message):
    errors: list[Status]
    next_page_token: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        errors: list[Status] = ...,
        next_page_token: str = ...
    ) -> None: ...

class MutateExperimentResult(proto.Message):
    resource_name: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...
    ) -> None: ...

class MutateExperimentsRequest(proto.Message):
    customer_id: str
    operations: list[ExperimentOperation]
    partial_failure: bool
    validate_only: bool
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        customer_id: str = ...,
        operations: list[ExperimentOperation] = ...,
        partial_failure: bool = ...,
        validate_only: bool = ...
    ) -> None: ...

class MutateExperimentsResponse(proto.Message):
    partial_failure_error: Status
    results: list[MutateExperimentResult]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        partial_failure_error: Status = ...,
        results: list[MutateExperimentResult] = ...
    ) -> None: ...

class PromoteExperimentMetadata(proto.Message):
    experiment: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        experiment: str = ...
    ) -> None: ...

class PromoteExperimentRequest(proto.Message):
    resource_name: str
    validate_only: bool
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        validate_only: bool = ...
    ) -> None: ...

class ScheduleExperimentMetadata(proto.Message):
    experiment: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        experiment: str = ...
    ) -> None: ...

class ScheduleExperimentRequest(proto.Message):
    resource_name: str
    validate_only: bool
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        validate_only: bool = ...
    ) -> None: ...
