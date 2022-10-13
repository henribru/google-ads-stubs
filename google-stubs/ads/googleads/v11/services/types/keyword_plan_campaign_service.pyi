from typing import Any

import proto
from google.protobuf.field_mask_pb2 import FieldMask
from google.rpc.status_pb2 import Status

from google.ads.googleads.v11.resources.types.keyword_plan_campaign import (
    KeywordPlanCampaign,
)

class KeywordPlanCampaignOperation(proto.Message):
    update_mask: FieldMask
    create: KeywordPlanCampaign
    update: KeywordPlanCampaign
    remove: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        update_mask: FieldMask = ...,
        create: KeywordPlanCampaign = ...,
        update: KeywordPlanCampaign = ...,
        remove: str = ...
    ) -> None: ...

class MutateKeywordPlanCampaignResult(proto.Message):
    resource_name: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...
    ) -> None: ...

class MutateKeywordPlanCampaignsRequest(proto.Message):
    customer_id: str
    operations: list[KeywordPlanCampaignOperation]
    partial_failure: bool
    validate_only: bool
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        customer_id: str = ...,
        operations: list[KeywordPlanCampaignOperation] = ...,
        partial_failure: bool = ...,
        validate_only: bool = ...
    ) -> None: ...

class MutateKeywordPlanCampaignsResponse(proto.Message):
    partial_failure_error: Status
    results: list[MutateKeywordPlanCampaignResult]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        partial_failure_error: Status = ...,
        results: list[MutateKeywordPlanCampaignResult] = ...
    ) -> None: ...
