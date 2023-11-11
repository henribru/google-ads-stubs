from collections.abc import Mapping, MutableSequence
from typing import Any, TypeVar

import google.protobuf.message
import proto
from google.protobuf.field_mask_pb2 import FieldMask
from google.rpc.status_pb2 import Status

from google.ads.googleads.v15.resources.types.remarketing_action import (
    RemarketingAction,
)

_M = TypeVar("_M")

class MutateRemarketingActionResult(proto.Message):
    resource_name: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...
    ) -> None: ...

class MutateRemarketingActionsRequest(proto.Message):
    customer_id: str
    operations: MutableSequence[RemarketingActionOperation]
    partial_failure: bool
    validate_only: bool
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        customer_id: str = ...,
        operations: MutableSequence[RemarketingActionOperation] = ...,
        partial_failure: bool = ...,
        validate_only: bool = ...
    ) -> None: ...

class MutateRemarketingActionsResponse(proto.Message):
    partial_failure_error: Status
    results: MutableSequence[MutateRemarketingActionResult]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        partial_failure_error: Status = ...,
        results: MutableSequence[MutateRemarketingActionResult] = ...
    ) -> None: ...

class RemarketingActionOperation(proto.Message):
    update_mask: FieldMask
    create: RemarketingAction
    update: RemarketingAction
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        update_mask: FieldMask = ...,
        create: RemarketingAction = ...,
        update: RemarketingAction = ...
    ) -> None: ...
