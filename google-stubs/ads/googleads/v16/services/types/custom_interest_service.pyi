from collections.abc import Mapping, MutableSequence
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from google.protobuf.field_mask_pb2 import FieldMask
from typing_extensions import Literal

from google.ads.googleads.v16.resources.types.custom_interest import CustomInterest

_M = TypeVar("_M")

class CustomInterestOperation(proto.Message):
    update_mask: FieldMask
    create: CustomInterest
    update: CustomInterest
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        update_mask: FieldMask = ...,
        create: CustomInterest = ...,
        update: CustomInterest = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["update_mask", "create", "update"]
    ) -> bool: ...

class MutateCustomInterestResult(proto.Message):
    resource_name: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["resource_name"]
    ) -> bool: ...

class MutateCustomInterestsRequest(proto.Message):
    customer_id: str
    operations: MutableSequence[CustomInterestOperation]
    validate_only: bool
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        customer_id: str = ...,
        operations: MutableSequence[CustomInterestOperation] = ...,
        validate_only: bool = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["customer_id", "operations", "validate_only"]
    ) -> bool: ...

class MutateCustomInterestsResponse(proto.Message):
    results: MutableSequence[MutateCustomInterestResult]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        results: MutableSequence[MutateCustomInterestResult] = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["results"]
    ) -> bool: ...
