from collections.abc import MutableSequence
from google.rpc.status_pb2 import Status
from collections.abc import MutableSequence
from google.ads.googleads.v19.resources.types.keyword_plan_campaign_keyword import KeywordPlanCampaignKeyword
from google.ads.googleads.v19.resources.types.keyword_plan_campaign_keyword import KeywordPlanCampaignKeyword
from google.protobuf.field_mask_pb2 import FieldMask
import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class KeywordPlanCampaignKeywordOperation(proto.Message):
    update_mask: FieldMask
    create: KeywordPlanCampaignKeyword
    update: KeywordPlanCampaignKeyword
    remove: str
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., update_mask: FieldMask = ..., create: KeywordPlanCampaignKeyword = ..., update: KeywordPlanCampaignKeyword = ..., remove: str = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["update_mask", "create", "update", "remove"]) -> bool: ...
class MutateKeywordPlanCampaignKeywordResult(proto.Message):
    resource_name: str
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., resource_name: str = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["resource_name"]) -> bool: ...
class MutateKeywordPlanCampaignKeywordsRequest(proto.Message):
    customer_id: str
    operations: MutableSequence[KeywordPlanCampaignKeywordOperation]
    partial_failure: bool
    validate_only: bool
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., customer_id: str = ..., operations: MutableSequence[KeywordPlanCampaignKeywordOperation] = ..., partial_failure: bool = ..., validate_only: bool = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["customer_id", "operations", "partial_failure", "validate_only"]) -> bool: ...
class MutateKeywordPlanCampaignKeywordsResponse(proto.Message):
    partial_failure_error: Status
    results: MutableSequence[MutateKeywordPlanCampaignKeywordResult]
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., partial_failure_error: Status = ..., results: MutableSequence[MutateKeywordPlanCampaignKeywordResult] = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["partial_failure_error", "results"]) -> bool: ...
