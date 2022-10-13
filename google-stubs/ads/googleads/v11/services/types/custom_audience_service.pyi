from typing import Any

import proto
from google.protobuf.field_mask_pb2 import FieldMask

from google.ads.googleads.v11.resources.types.custom_audience import CustomAudience

class CustomAudienceOperation(proto.Message):
    update_mask: FieldMask
    create: CustomAudience
    update: CustomAudience
    remove: str
    def __init__(
        self,
        mapping: Any | None = ...,
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
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...
    ) -> None: ...

class MutateCustomAudiencesRequest(proto.Message):
    customer_id: str
    operations: list[CustomAudienceOperation]
    validate_only: bool
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        customer_id: str = ...,
        operations: list[CustomAudienceOperation] = ...,
        validate_only: bool = ...
    ) -> None: ...

class MutateCustomAudiencesResponse(proto.Message):
    results: list[MutateCustomAudienceResult]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        results: list[MutateCustomAudienceResult] = ...
    ) -> None: ...
