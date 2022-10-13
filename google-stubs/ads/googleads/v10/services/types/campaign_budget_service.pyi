from typing import Any

import proto
from google.protobuf.field_mask_pb2 import FieldMask
from google.rpc.status_pb2 import Status

from google.ads.googleads.v10.enums.types.response_content_type import (
    ResponseContentTypeEnum,
)
from google.ads.googleads.v10.resources.types.campaign_budget import CampaignBudget

class CampaignBudgetOperation(proto.Message):
    update_mask: FieldMask
    create: CampaignBudget
    update: CampaignBudget
    remove: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        update_mask: FieldMask = ...,
        create: CampaignBudget = ...,
        update: CampaignBudget = ...,
        remove: str = ...
    ) -> None: ...

class MutateCampaignBudgetResult(proto.Message):
    resource_name: str
    campaign_budget: CampaignBudget
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        campaign_budget: CampaignBudget = ...
    ) -> None: ...

class MutateCampaignBudgetsRequest(proto.Message):
    customer_id: str
    operations: list[CampaignBudgetOperation]
    partial_failure: bool
    validate_only: bool
    response_content_type: ResponseContentTypeEnum.ResponseContentType
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        customer_id: str = ...,
        operations: list[CampaignBudgetOperation] = ...,
        partial_failure: bool = ...,
        validate_only: bool = ...,
        response_content_type: ResponseContentTypeEnum.ResponseContentType = ...
    ) -> None: ...

class MutateCampaignBudgetsResponse(proto.Message):
    partial_failure_error: Status
    results: list[MutateCampaignBudgetResult]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        partial_failure_error: Status = ...,
        results: list[MutateCampaignBudgetResult] = ...
    ) -> None: ...
