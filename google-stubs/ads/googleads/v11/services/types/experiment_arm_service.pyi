from collections.abc import MutableSequence
from typing import Any

import proto
from google.protobuf.field_mask_pb2 import FieldMask
from google.rpc.status_pb2 import Status

from google.ads.googleads.v11.enums.types.response_content_type import (
    ResponseContentTypeEnum,
)
from google.ads.googleads.v11.resources.types.experiment_arm import ExperimentArm

class ExperimentArmOperation(proto.Message):
    update_mask: FieldMask
    create: ExperimentArm
    update: ExperimentArm
    remove: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        update_mask: FieldMask = ...,
        create: ExperimentArm = ...,
        update: ExperimentArm = ...,
        remove: str = ...
    ) -> None: ...

class MutateExperimentArmResult(proto.Message):
    resource_name: str
    experiment_arm: ExperimentArm
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        experiment_arm: ExperimentArm = ...
    ) -> None: ...

class MutateExperimentArmsRequest(proto.Message):
    customer_id: str
    operations: MutableSequence[ExperimentArmOperation]
    partial_failure: bool
    validate_only: bool
    response_content_type: ResponseContentTypeEnum.ResponseContentType
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        customer_id: str = ...,
        operations: MutableSequence[ExperimentArmOperation] = ...,
        partial_failure: bool = ...,
        validate_only: bool = ...,
        response_content_type: ResponseContentTypeEnum.ResponseContentType = ...
    ) -> None: ...

class MutateExperimentArmsResponse(proto.Message):
    partial_failure_error: Status
    results: MutableSequence[MutateExperimentArmResult]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        partial_failure_error: Status = ...,
        results: MutableSequence[MutateExperimentArmResult] = ...
    ) -> None: ...
