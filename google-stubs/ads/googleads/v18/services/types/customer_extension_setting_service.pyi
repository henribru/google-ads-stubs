import proto
from _typeshed import Incomplete
from google.ads.googleads.v18.enums.types import response_content_type as gage_response_content_type
from google.ads.googleads.v18.resources.types import customer_extension_setting as gagr_customer_extension_setting
from google.protobuf import field_mask_pb2
from google.rpc import status_pb2
from typing import MutableSequence

__protobuf__: Incomplete

class MutateCustomerExtensionSettingsRequest(proto.Message):
    customer_id: str
    operations: MutableSequence['CustomerExtensionSettingOperation']
    partial_failure: bool
    validate_only: bool
    response_content_type: gage_response_content_type.ResponseContentTypeEnum.ResponseContentType

class CustomerExtensionSettingOperation(proto.Message):
    update_mask: field_mask_pb2.FieldMask
    create: gagr_customer_extension_setting.CustomerExtensionSetting
    update: gagr_customer_extension_setting.CustomerExtensionSetting
    remove: str

class MutateCustomerExtensionSettingsResponse(proto.Message):
    partial_failure_error: status_pb2.Status
    results: MutableSequence['MutateCustomerExtensionSettingResult']

class MutateCustomerExtensionSettingResult(proto.Message):
    resource_name: str
    customer_extension_setting: gagr_customer_extension_setting.CustomerExtensionSetting
