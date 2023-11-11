from collections.abc import Mapping, MutableSequence
from typing import Any, TypeVar

import google.protobuf.message
import proto
from google.protobuf.field_mask_pb2 import FieldMask

from google.ads.googleads.v13.resources.types.custom_audience import CustomAudience

_M = TypeVar("_M")

class CustomAudienceOperation(proto.Message):
    update_mask: FieldMask
    create: CustomAudience
    update: CustomAudience
    remove: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        update_mask: FieldMask = ...,
        create: CustomAudience = ...,
        update: CustomAudience = ...,
        remove: str = ...
    ) -> None: ...

class MutateCustomAudienceResult(proto.Message):
    resource_name: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...
    ) -> None: ...

class MutateCustomAudiencesRequest(proto.Message):
    customer_id: str
    operations: MutableSequence[CustomAudienceOperation]
    validate_only: bool
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        customer_id: str = ...,
        operations: MutableSequence[CustomAudienceOperation] = ...,
        validate_only: bool = ...
    ) -> None: ...

class MutateCustomAudiencesResponse(proto.Message):
    results: MutableSequence[MutateCustomAudienceResult]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        results: MutableSequence[MutateCustomAudienceResult] = ...
    ) -> None: ...
