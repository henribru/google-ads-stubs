from collections.abc import Mapping, MutableSequence
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from google.rpc.status_pb2 import Status
from typing_extensions import Literal

from google.ads.googleads.v16.enums.types.response_content_type import (
    ResponseContentTypeEnum,
)
from google.ads.googleads.v16.resources.types.feed_item_target import FeedItemTarget

_M = TypeVar("_M")

class FeedItemTargetOperation(proto.Message):
    create: FeedItemTarget
    remove: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        create: FeedItemTarget = ...,
        remove: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["create", "remove"]
    ) -> bool: ...

class MutateFeedItemTargetResult(proto.Message):
    resource_name: str
    feed_item_target: FeedItemTarget
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        feed_item_target: FeedItemTarget = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["resource_name", "feed_item_target"]
    ) -> bool: ...

class MutateFeedItemTargetsRequest(proto.Message):
    customer_id: str
    operations: MutableSequence[FeedItemTargetOperation]
    partial_failure: bool
    response_content_type: ResponseContentTypeEnum.ResponseContentType
    validate_only: bool
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        customer_id: str = ...,
        operations: MutableSequence[FeedItemTargetOperation] = ...,
        partial_failure: bool = ...,
        response_content_type: ResponseContentTypeEnum.ResponseContentType = ...,
        validate_only: bool = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "customer_id",
            "operations",
            "partial_failure",
            "response_content_type",
            "validate_only",
        ],
    ) -> bool: ...

class MutateFeedItemTargetsResponse(proto.Message):
    partial_failure_error: Status
    results: MutableSequence[MutateFeedItemTargetResult]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        partial_failure_error: Status = ...,
        results: MutableSequence[MutateFeedItemTargetResult] = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["partial_failure_error", "results"]
    ) -> bool: ...
