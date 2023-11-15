from collections.abc import Mapping, MutableSequence
from typing import Any, TypeVar

import google.protobuf.message
import proto
from google.rpc.status_pb2 import Status

from google.ads.googleads.v14.enums.types.response_content_type import (
    ResponseContentTypeEnum,
)
from google.ads.googleads.v14.resources.types.campaign_shared_set import (
    CampaignSharedSet,
)

_M = TypeVar("_M")

class CampaignSharedSetOperation(proto.Message):
    create: CampaignSharedSet
    remove: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        create: CampaignSharedSet = ...,
        remove: str = ...
    ) -> None: ...

class MutateCampaignSharedSetResult(proto.Message):
    resource_name: str
    campaign_shared_set: CampaignSharedSet
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        campaign_shared_set: CampaignSharedSet = ...
    ) -> None: ...

class MutateCampaignSharedSetsRequest(proto.Message):
    customer_id: str
    operations: MutableSequence[CampaignSharedSetOperation]
    partial_failure: bool
    validate_only: bool
    response_content_type: ResponseContentTypeEnum.ResponseContentType
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        customer_id: str = ...,
        operations: MutableSequence[CampaignSharedSetOperation] = ...,
        partial_failure: bool = ...,
        validate_only: bool = ...,
        response_content_type: ResponseContentTypeEnum.ResponseContentType = ...
    ) -> None: ...

class MutateCampaignSharedSetsResponse(proto.Message):
    partial_failure_error: Status
    results: MutableSequence[MutateCampaignSharedSetResult]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        partial_failure_error: Status = ...,
        results: MutableSequence[MutateCampaignSharedSetResult] = ...
    ) -> None: ...
