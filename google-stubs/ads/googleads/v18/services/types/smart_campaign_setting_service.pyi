import proto
from _typeshed import Incomplete
from google.ads.googleads.v18.enums.types import response_content_type as gage_response_content_type, smart_campaign_not_eligible_reason, smart_campaign_status as gage_smart_campaign_status
from google.ads.googleads.v18.resources.types import smart_campaign_setting as gagr_smart_campaign_setting
from google.protobuf import field_mask_pb2
from google.rpc import status_pb2
from typing import MutableSequence

__protobuf__: Incomplete

class GetSmartCampaignStatusRequest(proto.Message):
    resource_name: str

class SmartCampaignNotEligibleDetails(proto.Message):
    not_eligible_reason: smart_campaign_not_eligible_reason.SmartCampaignNotEligibleReasonEnum.SmartCampaignNotEligibleReason

class SmartCampaignEligibleDetails(proto.Message):
    last_impression_date_time: str
    end_date_time: str

class SmartCampaignPausedDetails(proto.Message):
    paused_date_time: str

class SmartCampaignRemovedDetails(proto.Message):
    removed_date_time: str

class SmartCampaignEndedDetails(proto.Message):
    end_date_time: str

class GetSmartCampaignStatusResponse(proto.Message):
    smart_campaign_status: gage_smart_campaign_status.SmartCampaignStatusEnum.SmartCampaignStatus
    not_eligible_details: SmartCampaignNotEligibleDetails
    eligible_details: SmartCampaignEligibleDetails
    paused_details: SmartCampaignPausedDetails
    removed_details: SmartCampaignRemovedDetails
    ended_details: SmartCampaignEndedDetails

class MutateSmartCampaignSettingsRequest(proto.Message):
    customer_id: str
    operations: MutableSequence['SmartCampaignSettingOperation']
    partial_failure: bool
    validate_only: bool
    response_content_type: gage_response_content_type.ResponseContentTypeEnum.ResponseContentType

class SmartCampaignSettingOperation(proto.Message):
    update: gagr_smart_campaign_setting.SmartCampaignSetting
    update_mask: field_mask_pb2.FieldMask

class MutateSmartCampaignSettingsResponse(proto.Message):
    partial_failure_error: status_pb2.Status
    results: MutableSequence['MutateSmartCampaignSettingResult']

class MutateSmartCampaignSettingResult(proto.Message):
    resource_name: str
    smart_campaign_setting: gagr_smart_campaign_setting.SmartCampaignSetting
