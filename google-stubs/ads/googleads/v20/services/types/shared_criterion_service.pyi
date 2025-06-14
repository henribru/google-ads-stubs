import proto
from _typeshed import Incomplete
from google.ads.googleads.v20.enums.types import response_content_type as gage_response_content_type
from google.ads.googleads.v20.resources.types import shared_criterion as gagr_shared_criterion
from google.rpc import status_pb2
from typing import MutableSequence

__protobuf__: Incomplete

class MutateSharedCriteriaRequest(proto.Message):
    customer_id: str
    operations: MutableSequence['SharedCriterionOperation']
    partial_failure: bool
    validate_only: bool
    response_content_type: gage_response_content_type.ResponseContentTypeEnum.ResponseContentType

class SharedCriterionOperation(proto.Message):
    create: gagr_shared_criterion.SharedCriterion
    remove: str

class MutateSharedCriteriaResponse(proto.Message):
    partial_failure_error: status_pb2.Status
    results: MutableSequence['MutateSharedCriterionResult']

class MutateSharedCriterionResult(proto.Message):
    resource_name: str
    shared_criterion: gagr_shared_criterion.SharedCriterion
