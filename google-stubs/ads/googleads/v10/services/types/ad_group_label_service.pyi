from typing import Any

import proto
from google.rpc.status_pb2 import Status

from google.ads.googleads.v10.resources.types.ad_group_label import AdGroupLabel

class AdGroupLabelOperation(proto.Message):
    create: AdGroupLabel
    remove: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        create: AdGroupLabel = ...,
        remove: str = ...
    ) -> None: ...

class MutateAdGroupLabelResult(proto.Message):
    resource_name: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...
    ) -> None: ...

class MutateAdGroupLabelsRequest(proto.Message):
    customer_id: str
    operations: list[AdGroupLabelOperation]
    partial_failure: bool
    validate_only: bool
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        customer_id: str = ...,
        operations: list[AdGroupLabelOperation] = ...,
        partial_failure: bool = ...,
        validate_only: bool = ...
    ) -> None: ...

class MutateAdGroupLabelsResponse(proto.Message):
    partial_failure_error: Status
    results: list[MutateAdGroupLabelResult]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        partial_failure_error: Status = ...,
        results: list[MutateAdGroupLabelResult] = ...
    ) -> None: ...
