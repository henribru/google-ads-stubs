import proto
from _typeshed import Incomplete
from google.ads.googleads.v19.enums.types import response_content_type as gage_response_content_type
from google.ads.googleads.v19.resources.types import customer_customizer as gagr_customer_customizer
from google.rpc import status_pb2
from typing import MutableSequence

__protobuf__: Incomplete

class MutateCustomerCustomizersRequest(proto.Message):
    customer_id: str
    operations: MutableSequence['CustomerCustomizerOperation']
    partial_failure: bool
    validate_only: bool
    response_content_type: gage_response_content_type.ResponseContentTypeEnum.ResponseContentType

class CustomerCustomizerOperation(proto.Message):
    create: gagr_customer_customizer.CustomerCustomizer
    remove: str

class MutateCustomerCustomizersResponse(proto.Message):
    results: MutableSequence['MutateCustomerCustomizerResult']
    partial_failure_error: status_pb2.Status

class MutateCustomerCustomizerResult(proto.Message):
    resource_name: str
    customer_customizer: gagr_customer_customizer.CustomerCustomizer
