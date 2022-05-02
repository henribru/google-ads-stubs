import proto
from _typeshed import Incomplete
from google.rpc import status_pb2 as status_pb2

__protobuf__: Incomplete

class MutateCampaignCustomizersRequest(proto.Message):
    customer_id: Incomplete
    operations: Incomplete
    partial_failure: Incomplete
    validate_only: Incomplete
    response_content_type: Incomplete

class CampaignCustomizerOperation(proto.Message):
    create: Incomplete
    remove: Incomplete

class MutateCampaignCustomizersResponse(proto.Message):
    results: Incomplete
    partial_failure_error: Incomplete

class MutateCampaignCustomizerResult(proto.Message):
    resource_name: Incomplete
    campaign_customizer: Incomplete
