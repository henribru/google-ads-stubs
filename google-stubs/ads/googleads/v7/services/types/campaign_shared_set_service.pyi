from typing import Any

import proto

__protobuf__: Any

class GetCampaignSharedSetRequest(proto.Message):
    resource_name: Any

class MutateCampaignSharedSetsRequest(proto.Message):
    customer_id: Any
    operations: Any
    partial_failure: Any
    validate_only: Any
    response_content_type: Any

class CampaignSharedSetOperation(proto.Message):
    create: Any
    remove: Any

class MutateCampaignSharedSetsResponse(proto.Message):
    partial_failure_error: Any
    results: Any

class MutateCampaignSharedSetResult(proto.Message):
    resource_name: Any
    campaign_shared_set: Any
