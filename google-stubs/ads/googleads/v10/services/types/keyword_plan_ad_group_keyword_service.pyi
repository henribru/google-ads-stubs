from typing import Any

import proto
from google.protobuf.field_mask_pb2 import FieldMask
from google.rpc.status_pb2 import Status

from google.ads.googleads.v10.resources.types.keyword_plan_ad_group_keyword import (
    KeywordPlanAdGroupKeyword,
)

class KeywordPlanAdGroupKeywordOperation(proto.Message):
    update_mask: FieldMask
    create: KeywordPlanAdGroupKeyword
    update: KeywordPlanAdGroupKeyword
    remove: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        update_mask: FieldMask = ...,
        create: KeywordPlanAdGroupKeyword = ...,
        update: KeywordPlanAdGroupKeyword = ...,
        remove: str = ...
    ) -> None: ...

class MutateKeywordPlanAdGroupKeywordResult(proto.Message):
    resource_name: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...
    ) -> None: ...

class MutateKeywordPlanAdGroupKeywordsRequest(proto.Message):
    customer_id: str
    operations: list[KeywordPlanAdGroupKeywordOperation]
    partial_failure: bool
    validate_only: bool
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        customer_id: str = ...,
        operations: list[KeywordPlanAdGroupKeywordOperation] = ...,
        partial_failure: bool = ...,
        validate_only: bool = ...
    ) -> None: ...

class MutateKeywordPlanAdGroupKeywordsResponse(proto.Message):
    partial_failure_error: Status
    results: list[MutateKeywordPlanAdGroupKeywordResult]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        partial_failure_error: Status = ...,
        results: list[MutateKeywordPlanAdGroupKeywordResult] = ...
    ) -> None: ...
