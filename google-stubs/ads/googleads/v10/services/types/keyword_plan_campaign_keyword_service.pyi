from typing import Any

import proto
from google.protobuf.field_mask_pb2 import FieldMask
from google.rpc.status_pb2 import Status

from google.ads.googleads.v10.resources.types.keyword_plan_campaign_keyword import (
    KeywordPlanCampaignKeyword,
)

class KeywordPlanCampaignKeywordOperation(proto.Message):
    update_mask: FieldMask
    create: KeywordPlanCampaignKeyword
    update: KeywordPlanCampaignKeyword
    remove: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        update_mask: FieldMask = ...,
        create: KeywordPlanCampaignKeyword = ...,
        update: KeywordPlanCampaignKeyword = ...,
        remove: str = ...
    ) -> None: ...

class MutateKeywordPlanCampaignKeywordResult(proto.Message):
    resource_name: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...
    ) -> None: ...

class MutateKeywordPlanCampaignKeywordsRequest(proto.Message):
    customer_id: str
    operations: list[KeywordPlanCampaignKeywordOperation]
    partial_failure: bool
    validate_only: bool
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        customer_id: str = ...,
        operations: list[KeywordPlanCampaignKeywordOperation] = ...,
        partial_failure: bool = ...,
        validate_only: bool = ...
    ) -> None: ...

class MutateKeywordPlanCampaignKeywordsResponse(proto.Message):
    partial_failure_error: Status
    results: list[MutateKeywordPlanCampaignKeywordResult]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        partial_failure_error: Status = ...,
        results: list[MutateKeywordPlanCampaignKeywordResult] = ...
    ) -> None: ...
