from typing import Any

import proto
from google.protobuf.field_mask_pb2 import FieldMask
from google.rpc.status_pb2 import Status

from google.ads.googleads.v11.enums.types.response_content_type import (
    ResponseContentTypeEnum,
)
from google.ads.googleads.v11.resources.types.ad_group_bid_modifier import (
    AdGroupBidModifier,
)

class AdGroupBidModifierOperation(proto.Message):
    update_mask: FieldMask
    create: AdGroupBidModifier
    update: AdGroupBidModifier
    remove: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        update_mask: FieldMask = ...,
        create: AdGroupBidModifier = ...,
        update: AdGroupBidModifier = ...,
        remove: str = ...
    ) -> None: ...

class MutateAdGroupBidModifierResult(proto.Message):
    resource_name: str
    ad_group_bid_modifier: AdGroupBidModifier
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        ad_group_bid_modifier: AdGroupBidModifier = ...
    ) -> None: ...

class MutateAdGroupBidModifiersRequest(proto.Message):
    customer_id: str
    operations: list[AdGroupBidModifierOperation]
    partial_failure: bool
    validate_only: bool
    response_content_type: ResponseContentTypeEnum.ResponseContentType
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        customer_id: str = ...,
        operations: list[AdGroupBidModifierOperation] = ...,
        partial_failure: bool = ...,
        validate_only: bool = ...,
        response_content_type: ResponseContentTypeEnum.ResponseContentType = ...
    ) -> None: ...

class MutateAdGroupBidModifiersResponse(proto.Message):
    partial_failure_error: Status
    results: list[MutateAdGroupBidModifierResult]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        partial_failure_error: Status = ...,
        results: list[MutateAdGroupBidModifierResult] = ...
    ) -> None: ...
