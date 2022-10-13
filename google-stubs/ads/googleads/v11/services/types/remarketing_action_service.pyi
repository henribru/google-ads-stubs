from typing import Any

import proto
from google.protobuf.field_mask_pb2 import FieldMask
from google.rpc.status_pb2 import Status

from google.ads.googleads.v11.resources.types.remarketing_action import (
    RemarketingAction,
)

class MutateRemarketingActionResult(proto.Message):
    resource_name: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...
    ) -> None: ...

class MutateRemarketingActionsRequest(proto.Message):
    customer_id: str
    operations: list[RemarketingActionOperation]
    partial_failure: bool
    validate_only: bool
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        customer_id: str = ...,
        operations: list[RemarketingActionOperation] = ...,
        partial_failure: bool = ...,
        validate_only: bool = ...
    ) -> None: ...

class MutateRemarketingActionsResponse(proto.Message):
    partial_failure_error: Status
    results: list[MutateRemarketingActionResult]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        partial_failure_error: Status = ...,
        results: list[MutateRemarketingActionResult] = ...
    ) -> None: ...

class RemarketingActionOperation(proto.Message):
    update_mask: FieldMask
    create: RemarketingAction
    update: RemarketingAction
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        update_mask: FieldMask = ...,
        create: RemarketingAction = ...,
        update: RemarketingAction = ...
    ) -> None: ...
