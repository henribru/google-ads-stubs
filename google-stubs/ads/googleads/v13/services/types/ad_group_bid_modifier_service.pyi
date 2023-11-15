from collections.abc import Mapping, MutableSequence
from typing import Any, TypeVar

import google.protobuf.message
import proto
from google.protobuf.field_mask_pb2 import FieldMask
from google.rpc.status_pb2 import Status

from google.ads.googleads.v13.enums.types.response_content_type import (
    ResponseContentTypeEnum,
)
from google.ads.googleads.v13.resources.types.ad_group_bid_modifier import (
    AdGroupBidModifier,
)

_M = TypeVar("_M")

class AdGroupBidModifierOperation(proto.Message):
    update_mask: FieldMask
    create: AdGroupBidModifier
    update: AdGroupBidModifier
    remove: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        update_mask: FieldMask = ...,
        create: AdGroupBidModifier = ...,
        update: AdGroupBidModifier = ...,
        remove: str = ...
    ) -> None: ...

class MutateAdGroupBidModifierResult(proto.Message):
    resource_name: str
    ad_group_bid_modifier: AdGroupBidModifier
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        ad_group_bid_modifier: AdGroupBidModifier = ...
    ) -> None: ...

class MutateAdGroupBidModifiersRequest(proto.Message):
    customer_id: str
    operations: MutableSequence[AdGroupBidModifierOperation]
    partial_failure: bool
    validate_only: bool
    response_content_type: ResponseContentTypeEnum.ResponseContentType
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        customer_id: str = ...,
        operations: MutableSequence[AdGroupBidModifierOperation] = ...,
        partial_failure: bool = ...,
        validate_only: bool = ...,
        response_content_type: ResponseContentTypeEnum.ResponseContentType = ...
    ) -> None: ...

class MutateAdGroupBidModifiersResponse(proto.Message):
    partial_failure_error: Status
    results: MutableSequence[MutateAdGroupBidModifierResult]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        partial_failure_error: Status = ...,
        results: MutableSequence[MutateAdGroupBidModifierResult] = ...
    ) -> None: ...
