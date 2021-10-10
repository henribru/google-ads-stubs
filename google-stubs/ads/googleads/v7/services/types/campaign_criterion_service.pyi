from typing import Any

import proto

__protobuf__: Any

class GetCampaignCriterionRequest(proto.Message):
    resource_name: Any

class MutateCampaignCriteriaRequest(proto.Message):
    customer_id: Any
    operations: Any
    partial_failure: Any
    validate_only: Any
    response_content_type: Any

class CampaignCriterionOperation(proto.Message):
    update_mask: Any
    create: Any
    update: Any
    remove: Any

class MutateCampaignCriteriaResponse(proto.Message):
    partial_failure_error: Any
    results: Any

class MutateCampaignCriterionResult(proto.Message):
    resource_name: Any
    campaign_criterion: Any
