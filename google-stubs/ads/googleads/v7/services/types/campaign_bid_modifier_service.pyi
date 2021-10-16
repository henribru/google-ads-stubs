from typing import Any

import proto

__protobuf__: Any

class GetCampaignBidModifierRequest(proto.Message):
    resource_name: Any

class MutateCampaignBidModifiersRequest(proto.Message):
    customer_id: Any
    operations: Any
    partial_failure: Any
    validate_only: Any
    response_content_type: Any

class CampaignBidModifierOperation(proto.Message):
    update_mask: Any
    create: Any
    update: Any
    remove: Any

class MutateCampaignBidModifiersResponse(proto.Message):
    partial_failure_error: Any
    results: Any

class MutateCampaignBidModifierResult(proto.Message):
    resource_name: Any
    campaign_bid_modifier: Any