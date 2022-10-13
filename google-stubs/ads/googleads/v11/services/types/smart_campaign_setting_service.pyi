from typing import Any

import proto
from google.protobuf.field_mask_pb2 import FieldMask
from google.rpc.status_pb2 import Status

from google.ads.googleads.v11.enums.types.response_content_type import (
    ResponseContentTypeEnum,
)
from google.ads.googleads.v11.resources.types.smart_campaign_setting import (
    SmartCampaignSetting,
)

class MutateSmartCampaignSettingResult(proto.Message):
    resource_name: str
    smart_campaign_setting: SmartCampaignSetting
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        smart_campaign_setting: SmartCampaignSetting = ...
    ) -> None: ...

class MutateSmartCampaignSettingsRequest(proto.Message):
    customer_id: str
    operations: list[SmartCampaignSettingOperation]
    partial_failure: bool
    validate_only: bool
    response_content_type: ResponseContentTypeEnum.ResponseContentType
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        customer_id: str = ...,
        operations: list[SmartCampaignSettingOperation] = ...,
        partial_failure: bool = ...,
        validate_only: bool = ...,
        response_content_type: ResponseContentTypeEnum.ResponseContentType = ...
    ) -> None: ...

class MutateSmartCampaignSettingsResponse(proto.Message):
    partial_failure_error: Status
    results: list[MutateSmartCampaignSettingResult]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        partial_failure_error: Status = ...,
        results: list[MutateSmartCampaignSettingResult] = ...
    ) -> None: ...

class SmartCampaignSettingOperation(proto.Message):
    update: SmartCampaignSetting
    update_mask: FieldMask
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        update: SmartCampaignSetting = ...,
        update_mask: FieldMask = ...
    ) -> None: ...
