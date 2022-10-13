from typing import Any

import proto
from google.protobuf.field_mask_pb2 import FieldMask
from google.rpc.status_pb2 import Status

from google.ads.googleads.v10.enums.types.response_content_type import (
    ResponseContentTypeEnum,
)
from google.ads.googleads.v10.resources.types.campaign_extension_setting import (
    CampaignExtensionSetting,
)

class CampaignExtensionSettingOperation(proto.Message):
    update_mask: FieldMask
    create: CampaignExtensionSetting
    update: CampaignExtensionSetting
    remove: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        update_mask: FieldMask = ...,
        create: CampaignExtensionSetting = ...,
        update: CampaignExtensionSetting = ...,
        remove: str = ...
    ) -> None: ...

class MutateCampaignExtensionSettingResult(proto.Message):
    resource_name: str
    campaign_extension_setting: CampaignExtensionSetting
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        campaign_extension_setting: CampaignExtensionSetting = ...
    ) -> None: ...

class MutateCampaignExtensionSettingsRequest(proto.Message):
    customer_id: str
    operations: list[CampaignExtensionSettingOperation]
    partial_failure: bool
    validate_only: bool
    response_content_type: ResponseContentTypeEnum.ResponseContentType
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        customer_id: str = ...,
        operations: list[CampaignExtensionSettingOperation] = ...,
        partial_failure: bool = ...,
        validate_only: bool = ...,
        response_content_type: ResponseContentTypeEnum.ResponseContentType = ...
    ) -> None: ...

class MutateCampaignExtensionSettingsResponse(proto.Message):
    partial_failure_error: Status
    results: list[MutateCampaignExtensionSettingResult]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        partial_failure_error: Status = ...,
        results: list[MutateCampaignExtensionSettingResult] = ...
    ) -> None: ...
