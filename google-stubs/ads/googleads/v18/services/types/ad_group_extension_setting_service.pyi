import proto
from _typeshed import Incomplete
from google.ads.googleads.v18.enums.types import response_content_type as gage_response_content_type
from google.ads.googleads.v18.resources.types import ad_group_extension_setting as gagr_ad_group_extension_setting
from google.protobuf import field_mask_pb2
from google.rpc import status_pb2
from typing import MutableSequence

__protobuf__: Incomplete

class MutateAdGroupExtensionSettingsRequest(proto.Message):
    customer_id: str
    operations: MutableSequence['AdGroupExtensionSettingOperation']
    partial_failure: bool
    validate_only: bool

class AdGroupExtensionSettingOperation(proto.Message):
    update_mask: field_mask_pb2.FieldMask
    response_content_type: gage_response_content_type.ResponseContentTypeEnum.ResponseContentType
    create: gagr_ad_group_extension_setting.AdGroupExtensionSetting
    update: gagr_ad_group_extension_setting.AdGroupExtensionSetting
    remove: str

class MutateAdGroupExtensionSettingsResponse(proto.Message):
    partial_failure_error: status_pb2.Status
    results: MutableSequence['MutateAdGroupExtensionSettingResult']

class MutateAdGroupExtensionSettingResult(proto.Message):
    resource_name: str
    ad_group_extension_setting: gagr_ad_group_extension_setting.AdGroupExtensionSetting
