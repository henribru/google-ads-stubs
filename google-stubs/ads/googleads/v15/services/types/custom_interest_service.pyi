from collections.abc import Mapping, MutableSequence
from typing import Any, TypeVar

import google.protobuf.message
import proto
from google.protobuf.field_mask_pb2 import FieldMask

from google.ads.googleads.v15.resources.types.custom_interest import CustomInterest

_M = TypeVar("_M")

class CustomInterestOperation(proto.Message):
    update_mask: FieldMask
    create: CustomInterest
    update: CustomInterest
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        update_mask: FieldMask = ...,
        create: CustomInterest = ...,
        update: CustomInterest = ...
    ) -> None: ...

class MutateCustomInterestResult(proto.Message):
    resource_name: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...
    ) -> None: ...

class MutateCustomInterestsRequest(proto.Message):
    customer_id: str
    operations: MutableSequence[CustomInterestOperation]
    validate_only: bool
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        customer_id: str = ...,
        operations: MutableSequence[CustomInterestOperation] = ...,
        validate_only: bool = ...
    ) -> None: ...

class MutateCustomInterestsResponse(proto.Message):
    results: MutableSequence[MutateCustomInterestResult]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        results: MutableSequence[MutateCustomInterestResult] = ...
    ) -> None: ...
