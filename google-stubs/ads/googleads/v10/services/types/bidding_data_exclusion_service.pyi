import proto
from _typeshed import Incomplete
from google.protobuf import field_mask_pb2 as field_mask_pb2
from google.rpc import status_pb2 as status_pb2

__protobuf__: Incomplete

class MutateBiddingDataExclusionsRequest(proto.Message):
    customer_id: Incomplete
    operations: Incomplete
    partial_failure: Incomplete
    validate_only: Incomplete
    response_content_type: Incomplete

class BiddingDataExclusionOperation(proto.Message):
    update_mask: Incomplete
    create: Incomplete
    update: Incomplete
    remove: Incomplete

class MutateBiddingDataExclusionsResponse(proto.Message):
    partial_failure_error: Incomplete
    results: Incomplete

class MutateBiddingDataExclusionsResult(proto.Message):
    resource_name: Incomplete
    bidding_data_exclusion: Incomplete
