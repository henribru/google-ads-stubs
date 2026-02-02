from google.ads.googleads.v22.resources.types.ad_group_criterion import AdGroupCriterion
from collections.abc import MutableSequence
from google.rpc.status_pb2 import Status
from google.ads.googleads.v22.enums.types.response_content_type import ResponseContentTypeEnum
from collections.abc import MutableSequence
from google.ads.googleads.v22.resources.types.ad_group_criterion import AdGroupCriterion
from google.ads.googleads.v22.resources.types.ad_group_criterion import AdGroupCriterion
from collections.abc import MutableSequence
from google.ads.googleads.v22.common.types.policy import PolicyViolationKey
from google.protobuf.field_mask_pb2 import FieldMask
import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class AdGroupCriterionOperation(proto.Message):
    update_mask: FieldMask
    exempt_policy_violation_keys: MutableSequence[PolicyViolationKey]
    create: AdGroupCriterion
    update: AdGroupCriterion
    remove: str
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, update_mask: FieldMask = ..., exempt_policy_violation_keys: MutableSequence[PolicyViolationKey] = ..., create: AdGroupCriterion = ..., update: AdGroupCriterion = ..., remove: str = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["update_mask", "exempt_policy_violation_keys", "create", "update", "remove"]) -> bool: ...
class MutateAdGroupCriteriaRequest(proto.Message):
    customer_id: str
    operations: MutableSequence[AdGroupCriterionOperation]
    partial_failure: bool
    validate_only: bool
    response_content_type: ResponseContentTypeEnum.ResponseContentType
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, customer_id: str = ..., operations: MutableSequence[AdGroupCriterionOperation] = ..., partial_failure: bool = ..., validate_only: bool = ..., response_content_type: ResponseContentTypeEnum.ResponseContentType = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["customer_id", "operations", "partial_failure", "validate_only", "response_content_type"]) -> bool: ...
class MutateAdGroupCriteriaResponse(proto.Message):
    partial_failure_error: Status
    results: MutableSequence[MutateAdGroupCriterionResult]
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, partial_failure_error: Status = ..., results: MutableSequence[MutateAdGroupCriterionResult] = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["partial_failure_error", "results"]) -> bool: ...
class MutateAdGroupCriterionResult(proto.Message):
    resource_name: str
    ad_group_criterion: AdGroupCriterion
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, resource_name: str = ..., ad_group_criterion: AdGroupCriterion = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["resource_name", "ad_group_criterion"]) -> bool: ...
