import proto
from _typeshed import Incomplete
from google.rpc import status_pb2 as status_pb2

__protobuf__: Incomplete

class MutateCampaignSharedSetsRequest(proto.Message):
    customer_id: Incomplete
    operations: Incomplete
    partial_failure: Incomplete
    validate_only: Incomplete
    response_content_type: Incomplete

class CampaignSharedSetOperation(proto.Message):
    create: Incomplete
    remove: Incomplete

class MutateCampaignSharedSetsResponse(proto.Message):
    partial_failure_error: Incomplete
    results: Incomplete

class MutateCampaignSharedSetResult(proto.Message):
    resource_name: Incomplete
    campaign_shared_set: Incomplete
