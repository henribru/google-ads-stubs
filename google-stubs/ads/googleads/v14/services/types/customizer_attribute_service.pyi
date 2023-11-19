from collections.abc import Mapping, MutableSequence
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from google.protobuf.field_mask_pb2 import FieldMask
from google.rpc.status_pb2 import Status
from typing_extensions import Literal

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
    def __contains__(self, key: Literal["update_mask", "create", "remove"]) -> bool: ...  # type: ignore[override]

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
    def __contains__(self, key: Literal["resource_name", "customizer_attribute"]) -> bool: ...  # type: ignore[override]

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
    def __contains__(self, key: Literal["customer_id", "operations", "partial_failure", "validate_only", "response_content_type"]) -> bool: ...  # type: ignore[override]

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
    def __contains__(self, key: Literal["results", "partial_failure_error"]) -> bool: ...  # type: ignore[override]
