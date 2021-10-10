from typing import Any

import proto

__protobuf__: Any

class GetCampaignExtensionSettingRequest(proto.Message):
    resource_name: Any

class MutateCampaignExtensionSettingsRequest(proto.Message):
    customer_id: Any
    operations: Any
    partial_failure: Any
    validate_only: Any
    response_content_type: Any

class CampaignExtensionSettingOperation(proto.Message):
    update_mask: Any
    create: Any
    update: Any
    remove: Any

class MutateCampaignExtensionSettingsResponse(proto.Message):
    partial_failure_error: Any
    results: Any

class MutateCampaignExtensionSettingResult(proto.Message):
    resource_name: Any
    campaign_extension_setting: Any
