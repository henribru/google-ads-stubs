import proto
from _typeshed import Incomplete
from google.ads.googleads.v19.enums.types import response_content_type as gage_response_content_type
from google.ads.googleads.v19.resources.types import conversion_custom_variable as gagr_conversion_custom_variable
from google.protobuf import field_mask_pb2
from google.rpc import status_pb2
from typing import MutableSequence

__protobuf__: Incomplete

class MutateConversionCustomVariablesRequest(proto.Message):
    customer_id: str
    operations: MutableSequence['ConversionCustomVariableOperation']
    partial_failure: bool
    validate_only: bool
    response_content_type: gage_response_content_type.ResponseContentTypeEnum.ResponseContentType

class ConversionCustomVariableOperation(proto.Message):
    update_mask: field_mask_pb2.FieldMask
    create: gagr_conversion_custom_variable.ConversionCustomVariable
    update: gagr_conversion_custom_variable.ConversionCustomVariable

class MutateConversionCustomVariablesResponse(proto.Message):
    partial_failure_error: status_pb2.Status
    results: MutableSequence['MutateConversionCustomVariableResult']

class MutateConversionCustomVariableResult(proto.Message):
    resource_name: str
    conversion_custom_variable: gagr_conversion_custom_variable.ConversionCustomVariable
