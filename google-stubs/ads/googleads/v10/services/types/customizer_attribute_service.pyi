from typing import Any

import proto
from google.protobuf.field_mask_pb2 import FieldMask
from google.rpc.status_pb2 import Status

from google.ads.googleads.v10.enums.types.response_content_type import (
    ResponseContentTypeEnum,
)
from google.ads.googleads.v10.resources.types.customizer_attribute import (
    CustomizerAttribute,
)

class CustomizerAttributeOperation(proto.Message):
    update_mask: FieldMask
    create: CustomizerAttribute
    remove: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        update_mask: FieldMask = ...,
        create: CustomizerAttribute = ...,
        remove: str = ...
    ) -> None: ...

class MutateCustomizerAttributeResult(proto.Message):
    resource_name: str
    customizer_attribute: CustomizerAttribute
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        customizer_attribute: CustomizerAttribute = ...
    ) -> None: ...

class MutateCustomizerAttributesRequest(proto.Message):
    customer_id: str
    operations: list[CustomizerAttributeOperation]
    partial_failure: bool
    validate_only: bool
    response_content_type: ResponseContentTypeEnum.ResponseContentType
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        customer_id: str = ...,
        operations: list[CustomizerAttributeOperation] = ...,
        partial_failure: bool = ...,
        validate_only: bool = ...,
        response_content_type: ResponseContentTypeEnum.ResponseContentType = ...
    ) -> None: ...

class MutateCustomizerAttributesResponse(proto.Message):
    results: list[MutateCustomizerAttributeResult]
    partial_failure_error: Status
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        results: list[MutateCustomizerAttributeResult] = ...,
        partial_failure_error: Status = ...
    ) -> None: ...
