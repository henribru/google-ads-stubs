import proto
from _typeshed import Incomplete
from google.ads.googleads.v19.common.types import policy
from google.ads.googleads.v19.enums.types import response_content_type as gage_response_content_type
from google.ads.googleads.v19.resources.types import ad_group_criterion as gagr_ad_group_criterion
from google.protobuf import field_mask_pb2
from google.rpc import status_pb2
from typing import MutableSequence

__protobuf__: Incomplete

class MutateAdGroupCriteriaRequest(proto.Message):
    customer_id: str
    operations: MutableSequence['AdGroupCriterionOperation']
    partial_failure: bool
    validate_only: bool
    response_content_type: gage_response_content_type.ResponseContentTypeEnum.ResponseContentType

class AdGroupCriterionOperation(proto.Message):
    update_mask: field_mask_pb2.FieldMask
    exempt_policy_violation_keys: MutableSequence[policy.PolicyViolationKey]
    create: gagr_ad_group_criterion.AdGroupCriterion
    update: gagr_ad_group_criterion.AdGroupCriterion
    remove: str

class MutateAdGroupCriteriaResponse(proto.Message):
    partial_failure_error: status_pb2.Status
    results: MutableSequence['MutateAdGroupCriterionResult']

class MutateAdGroupCriterionResult(proto.Message):
    resource_name: str
    ad_group_criterion: gagr_ad_group_criterion.AdGroupCriterion
