from typing import Any

import proto
from google.protobuf.field_mask_pb2 import FieldMask
from google.rpc.status_pb2 import Status

from google.ads.googleads.v10.enums.types.response_content_type import (
    ResponseContentTypeEnum,
)
from google.ads.googleads.v10.resources.types.ad_group_extension_setting import (
    AdGroupExtensionSetting,
)

class AdGroupExtensionSettingOperation(proto.Message):
    update_mask: FieldMask
    response_content_type: ResponseContentTypeEnum.ResponseContentType
    create: AdGroupExtensionSetting
    update: AdGroupExtensionSetting
    remove: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        update_mask: FieldMask = ...,
        response_content_type: ResponseContentTypeEnum.ResponseContentType = ...,
        create: AdGroupExtensionSetting = ...,
        update: AdGroupExtensionSetting = ...,
        remove: str = ...
    ) -> None: ...

class MutateAdGroupExtensionSettingResult(proto.Message):
    resource_name: str
    ad_group_extension_setting: AdGroupExtensionSetting
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        ad_group_extension_setting: AdGroupExtensionSetting = ...
    ) -> None: ...

class MutateAdGroupExtensionSettingsRequest(proto.Message):
    customer_id: str
    operations: list[AdGroupExtensionSettingOperation]
    partial_failure: bool
    validate_only: bool
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        customer_id: str = ...,
        operations: list[AdGroupExtensionSettingOperation] = ...,
        partial_failure: bool = ...,
        validate_only: bool = ...
    ) -> None: ...

class MutateAdGroupExtensionSettingsResponse(proto.Message):
    partial_failure_error: Status
    results: list[MutateAdGroupExtensionSettingResult]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        partial_failure_error: Status = ...,
        results: list[MutateAdGroupExtensionSettingResult] = ...
    ) -> None: ...
