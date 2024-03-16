from collections.abc import Mapping, MutableSequence
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from google.protobuf.field_mask_pb2 import FieldMask
from google.rpc.status_pb2 import Status
from typing_extensions import Literal

from google.ads.googleads.v16.enums.types.response_content_type import (
    ResponseContentTypeEnum,
)
from google.ads.googleads.v16.resources.types.ad_group_feed import AdGroupFeed

_M = TypeVar("_M")

class AdGroupFeedOperation(proto.Message):
    update_mask: FieldMask
    create: AdGroupFeed
    update: AdGroupFeed
    remove: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        update_mask: FieldMask = ...,
        create: AdGroupFeed = ...,
        update: AdGroupFeed = ...,
        remove: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["update_mask", "create", "update", "remove"]
    ) -> bool: ...

class MutateAdGroupFeedResult(proto.Message):
    resource_name: str
    ad_group_feed: AdGroupFeed
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        ad_group_feed: AdGroupFeed = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["resource_name", "ad_group_feed"]
    ) -> bool: ...

class MutateAdGroupFeedsRequest(proto.Message):
    customer_id: str
    operations: MutableSequence[AdGroupFeedOperation]
    partial_failure: bool
    validate_only: bool
    response_content_type: ResponseContentTypeEnum.ResponseContentType
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        customer_id: str = ...,
        operations: MutableSequence[AdGroupFeedOperation] = ...,
        partial_failure: bool = ...,
        validate_only: bool = ...,
        response_content_type: ResponseContentTypeEnum.ResponseContentType = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "customer_id",
            "operations",
            "partial_failure",
            "validate_only",
            "response_content_type",
        ],
    ) -> bool: ...

class MutateAdGroupFeedsResponse(proto.Message):
    partial_failure_error: Status
    results: MutableSequence[MutateAdGroupFeedResult]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        partial_failure_error: Status = ...,
        results: MutableSequence[MutateAdGroupFeedResult] = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["partial_failure_error", "results"]
    ) -> bool: ...
