from collections.abc import Mapping, MutableSequence
from typing import Any, TypeVar

import google.protobuf.message
import proto
from google.protobuf.field_mask_pb2 import FieldMask
from google.rpc.status_pb2 import Status

from google.ads.googleads.v13.enums.types.response_content_type import (
    ResponseContentTypeEnum,
)
from google.ads.googleads.v13.resources.types.campaign_group import CampaignGroup

_M = TypeVar("_M")

class CampaignGroupOperation(proto.Message):
    update_mask: FieldMask
    create: CampaignGroup
    update: CampaignGroup
    remove: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        update_mask: FieldMask = ...,
        create: CampaignGroup = ...,
        update: CampaignGroup = ...,
        remove: str = ...
    ) -> None: ...

class MutateCampaignGroupResult(proto.Message):
    resource_name: str
    campaign_group: CampaignGroup
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        campaign_group: CampaignGroup = ...
    ) -> None: ...

class MutateCampaignGroupsRequest(proto.Message):
    customer_id: str
    operations: MutableSequence[CampaignGroupOperation]
    partial_failure: bool
    validate_only: bool
    response_content_type: ResponseContentTypeEnum.ResponseContentType
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        customer_id: str = ...,
        operations: MutableSequence[CampaignGroupOperation] = ...,
        partial_failure: bool = ...,
        validate_only: bool = ...,
        response_content_type: ResponseContentTypeEnum.ResponseContentType = ...
    ) -> None: ...

class MutateCampaignGroupsResponse(proto.Message):
    results: MutableSequence[MutateCampaignGroupResult]
    partial_failure_error: Status
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        results: MutableSequence[MutateCampaignGroupResult] = ...,
        partial_failure_error: Status = ...
    ) -> None: ...
