from collections.abc import Mapping, MutableSequence
from typing import Any, TypeVar

import google.protobuf.message
import proto
from google.protobuf.field_mask_pb2 import FieldMask

from google.ads.googleads.v14.enums.types.response_content_type import (
    ResponseContentTypeEnum,
)
from google.ads.googleads.v14.resources.types.conversion_goal_campaign_config import (
    ConversionGoalCampaignConfig,
)

_M = TypeVar("_M")

class ConversionGoalCampaignConfigOperation(proto.Message):
    update_mask: FieldMask
    update: ConversionGoalCampaignConfig
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        update_mask: FieldMask = ...,
        update: ConversionGoalCampaignConfig = ...
    ) -> None: ...

class MutateConversionGoalCampaignConfigResult(proto.Message):
    resource_name: str
    conversion_goal_campaign_config: ConversionGoalCampaignConfig
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        conversion_goal_campaign_config: ConversionGoalCampaignConfig = ...
    ) -> None: ...

class MutateConversionGoalCampaignConfigsRequest(proto.Message):
    customer_id: str
    operations: MutableSequence[ConversionGoalCampaignConfigOperation]
    validate_only: bool
    response_content_type: ResponseContentTypeEnum.ResponseContentType
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        customer_id: str = ...,
        operations: MutableSequence[ConversionGoalCampaignConfigOperation] = ...,
        validate_only: bool = ...,
        response_content_type: ResponseContentTypeEnum.ResponseContentType = ...
    ) -> None: ...

class MutateConversionGoalCampaignConfigsResponse(proto.Message):
    results: MutableSequence[MutateConversionGoalCampaignConfigResult]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        results: MutableSequence[MutateConversionGoalCampaignConfigResult] = ...
    ) -> None: ...
