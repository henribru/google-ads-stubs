from typing import Any

import proto
from google.protobuf.field_mask_pb2 import FieldMask
from google.rpc.status_pb2 import Status

from google.ads.googleads.v11.enums.types.response_content_type import (
    ResponseContentTypeEnum,
)
from google.ads.googleads.v11.resources.types.ad_parameter import AdParameter

class AdParameterOperation(proto.Message):
    update_mask: FieldMask
    create: AdParameter
    update: AdParameter
    remove: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        update_mask: FieldMask = ...,
        create: AdParameter = ...,
        update: AdParameter = ...,
        remove: str = ...
    ) -> None: ...

class MutateAdParameterResult(proto.Message):
    resource_name: str
    ad_parameter: AdParameter
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        ad_parameter: AdParameter = ...
    ) -> None: ...

class MutateAdParametersRequest(proto.Message):
    customer_id: str
    operations: list[AdParameterOperation]
    partial_failure: bool
    validate_only: bool
    response_content_type: ResponseContentTypeEnum.ResponseContentType
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        customer_id: str = ...,
        operations: list[AdParameterOperation] = ...,
        partial_failure: bool = ...,
        validate_only: bool = ...,
        response_content_type: ResponseContentTypeEnum.ResponseContentType = ...
    ) -> None: ...

class MutateAdParametersResponse(proto.Message):
    partial_failure_error: Status
    results: list[MutateAdParameterResult]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        partial_failure_error: Status = ...,
        results: list[MutateAdParameterResult] = ...
    ) -> None: ...
