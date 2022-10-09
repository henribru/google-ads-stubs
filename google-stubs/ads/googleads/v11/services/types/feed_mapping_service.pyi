import proto
from _typeshed import Incomplete
from google.rpc import status_pb2 as status_pb2

__protobuf__: Incomplete

class MutateFeedMappingsRequest(proto.Message):
    customer_id: Incomplete
    operations: Incomplete
    partial_failure: Incomplete
    validate_only: Incomplete
    response_content_type: Incomplete

class FeedMappingOperation(proto.Message):
    create: Incomplete
    remove: Incomplete

class MutateFeedMappingsResponse(proto.Message):
    partial_failure_error: Incomplete
    results: Incomplete

class MutateFeedMappingResult(proto.Message):
    resource_name: Incomplete
    feed_mapping: Incomplete
