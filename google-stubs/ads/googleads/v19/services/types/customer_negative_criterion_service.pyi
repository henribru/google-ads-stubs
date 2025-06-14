import proto
from _typeshed import Incomplete
from google.ads.googleads.v19.enums.types import response_content_type as gage_response_content_type
from google.ads.googleads.v19.resources.types import customer_negative_criterion as gagr_customer_negative_criterion
from google.rpc import status_pb2
from typing import MutableSequence

__protobuf__: Incomplete

class MutateCustomerNegativeCriteriaRequest(proto.Message):
    customer_id: str
    operations: MutableSequence['CustomerNegativeCriterionOperation']
    partial_failure: bool
    validate_only: bool
    response_content_type: gage_response_content_type.ResponseContentTypeEnum.ResponseContentType

class CustomerNegativeCriterionOperation(proto.Message):
    create: gagr_customer_negative_criterion.CustomerNegativeCriterion
    remove: str

class MutateCustomerNegativeCriteriaResponse(proto.Message):
    partial_failure_error: status_pb2.Status
    results: MutableSequence['MutateCustomerNegativeCriteriaResult']

class MutateCustomerNegativeCriteriaResult(proto.Message):
    resource_name: str
    customer_negative_criterion: gagr_customer_negative_criterion.CustomerNegativeCriterion
