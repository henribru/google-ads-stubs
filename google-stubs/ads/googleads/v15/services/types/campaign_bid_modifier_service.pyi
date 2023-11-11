from collections.abc import Mapping, MutableSequence
from typing import Any, TypeVar

import google.protobuf.message
import proto
from google.protobuf.field_mask_pb2 import FieldMask
from google.rpc.status_pb2 import Status

from google.ads.googleads.v15.enums.types.response_content_type import (
    ResponseContentTypeEnum,
)
from google.ads.googleads.v15.resources.types.campaign_bid_modifier import (
    CampaignBidModifier,
)

_M = TypeVar("_M")

class CampaignBidModifierOperation(proto.Message):
    update_mask: FieldMask
    create: CampaignBidModifier
    update: CampaignBidModifier
    remove: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        update_mask: FieldMask = ...,
        create: CampaignBidModifier = ...,
        update: CampaignBidModifier = ...,
        remove: str = ...
    ) -> None: ...

class MutateCampaignBidModifierResult(proto.Message):
    resource_name: str
    campaign_bid_modifier: CampaignBidModifier
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        campaign_bid_modifier: CampaignBidModifier = ...
    ) -> None: ...

class MutateCampaignBidModifiersRequest(proto.Message):
    customer_id: str
    operations: MutableSequence[CampaignBidModifierOperation]
    partial_failure: bool
    validate_only: bool
    response_content_type: ResponseContentTypeEnum.ResponseContentType
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        customer_id: str = ...,
        operations: MutableSequence[CampaignBidModifierOperation] = ...,
        partial_failure: bool = ...,
        validate_only: bool = ...,
        response_content_type: ResponseContentTypeEnum.ResponseContentType = ...
    ) -> None: ...

class MutateCampaignBidModifiersResponse(proto.Message):
    partial_failure_error: Status
    results: MutableSequence[MutateCampaignBidModifierResult]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        partial_failure_error: Status = ...,
        results: MutableSequence[MutateCampaignBidModifierResult] = ...
    ) -> None: ...
