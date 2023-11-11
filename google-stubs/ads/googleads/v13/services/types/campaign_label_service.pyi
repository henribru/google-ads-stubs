from collections.abc import Mapping, MutableSequence
from typing import Any, TypeVar

import google.protobuf.message
import proto
from google.rpc.status_pb2 import Status

from google.ads.googleads.v13.resources.types.campaign_label import CampaignLabel

_M = TypeVar("_M")

class CampaignLabelOperation(proto.Message):
    create: CampaignLabel
    remove: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        create: CampaignLabel = ...,
        remove: str = ...
    ) -> None: ...

class MutateCampaignLabelResult(proto.Message):
    resource_name: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...
    ) -> None: ...

class MutateCampaignLabelsRequest(proto.Message):
    customer_id: str
    operations: MutableSequence[CampaignLabelOperation]
    partial_failure: bool
    validate_only: bool
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        customer_id: str = ...,
        operations: MutableSequence[CampaignLabelOperation] = ...,
        partial_failure: bool = ...,
        validate_only: bool = ...
    ) -> None: ...

class MutateCampaignLabelsResponse(proto.Message):
    partial_failure_error: Status
    results: MutableSequence[MutateCampaignLabelResult]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        partial_failure_error: Status = ...,
        results: MutableSequence[MutateCampaignLabelResult] = ...
    ) -> None: ...
