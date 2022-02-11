from typing import Any

import proto
from google.rpc import status_pb2 as status_pb2

__protobuf__: Any

class MutateCampaignCustomizersRequest(proto.Message):
    customer_id: Any
    operations: Any
    partial_failure: Any
    validate_only: Any
    response_content_type: Any

class CampaignCustomizerOperation(proto.Message):
    create: Any
    remove: Any

class MutateCampaignCustomizersResponse(proto.Message):
    results: Any
    partial_failure_error: Any

class MutateCampaignCustomizerResult(proto.Message):
    resource_name: Any
    campaign_customizer: Any
