import proto
from _typeshed import Incomplete
from google.ads.googleads.v20.enums.types import response_content_type as gage_response_content_type
from google.ads.googleads.v20.resources.types import customizer_attribute as gagr_customizer_attribute
from google.protobuf import field_mask_pb2
from google.rpc import status_pb2
from typing import MutableSequence

__protobuf__: Incomplete

class MutateCustomizerAttributesRequest(proto.Message):
    customer_id: str
    operations: MutableSequence['CustomizerAttributeOperation']
    partial_failure: bool
    validate_only: bool
    response_content_type: gage_response_content_type.ResponseContentTypeEnum.ResponseContentType

class CustomizerAttributeOperation(proto.Message):
    update_mask: field_mask_pb2.FieldMask
    create: gagr_customizer_attribute.CustomizerAttribute
    remove: str

class MutateCustomizerAttributesResponse(proto.Message):
    results: MutableSequence['MutateCustomizerAttributeResult']
    partial_failure_error: status_pb2.Status

class MutateCustomizerAttributeResult(proto.Message):
    resource_name: str
    customizer_attribute: gagr_customizer_attribute.CustomizerAttribute
