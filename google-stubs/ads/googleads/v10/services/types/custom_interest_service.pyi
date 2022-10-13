from typing import Any

import proto
from google.protobuf.field_mask_pb2 import FieldMask

from google.ads.googleads.v10.resources.types.custom_interest import CustomInterest

class CustomInterestOperation(proto.Message):
    update_mask: FieldMask
    create: CustomInterest
    update: CustomInterest
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        update_mask: FieldMask = ...,
        create: CustomInterest = ...,
        update: CustomInterest = ...
    ) -> None: ...

class MutateCustomInterestResult(proto.Message):
    resource_name: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...
    ) -> None: ...

class MutateCustomInterestsRequest(proto.Message):
    customer_id: str
    operations: list[CustomInterestOperation]
    validate_only: bool
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        customer_id: str = ...,
        operations: list[CustomInterestOperation] = ...,
        validate_only: bool = ...
    ) -> None: ...

class MutateCustomInterestsResponse(proto.Message):
    results: list[MutateCustomInterestResult]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        results: list[MutateCustomInterestResult] = ...
    ) -> None: ...
