from typing import Any

import proto
from google.protobuf import field_mask_pb2 as field_mask_pb2
from google.rpc import status_pb2 as status_pb2

from google.ads.googleads.v9.resources.types import feed_item_set as feed_item_set

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
    partial_failure_error: Any

class MutateFeedItemSetResult(proto.Message):
    resource_name: Any
