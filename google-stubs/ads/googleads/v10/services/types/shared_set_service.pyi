from typing import Any

import proto
from google.protobuf.field_mask_pb2 import FieldMask
from google.rpc.status_pb2 import Status

from google.ads.googleads.v10.enums.types.response_content_type import (
    ResponseContentTypeEnum,
)
from google.ads.googleads.v10.resources.types.shared_set import SharedSet

class MutateSharedSetResult(proto.Message):
    resource_name: str
    shared_set: SharedSet
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        shared_set: SharedSet = ...
    ) -> None: ...

class MutateSharedSetsRequest(proto.Message):
    customer_id: str
    operations: list[SharedSetOperation]
    partial_failure: bool
    validate_only: bool
    response_content_type: ResponseContentTypeEnum.ResponseContentType
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        customer_id: str = ...,
        operations: list[SharedSetOperation] = ...,
        partial_failure: bool = ...,
        validate_only: bool = ...,
        response_content_type: ResponseContentTypeEnum.ResponseContentType = ...
    ) -> None: ...

class MutateSharedSetsResponse(proto.Message):
    partial_failure_error: Status
    results: list[MutateSharedSetResult]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        partial_failure_error: Status = ...,
        results: list[MutateSharedSetResult] = ...
    ) -> None: ...

class SharedSetOperation(proto.Message):
    update_mask: FieldMask
    create: SharedSet
    update: SharedSet
    remove: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        update_mask: FieldMask = ...,
        create: SharedSet = ...,
        update: SharedSet = ...,
        remove: str = ...
    ) -> None: ...
