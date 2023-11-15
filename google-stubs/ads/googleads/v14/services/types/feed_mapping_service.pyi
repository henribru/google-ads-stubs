from collections.abc import Mapping, MutableSequence
from typing import Any, TypeVar

import google.protobuf.message
import proto
from google.rpc.status_pb2 import Status

from google.ads.googleads.v14.enums.types.response_content_type import (
    ResponseContentTypeEnum,
)
from google.ads.googleads.v14.resources.types.feed_mapping import FeedMapping

_M = TypeVar("_M")

class FeedMappingOperation(proto.Message):
    create: FeedMapping
    remove: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        create: FeedMapping = ...,
        remove: str = ...
    ) -> None: ...

class MutateFeedMappingResult(proto.Message):
    resource_name: str
    feed_mapping: FeedMapping
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        feed_mapping: FeedMapping = ...
    ) -> None: ...

class MutateFeedMappingsRequest(proto.Message):
    customer_id: str
    operations: MutableSequence[FeedMappingOperation]
    partial_failure: bool
    validate_only: bool
    response_content_type: ResponseContentTypeEnum.ResponseContentType
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        customer_id: str = ...,
        operations: MutableSequence[FeedMappingOperation] = ...,
        partial_failure: bool = ...,
        validate_only: bool = ...,
        response_content_type: ResponseContentTypeEnum.ResponseContentType = ...
    ) -> None: ...

class MutateFeedMappingsResponse(proto.Message):
    partial_failure_error: Status
    results: MutableSequence[MutateFeedMappingResult]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        partial_failure_error: Status = ...,
        results: MutableSequence[MutateFeedMappingResult] = ...
    ) -> None: ...
