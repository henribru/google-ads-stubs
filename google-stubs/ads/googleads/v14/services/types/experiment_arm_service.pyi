from collections.abc import Mapping, MutableSequence
from typing import Any, TypeVar

import google.protobuf.message
import proto
from google.protobuf.field_mask_pb2 import FieldMask
from google.rpc.status_pb2 import Status

from google.ads.googleads.v14.enums.types.response_content_type import (
    ResponseContentTypeEnum,
)
from google.ads.googleads.v14.resources.types.experiment_arm import ExperimentArm

_M = TypeVar("_M")

class ExperimentArmOperation(proto.Message):
    update_mask: FieldMask
    create: ExperimentArm
    update: ExperimentArm
    remove: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        update_mask: FieldMask = ...,
        create: ExperimentArm = ...,
        update: ExperimentArm = ...,
        remove: str = ...
    ) -> None: ...

class MutateExperimentArmResult(proto.Message):
    resource_name: str
    experiment_arm: ExperimentArm
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
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
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
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
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        partial_failure_error: Status = ...,
        results: MutableSequence[MutateExperimentArmResult] = ...
    ) -> None: ...
