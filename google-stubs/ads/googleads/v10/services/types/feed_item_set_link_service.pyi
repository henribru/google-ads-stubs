from typing import Any

import proto
from google.rpc.status_pb2 import Status

from google.ads.googleads.v10.resources.types.feed_item_set_link import FeedItemSetLink

class FeedItemSetLinkOperation(proto.Message):
    create: FeedItemSetLink
    remove: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        create: FeedItemSetLink = ...,
        remove: str = ...
    ) -> None: ...

class MutateFeedItemSetLinkResult(proto.Message):
    resource_name: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...
    ) -> None: ...

class MutateFeedItemSetLinksRequest(proto.Message):
    customer_id: str
    operations: list[FeedItemSetLinkOperation]
    partial_failure: bool
    validate_only: bool
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        customer_id: str = ...,
        operations: list[FeedItemSetLinkOperation] = ...,
        partial_failure: bool = ...,
        validate_only: bool = ...
    ) -> None: ...

class MutateFeedItemSetLinksResponse(proto.Message):
    results: list[MutateFeedItemSetLinkResult]
    partial_failure_error: Status
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        results: list[MutateFeedItemSetLinkResult] = ...,
        partial_failure_error: Status = ...
    ) -> None: ...
