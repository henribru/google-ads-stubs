import proto
from _typeshed import Incomplete
from google.ads.googleads.v20.resources.types import keyword_plan
from google.protobuf import field_mask_pb2
from google.rpc import status_pb2
from typing import MutableSequence

__protobuf__: Incomplete

class MutateKeywordPlansRequest(proto.Message):
    customer_id: str
    operations: MutableSequence['KeywordPlanOperation']
    partial_failure: bool
    validate_only: bool

class KeywordPlanOperation(proto.Message):
    update_mask: field_mask_pb2.FieldMask
    create: keyword_plan.KeywordPlan
    update: keyword_plan.KeywordPlan
    remove: str

class MutateKeywordPlansResponse(proto.Message):
    partial_failure_error: status_pb2.Status
    results: MutableSequence['MutateKeywordPlansResult']

class MutateKeywordPlansResult(proto.Message):
    resource_name: str
