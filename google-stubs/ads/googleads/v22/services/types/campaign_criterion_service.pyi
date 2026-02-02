from google.ads.googleads.v22.resources.types.campaign_criterion import CampaignCriterion
from collections.abc import MutableSequence
from google.rpc.status_pb2 import Status
from google.ads.googleads.v22.enums.types.response_content_type import ResponseContentTypeEnum
from collections.abc import MutableSequence
from google.ads.googleads.v22.resources.types.campaign_criterion import CampaignCriterion
from google.ads.googleads.v22.resources.types.campaign_criterion import CampaignCriterion
from google.protobuf.field_mask_pb2 import FieldMask
import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class CampaignCriterionOperation(proto.Message):
    update_mask: FieldMask
    create: CampaignCriterion
    update: CampaignCriterion
    remove: str
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, update_mask: FieldMask = ..., create: CampaignCriterion = ..., update: CampaignCriterion = ..., remove: str = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["update_mask", "create", "update", "remove"]) -> bool: ...
class MutateCampaignCriteriaRequest(proto.Message):
    customer_id: str
    operations: MutableSequence[CampaignCriterionOperation]
    partial_failure: bool
    validate_only: bool
    response_content_type: ResponseContentTypeEnum.ResponseContentType
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, customer_id: str = ..., operations: MutableSequence[CampaignCriterionOperation] = ..., partial_failure: bool = ..., validate_only: bool = ..., response_content_type: ResponseContentTypeEnum.ResponseContentType = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["customer_id", "operations", "partial_failure", "validate_only", "response_content_type"]) -> bool: ...
class MutateCampaignCriteriaResponse(proto.Message):
    partial_failure_error: Status
    results: MutableSequence[MutateCampaignCriterionResult]
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, partial_failure_error: Status = ..., results: MutableSequence[MutateCampaignCriterionResult] = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["partial_failure_error", "results"]) -> bool: ...
class MutateCampaignCriterionResult(proto.Message):
    resource_name: str
    campaign_criterion: CampaignCriterion
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, resource_name: str = ..., campaign_criterion: CampaignCriterion = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["resource_name", "campaign_criterion"]) -> bool: ...
