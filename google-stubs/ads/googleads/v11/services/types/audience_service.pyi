from typing import Any

import proto
from google.protobuf.field_mask_pb2 import FieldMask
from google.rpc.status_pb2 import Status

from google.ads.googleads.v11.enums.types.response_content_type import (
    ResponseContentTypeEnum,
)
from google.ads.googleads.v11.resources.types.audience import Audience

class AudienceOperation(proto.Message):
    update_mask: FieldMask
    create: Audience
    update: Audience
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        update_mask: FieldMask = ...,
        create: Audience = ...,
        update: Audience = ...
    ) -> None: ...

class MutateAudienceResult(proto.Message):
    resource_name: str
    audience: Audience
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        audience: Audience = ...
    ) -> None: ...

class MutateAudiencesRequest(proto.Message):
    customer_id: str
    operations: list[AudienceOperation]
    partial_failure: bool
    validate_only: bool
    response_content_type: ResponseContentTypeEnum.ResponseContentType
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        customer_id: str = ...,
        operations: list[AudienceOperation] = ...,
        partial_failure: bool = ...,
        validate_only: bool = ...,
        response_content_type: ResponseContentTypeEnum.ResponseContentType = ...
    ) -> None: ...

class MutateAudiencesResponse(proto.Message):
    results: list[MutateAudienceResult]
    partial_failure_error: Status
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        results: list[MutateAudienceResult] = ...,
        partial_failure_error: Status = ...
    ) -> None: ...
