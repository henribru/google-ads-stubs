from typing import Any

import proto
from google.protobuf import field_mask_pb2 as field_mask_pb2
from google.rpc import status_pb2 as status_pb2

__protobuf__: Any

class GetAdGroupExtensionSettingRequest(proto.Message):
    resource_name: Any

class MutateAdGroupExtensionSettingsRequest(proto.Message):
    customer_id: Any
    operations: Any
    partial_failure: Any
    validate_only: Any

class AdGroupExtensionSettingOperation(proto.Message):
    update_mask: Any
    response_content_type: Any
    create: Any
    update: Any
    remove: Any

class MutateAdGroupExtensionSettingsResponse(proto.Message):
    partial_failure_error: Any
    results: Any

class MutateAdGroupExtensionSettingResult(proto.Message):
    resource_name: Any
    ad_group_extension_setting: Any