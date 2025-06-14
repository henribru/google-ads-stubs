import proto
from _typeshed import Incomplete
from google.ads.googleads.v19.resources.types import keyword_plan_ad_group_keyword
from google.protobuf import field_mask_pb2
from google.rpc import status_pb2
from typing import MutableSequence

__protobuf__: Incomplete

class MutateKeywordPlanAdGroupKeywordsRequest(proto.Message):
    customer_id: str
    operations: MutableSequence['KeywordPlanAdGroupKeywordOperation']
    partial_failure: bool
    validate_only: bool

class KeywordPlanAdGroupKeywordOperation(proto.Message):
    update_mask: field_mask_pb2.FieldMask
    create: keyword_plan_ad_group_keyword.KeywordPlanAdGroupKeyword
    update: keyword_plan_ad_group_keyword.KeywordPlanAdGroupKeyword
    remove: str

class MutateKeywordPlanAdGroupKeywordsResponse(proto.Message):
    partial_failure_error: status_pb2.Status
    results: MutableSequence['MutateKeywordPlanAdGroupKeywordResult']

class MutateKeywordPlanAdGroupKeywordResult(proto.Message):
    resource_name: str
