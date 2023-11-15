from collections.abc import Mapping, MutableSequence
from typing import Any, TypeVar

import google.protobuf.message
import proto
from google.rpc.status_pb2 import Status

from google.ads.googleads.v15.resources.types.feed_item_set_link import FeedItemSetLink

_M = TypeVar("_M")

class FeedItemSetLinkOperation(proto.Message):
    create: FeedItemSetLink
    remove: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        create: FeedItemSetLink = ...,
        remove: str = ...
    ) -> None: ...

class MutateFeedItemSetLinkResult(proto.Message):
    resource_name: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...
    ) -> None: ...

class MutateFeedItemSetLinksRequest(proto.Message):
    customer_id: str
    operations: MutableSequence[FeedItemSetLinkOperation]
    partial_failure: bool
    validate_only: bool
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        customer_id: str = ...,
        operations: MutableSequence[FeedItemSetLinkOperation] = ...,
        partial_failure: bool = ...,
        validate_only: bool = ...
    ) -> None: ...

class MutateFeedItemSetLinksResponse(proto.Message):
    results: MutableSequence[MutateFeedItemSetLinkResult]
    partial_failure_error: Status
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        results: MutableSequence[MutateFeedItemSetLinkResult] = ...,
        partial_failure_error: Status = ...
    ) -> None: ...
