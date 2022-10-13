from typing import Any

import proto
from google.rpc.status_pb2 import Status

from google.ads.googleads.v10.enums.types.response_content_type import (
    ResponseContentTypeEnum,
)
from google.ads.googleads.v10.resources.types.shared_criterion import SharedCriterion

class MutateSharedCriteriaRequest(proto.Message):
    customer_id: str
    operations: list[SharedCriterionOperation]
    partial_failure: bool
    validate_only: bool
    response_content_type: ResponseContentTypeEnum.ResponseContentType
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        customer_id: str = ...,
        operations: list[SharedCriterionOperation] = ...,
        partial_failure: bool = ...,
        validate_only: bool = ...,
        response_content_type: ResponseContentTypeEnum.ResponseContentType = ...
    ) -> None: ...

class MutateSharedCriteriaResponse(proto.Message):
    partial_failure_error: Status
    results: list[MutateSharedCriterionResult]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        partial_failure_error: Status = ...,
        results: list[MutateSharedCriterionResult] = ...
    ) -> None: ...

class MutateSharedCriterionResult(proto.Message):
    resource_name: str
    shared_criterion: SharedCriterion
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        shared_criterion: SharedCriterion = ...
    ) -> None: ...

class SharedCriterionOperation(proto.Message):
    create: SharedCriterion
    remove: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        create: SharedCriterion = ...,
        remove: str = ...
    ) -> None: ...
