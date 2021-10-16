from typing import Any

import proto
from google.rpc import status_pb2 as status_pb2

__protobuf__: Any

class GetFeedMappingRequest(proto.Message):
    resource_name: Any

class MutateFeedMappingsRequest(proto.Message):
    customer_id: Any
    operations: Any
    partial_failure: Any
    validate_only: Any
    response_content_type: Any

class FeedMappingOperation(proto.Message):
    create: Any
    remove: Any

class MutateFeedMappingsResponse(proto.Message):
    partial_failure_error: Any
    results: Any

class MutateFeedMappingResult(proto.Message):
    resource_name: Any
    feed_mapping: Any
