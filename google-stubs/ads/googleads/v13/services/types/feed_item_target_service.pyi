from collections.abc import MutableSequence
from typing import Any

import proto
from google.rpc.status_pb2 import Status

from google.ads.googleads.v13.enums.types.response_content_type import (
    ResponseContentTypeEnum,
)
from google.ads.googleads.v13.resources.types.feed_item_target import FeedItemTarget

class FeedItemTargetOperation(proto.Message):
    create: FeedItemTarget
    remove: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        create: FeedItemTarget = ...,
        remove: str = ...
    ) -> None: ...

class MutateFeedItemTargetResult(proto.Message):
    resource_name: str
    feed_item_target: FeedItemTarget
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        feed_item_target: FeedItemTarget = ...
    ) -> None: ...

class MutateFeedItemTargetsRequest(proto.Message):
    customer_id: str
    operations: MutableSequence[FeedItemTargetOperation]
    partial_failure: bool
    response_content_type: ResponseContentTypeEnum.ResponseContentType
    validate_only: bool
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        customer_id: str = ...,
        operations: MutableSequence[FeedItemTargetOperation] = ...,
        partial_failure: bool = ...,
        response_content_type: ResponseContentTypeEnum.ResponseContentType = ...,
        validate_only: bool = ...
    ) -> None: ...

class MutateFeedItemTargetsResponse(proto.Message):
    partial_failure_error: Status
    results: MutableSequence[MutateFeedItemTargetResult]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        partial_failure_error: Status = ...,
        results: MutableSequence[MutateFeedItemTargetResult] = ...
    ) -> None: ...
