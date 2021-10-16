from typing import Any

import proto

__protobuf__: Any

class GetCustomerExtensionSettingRequest(proto.Message):
    resource_name: Any

class MutateCustomerExtensionSettingsRequest(proto.Message):
    customer_id: Any
    operations: Any
    partial_failure: Any
    validate_only: Any
    response_content_type: Any

class CustomerExtensionSettingOperation(proto.Message):
    update_mask: Any
    create: Any
    update: Any
    remove: Any

class MutateCustomerExtensionSettingsResponse(proto.Message):
    partial_failure_error: Any
    results: Any

class MutateCustomerExtensionSettingResult(proto.Message):
    resource_name: Any
    customer_extension_setting: Any
