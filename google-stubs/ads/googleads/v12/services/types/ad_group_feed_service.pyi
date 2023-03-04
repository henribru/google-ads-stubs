from collections.abc import MutableSequence
from typing import Any

import proto
from google.protobuf.field_mask_pb2 import FieldMask
from google.rpc.status_pb2 import Status

from google.ads.googleads.v12.enums.types.response_content_type import (
    ResponseContentTypeEnum,
)
from google.ads.googleads.v12.resources.types.ad_group_feed import AdGroupFeed

class AdGroupFeedOperation(proto.Message):
    update_mask: FieldMask
    create: AdGroupFeed
    update: AdGroupFeed
    remove: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        update_mask: FieldMask = ...,
        create: AdGroupFeed = ...,
        update: AdGroupFeed = ...,
        remove: str = ...
    ) -> None: ...

class MutateAdGroupFeedResult(proto.Message):
    resource_name: str
    ad_group_feed: AdGroupFeed
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        ad_group_feed: AdGroupFeed = ...
    ) -> None: ...

class MutateAdGroupFeedsRequest(proto.Message):
    customer_id: str
    operations: MutableSequence[AdGroupFeedOperation]
    partial_failure: bool
    validate_only: bool
    response_content_type: ResponseContentTypeEnum.ResponseContentType
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        customer_id: str = ...,
        operations: MutableSequence[AdGroupFeedOperation] = ...,
        partial_failure: bool = ...,
        validate_only: bool = ...,
        response_content_type: ResponseContentTypeEnum.ResponseContentType = ...
    ) -> None: ...

class MutateAdGroupFeedsResponse(proto.Message):
    partial_failure_error: Status
    results: MutableSequence[MutateAdGroupFeedResult]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        partial_failure_error: Status = ...,
        results: MutableSequence[MutateAdGroupFeedResult] = ...
    ) -> None: ...
