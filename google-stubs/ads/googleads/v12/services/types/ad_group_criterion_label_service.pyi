from collections.abc import MutableSequence
from typing import Any

import proto
from google.rpc.status_pb2 import Status

from google.ads.googleads.v12.resources.types.ad_group_criterion_label import (
    AdGroupCriterionLabel,
)

class AdGroupCriterionLabelOperation(proto.Message):
    create: AdGroupCriterionLabel
    remove: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        create: AdGroupCriterionLabel = ...,
        remove: str = ...
    ) -> None: ...

class MutateAdGroupCriterionLabelResult(proto.Message):
    resource_name: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...
    ) -> None: ...

class MutateAdGroupCriterionLabelsRequest(proto.Message):
    customer_id: str
    operations: MutableSequence[AdGroupCriterionLabelOperation]
    partial_failure: bool
    validate_only: bool
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        customer_id: str = ...,
        operations: MutableSequence[AdGroupCriterionLabelOperation] = ...,
        partial_failure: bool = ...,
        validate_only: bool = ...
    ) -> None: ...

class MutateAdGroupCriterionLabelsResponse(proto.Message):
    partial_failure_error: Status
    results: MutableSequence[MutateAdGroupCriterionLabelResult]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        partial_failure_error: Status = ...,
        results: MutableSequence[MutateAdGroupCriterionLabelResult] = ...
    ) -> None: ...
