from typing import Any

import proto
from google.protobuf import field_mask_pb2 as field_mask_pb2
from google.rpc import status_pb2 as status_pb2

__protobuf__: Any

class GetSmartCampaignSettingRequest(proto.Message):
    resource_name: Any

class MutateSmartCampaignSettingsRequest(proto.Message):
    customer_id: Any
    operations: Any
    partial_failure: Any
    validate_only: Any
    response_content_type: Any

class SmartCampaignSettingOperation(proto.Message):
    update: Any
    update_mask: Any

class MutateSmartCampaignSettingsResponse(proto.Message):
    partial_failure_error: Any
    results: Any

class MutateSmartCampaignSettingResult(proto.Message):
    resource_name: Any
    smart_campaign_setting: Any
