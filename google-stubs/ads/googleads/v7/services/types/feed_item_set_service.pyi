from typing import Any

import proto

from google.ads.googleads.v7.resources.types import feed_item_set as feed_item_set

__protobuf__: Any

class GetFeedItemSetRequest(proto.Message):
    resource_name: Any

class MutateFeedItemSetsRequest(proto.Message):
    customer_id: Any
    operations: Any
    partial_failure: Any
    validate_only: Any

class FeedItemSetOperation(proto.Message):
    update_mask: Any
    create: Any
    update: Any
    remove: Any

class MutateFeedItemSetsResponse(proto.Message):
    results: Any

class MutateFeedItemSetResult(proto.Message):
    resource_name: Any
