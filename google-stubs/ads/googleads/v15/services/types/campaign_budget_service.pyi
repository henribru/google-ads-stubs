from collections.abc import Mapping, MutableSequence
from typing import Any, TypeVar

import google.protobuf.message
import proto
from google.protobuf.field_mask_pb2 import FieldMask
from google.rpc.status_pb2 import Status

from google.ads.googleads.v15.enums.types.response_content_type import (
    ResponseContentTypeEnum,
)
from google.ads.googleads.v15.resources.types.campaign_budget import CampaignBudget

_M = TypeVar("_M")

class CampaignBudgetOperation(proto.Message):
    update_mask: FieldMask
    create: CampaignBudget
    update: CampaignBudget
    remove: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        update_mask: FieldMask = ...,
        create: CampaignBudget = ...,
        update: CampaignBudget = ...,
        remove: str = ...
    ) -> None: ...

class MutateCampaignBudgetResult(proto.Message):
    resource_name: str
    campaign_budget: CampaignBudget
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        campaign_budget: CampaignBudget = ...
    ) -> None: ...

class MutateCampaignBudgetsRequest(proto.Message):
    customer_id: str
    operations: MutableSequence[CampaignBudgetOperation]
    partial_failure: bool
    validate_only: bool
    response_content_type: ResponseContentTypeEnum.ResponseContentType
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        customer_id: str = ...,
        operations: MutableSequence[CampaignBudgetOperation] = ...,
        partial_failure: bool = ...,
        validate_only: bool = ...,
        response_content_type: ResponseContentTypeEnum.ResponseContentType = ...
    ) -> None: ...

class MutateCampaignBudgetsResponse(proto.Message):
    partial_failure_error: Status
    results: MutableSequence[MutateCampaignBudgetResult]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        partial_failure_error: Status = ...,
        results: MutableSequence[MutateCampaignBudgetResult] = ...
    ) -> None: ...
