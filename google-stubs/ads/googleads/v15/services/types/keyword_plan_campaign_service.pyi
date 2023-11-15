from collections.abc import Mapping, MutableSequence
from typing import Any, TypeVar

import google.protobuf.message
import proto
from google.protobuf.field_mask_pb2 import FieldMask
from google.rpc.status_pb2 import Status

from google.ads.googleads.v15.resources.types.keyword_plan_campaign import (
    KeywordPlanCampaign,
)

_M = TypeVar("_M")

class KeywordPlanCampaignOperation(proto.Message):
    update_mask: FieldMask
    create: KeywordPlanCampaign
    update: KeywordPlanCampaign
    remove: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        update_mask: FieldMask = ...,
        create: KeywordPlanCampaign = ...,
        update: KeywordPlanCampaign = ...,
        remove: str = ...
    ) -> None: ...

class MutateKeywordPlanCampaignResult(proto.Message):
    resource_name: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...
    ) -> None: ...

class MutateKeywordPlanCampaignsRequest(proto.Message):
    customer_id: str
    operations: MutableSequence[KeywordPlanCampaignOperation]
    partial_failure: bool
    validate_only: bool
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        customer_id: str = ...,
        operations: MutableSequence[KeywordPlanCampaignOperation] = ...,
        partial_failure: bool = ...,
        validate_only: bool = ...
    ) -> None: ...

class MutateKeywordPlanCampaignsResponse(proto.Message):
    partial_failure_error: Status
    results: MutableSequence[MutateKeywordPlanCampaignResult]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        partial_failure_error: Status = ...,
        results: MutableSequence[MutateKeywordPlanCampaignResult] = ...
    ) -> None: ...
