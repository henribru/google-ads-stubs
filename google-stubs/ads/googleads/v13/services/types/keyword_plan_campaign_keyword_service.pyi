from collections.abc import Mapping, MutableSequence
from typing import Any, TypeVar

import google.protobuf.message
import proto
from google.protobuf.field_mask_pb2 import FieldMask
from google.rpc.status_pb2 import Status

from google.ads.googleads.v13.resources.types.keyword_plan_campaign_keyword import (
    KeywordPlanCampaignKeyword,
)

_M = TypeVar("_M")

class KeywordPlanCampaignKeywordOperation(proto.Message):
    update_mask: FieldMask
    create: KeywordPlanCampaignKeyword
    update: KeywordPlanCampaignKeyword
    remove: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        update_mask: FieldMask = ...,
        create: KeywordPlanCampaignKeyword = ...,
        update: KeywordPlanCampaignKeyword = ...,
        remove: str = ...
    ) -> None: ...

class MutateKeywordPlanCampaignKeywordResult(proto.Message):
    resource_name: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...
    ) -> None: ...

class MutateKeywordPlanCampaignKeywordsRequest(proto.Message):
    customer_id: str
    operations: MutableSequence[KeywordPlanCampaignKeywordOperation]
    partial_failure: bool
    validate_only: bool
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        customer_id: str = ...,
        operations: MutableSequence[KeywordPlanCampaignKeywordOperation] = ...,
        partial_failure: bool = ...,
        validate_only: bool = ...
    ) -> None: ...

class MutateKeywordPlanCampaignKeywordsResponse(proto.Message):
    partial_failure_error: Status
    results: MutableSequence[MutateKeywordPlanCampaignKeywordResult]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        partial_failure_error: Status = ...,
        results: MutableSequence[MutateKeywordPlanCampaignKeywordResult] = ...
    ) -> None: ...
