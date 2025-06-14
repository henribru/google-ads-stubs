import proto
from _typeshed import Incomplete
from google.ads.googleads.v19.resources.types import keyword_plan_ad_group
from google.protobuf import field_mask_pb2
from google.rpc import status_pb2
from typing import MutableSequence

__protobuf__: Incomplete

class MutateKeywordPlanAdGroupsRequest(proto.Message):
    customer_id: str
    operations: MutableSequence['KeywordPlanAdGroupOperation']
    partial_failure: bool
    validate_only: bool

class KeywordPlanAdGroupOperation(proto.Message):
    update_mask: field_mask_pb2.FieldMask
    create: keyword_plan_ad_group.KeywordPlanAdGroup
    update: keyword_plan_ad_group.KeywordPlanAdGroup
    remove: str

class MutateKeywordPlanAdGroupsResponse(proto.Message):
    partial_failure_error: status_pb2.Status
    results: MutableSequence['MutateKeywordPlanAdGroupResult']

class MutateKeywordPlanAdGroupResult(proto.Message):
    resource_name: str
