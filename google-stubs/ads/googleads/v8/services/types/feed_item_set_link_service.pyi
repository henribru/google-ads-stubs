from typing import Any

import proto

from google.ads.googleads.v8.resources.types import (
    feed_item_set_link as feed_item_set_link,
)

__protobuf__: Any

class GetFeedItemSetLinkRequest(proto.Message):
    resource_name: Any

class MutateFeedItemSetLinksRequest(proto.Message):
    customer_id: Any
    operations: Any
    partial_failure: Any
    validate_only: Any

class FeedItemSetLinkOperation(proto.Message):
    create: Any
    remove: Any

class MutateFeedItemSetLinksResponse(proto.Message):
    results: Any

class MutateFeedItemSetLinkResult(proto.Message):
    resource_name: Any