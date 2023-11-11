from collections.abc import Mapping, MutableSequence
from typing import Any, TypeVar

import google.protobuf.message
import proto
from google.rpc.status_pb2 import Status

from google.ads.googleads.v13.resources.types.ad_group_ad_label import AdGroupAdLabel

_M = TypeVar("_M")

class AdGroupAdLabelOperation(proto.Message):
    create: AdGroupAdLabel
    remove: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        create: AdGroupAdLabel = ...,
        remove: str = ...
    ) -> None: ...

class MutateAdGroupAdLabelResult(proto.Message):
    resource_name: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...
    ) -> None: ...

class MutateAdGroupAdLabelsRequest(proto.Message):
    customer_id: str
    operations: MutableSequence[AdGroupAdLabelOperation]
    partial_failure: bool
    validate_only: bool
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        customer_id: str = ...,
        operations: MutableSequence[AdGroupAdLabelOperation] = ...,
        partial_failure: bool = ...,
        validate_only: bool = ...
    ) -> None: ...

class MutateAdGroupAdLabelsResponse(proto.Message):
    partial_failure_error: Status
    results: MutableSequence[MutateAdGroupAdLabelResult]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        partial_failure_error: Status = ...,
        results: MutableSequence[MutateAdGroupAdLabelResult] = ...
    ) -> None: ...
