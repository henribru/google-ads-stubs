from collections.abc import Mapping, MutableSequence
from typing import Any, TypeVar

import google.protobuf.message
import proto
from google.rpc.status_pb2 import Status

from google.ads.googleads.v14.resources.types.ad_group_criterion_label import (
    AdGroupCriterionLabel,
)

_M = TypeVar("_M")

class AdGroupCriterionLabelOperation(proto.Message):
    create: AdGroupCriterionLabel
    remove: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        create: AdGroupCriterionLabel = ...,
        remove: str = ...
    ) -> None: ...

class MutateAdGroupCriterionLabelResult(proto.Message):
    resource_name: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...
    ) -> None: ...

class MutateAdGroupCriterionLabelsRequest(proto.Message):
    customer_id: str
    operations: MutableSequence[AdGroupCriterionLabelOperation]
    partial_failure: bool
    validate_only: bool
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        customer_id: str = ...,
        operations: MutableSequence[AdGroupCriterionLabelOperation] = ...,
        partial_failure: bool = ...,
        validate_only: bool = ...
    ) -> None: ...

class MutateAdGroupCriterionLabelsResponse(proto.Message):
    partial_failure_error: Status
    results: MutableSequence[MutateAdGroupCriterionLabelResult]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        partial_failure_error: Status = ...,
        results: MutableSequence[MutateAdGroupCriterionLabelResult] = ...
    ) -> None: ...
