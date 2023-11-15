from collections.abc import Mapping, MutableSequence
from typing import Any, TypeVar

import google.protobuf.message
import proto
from google.protobuf.field_mask_pb2 import FieldMask
from google.rpc.status_pb2 import Status

from google.ads.googleads.v13.enums.types.response_content_type import (
    ResponseContentTypeEnum,
)
from google.ads.googleads.v13.enums.types.smart_campaign_not_eligible_reason import (
    SmartCampaignNotEligibleReasonEnum,
)
from google.ads.googleads.v13.enums.types.smart_campaign_status import (
    SmartCampaignStatusEnum,
)
from google.ads.googleads.v13.resources.types.smart_campaign_setting import (
    SmartCampaignSetting,
)

_M = TypeVar("_M")

class GetSmartCampaignStatusRequest(proto.Message):
    resource_name: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...
    ) -> None: ...

class GetSmartCampaignStatusResponse(proto.Message):
    smart_campaign_status: SmartCampaignStatusEnum.SmartCampaignStatus
    not_eligible_details: SmartCampaignNotEligibleDetails
    eligible_details: SmartCampaignEligibleDetails
    paused_details: SmartCampaignPausedDetails
    removed_details: SmartCampaignRemovedDetails
    ended_details: SmartCampaignEndedDetails
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        smart_campaign_status: SmartCampaignStatusEnum.SmartCampaignStatus = ...,
        not_eligible_details: SmartCampaignNotEligibleDetails = ...,
        eligible_details: SmartCampaignEligibleDetails = ...,
        paused_details: SmartCampaignPausedDetails = ...,
        removed_details: SmartCampaignRemovedDetails = ...,
        ended_details: SmartCampaignEndedDetails = ...
    ) -> None: ...

class MutateSmartCampaignSettingResult(proto.Message):
    resource_name: str
    smart_campaign_setting: SmartCampaignSetting
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        smart_campaign_setting: SmartCampaignSetting = ...
    ) -> None: ...

class MutateSmartCampaignSettingsRequest(proto.Message):
    customer_id: str
    operations: MutableSequence[SmartCampaignSettingOperation]
    partial_failure: bool
    validate_only: bool
    response_content_type: ResponseContentTypeEnum.ResponseContentType
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        customer_id: str = ...,
        operations: MutableSequence[SmartCampaignSettingOperation] = ...,
        partial_failure: bool = ...,
        validate_only: bool = ...,
        response_content_type: ResponseContentTypeEnum.ResponseContentType = ...
    ) -> None: ...

class MutateSmartCampaignSettingsResponse(proto.Message):
    partial_failure_error: Status
    results: MutableSequence[MutateSmartCampaignSettingResult]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        partial_failure_error: Status = ...,
        results: MutableSequence[MutateSmartCampaignSettingResult] = ...
    ) -> None: ...

class SmartCampaignEligibleDetails(proto.Message):
    last_impression_date_time: str
    end_date_time: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        last_impression_date_time: str = ...,
        end_date_time: str = ...
    ) -> None: ...

class SmartCampaignEndedDetails(proto.Message):
    end_date_time: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        end_date_time: str = ...
    ) -> None: ...

class SmartCampaignNotEligibleDetails(proto.Message):
    not_eligible_reason: SmartCampaignNotEligibleReasonEnum.SmartCampaignNotEligibleReason
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        not_eligible_reason: SmartCampaignNotEligibleReasonEnum.SmartCampaignNotEligibleReason = ...
    ) -> None: ...

class SmartCampaignPausedDetails(proto.Message):
    paused_date_time: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        paused_date_time: str = ...
    ) -> None: ...

class SmartCampaignRemovedDetails(proto.Message):
    removed_date_time: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        removed_date_time: str = ...
    ) -> None: ...

class SmartCampaignSettingOperation(proto.Message):
    update: SmartCampaignSetting
    update_mask: FieldMask
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        update: SmartCampaignSetting = ...,
        update_mask: FieldMask = ...
    ) -> None: ...
