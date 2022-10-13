from typing import Any

import proto
from google.rpc.status_pb2 import Status

from google.ads.googleads.v11.resources.types.ad_group_ad_label import AdGroupAdLabel

class AdGroupAdLabelOperation(proto.Message):
    create: AdGroupAdLabel
    remove: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        create: AdGroupAdLabel = ...,
        remove: str = ...
    ) -> None: ...

class MutateAdGroupAdLabelResult(proto.Message):
    resource_name: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...
    ) -> None: ...

class MutateAdGroupAdLabelsRequest(proto.Message):
    customer_id: str
    operations: list[AdGroupAdLabelOperation]
    partial_failure: bool
    validate_only: bool
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        customer_id: str = ...,
        operations: list[AdGroupAdLabelOperation] = ...,
        partial_failure: bool = ...,
        validate_only: bool = ...
    ) -> None: ...

class MutateAdGroupAdLabelsResponse(proto.Message):
    partial_failure_error: Status
    results: list[MutateAdGroupAdLabelResult]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        partial_failure_error: Status = ...,
        results: list[MutateAdGroupAdLabelResult] = ...
    ) -> None: ...
