from typing import Any

import proto
from google.rpc.status_pb2 import Status

from google.ads.googleads.v10.enums.types.response_content_type import (
    ResponseContentTypeEnum,
)
from google.ads.googleads.v10.resources.types.feed_mapping import FeedMapping

class FeedMappingOperation(proto.Message):
    create: FeedMapping
    remove: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        create: FeedMapping = ...,
        remove: str = ...
    ) -> None: ...

class MutateFeedMappingResult(proto.Message):
    resource_name: str
    feed_mapping: FeedMapping
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        feed_mapping: FeedMapping = ...
    ) -> None: ...

class MutateFeedMappingsRequest(proto.Message):
    customer_id: str
    operations: list[FeedMappingOperation]
    partial_failure: bool
    validate_only: bool
    response_content_type: ResponseContentTypeEnum.ResponseContentType
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        customer_id: str = ...,
        operations: list[FeedMappingOperation] = ...,
        partial_failure: bool = ...,
        validate_only: bool = ...,
        response_content_type: ResponseContentTypeEnum.ResponseContentType = ...
    ) -> None: ...

class MutateFeedMappingsResponse(proto.Message):
    partial_failure_error: Status
    results: list[MutateFeedMappingResult]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        partial_failure_error: Status = ...,
        results: list[MutateFeedMappingResult] = ...
    ) -> None: ...
