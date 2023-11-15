from collections.abc import Mapping, MutableSequence
from typing import Any, TypeVar

import google.protobuf.message
import proto
from google.protobuf.field_mask_pb2 import FieldMask
from google.rpc.status_pb2 import Status

from google.ads.googleads.v14.enums.types.response_content_type import (
    ResponseContentTypeEnum,
)
from google.ads.googleads.v14.resources.types.customizer_attribute import (
    CustomizerAttribute,
)

_M = TypeVar("_M")

class CustomizerAttributeOperation(proto.Message):
    update_mask: FieldMask
    create: CustomizerAttribute
    remove: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        update_mask: FieldMask = ...,
        create: CustomizerAttribute = ...,
        remove: str = ...
    ) -> None: ...

class MutateCustomizerAttributeResult(proto.Message):
    resource_name: str
    customizer_attribute: CustomizerAttribute
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        customizer_attribute: CustomizerAttribute = ...
    ) -> None: ...

class MutateCustomizerAttributesRequest(proto.Message):
    customer_id: str
    operations: MutableSequence[CustomizerAttributeOperation]
    partial_failure: bool
    validate_only: bool
    response_content_type: ResponseContentTypeEnum.ResponseContentType
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        customer_id: str = ...,
        operations: MutableSequence[CustomizerAttributeOperation] = ...,
        partial_failure: bool = ...,
        validate_only: bool = ...,
        response_content_type: ResponseContentTypeEnum.ResponseContentType = ...
    ) -> None: ...

class MutateCustomizerAttributesResponse(proto.Message):
    results: MutableSequence[MutateCustomizerAttributeResult]
    partial_failure_error: Status
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        results: MutableSequence[MutateCustomizerAttributeResult] = ...,
        partial_failure_error: Status = ...
    ) -> None: ...
