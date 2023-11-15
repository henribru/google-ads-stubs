from collections.abc import Mapping, MutableSequence
from typing import Any, TypeVar

import google.protobuf.message
import proto
from google.protobuf.field_mask_pb2 import FieldMask
from google.rpc.status_pb2 import Status

from google.ads.googleads.v15.enums.types.response_content_type import (
    ResponseContentTypeEnum,
)
from google.ads.googleads.v15.resources.types.conversion_action import ConversionAction

_M = TypeVar("_M")

class ConversionActionOperation(proto.Message):
    update_mask: FieldMask
    create: ConversionAction
    update: ConversionAction
    remove: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        update_mask: FieldMask = ...,
        create: ConversionAction = ...,
        update: ConversionAction = ...,
        remove: str = ...
    ) -> None: ...

class MutateConversionActionResult(proto.Message):
    resource_name: str
    conversion_action: ConversionAction
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        conversion_action: ConversionAction = ...
    ) -> None: ...

class MutateConversionActionsRequest(proto.Message):
    customer_id: str
    operations: MutableSequence[ConversionActionOperation]
    partial_failure: bool
    validate_only: bool
    response_content_type: ResponseContentTypeEnum.ResponseContentType
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        customer_id: str = ...,
        operations: MutableSequence[ConversionActionOperation] = ...,
        partial_failure: bool = ...,
        validate_only: bool = ...,
        response_content_type: ResponseContentTypeEnum.ResponseContentType = ...
    ) -> None: ...

class MutateConversionActionsResponse(proto.Message):
    partial_failure_error: Status
    results: MutableSequence[MutateConversionActionResult]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        partial_failure_error: Status = ...,
        results: MutableSequence[MutateConversionActionResult] = ...
    ) -> None: ...
