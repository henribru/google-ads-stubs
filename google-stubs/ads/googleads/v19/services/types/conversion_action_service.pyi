import proto
from _typeshed import Incomplete
from google.ads.googleads.v19.enums.types import response_content_type as gage_response_content_type
from google.ads.googleads.v19.resources.types import conversion_action as gagr_conversion_action
from google.protobuf import field_mask_pb2
from google.rpc import status_pb2
from typing import MutableSequence

__protobuf__: Incomplete

class MutateConversionActionsRequest(proto.Message):
    customer_id: str
    operations: MutableSequence['ConversionActionOperation']
    partial_failure: bool
    validate_only: bool
    response_content_type: gage_response_content_type.ResponseContentTypeEnum.ResponseContentType

class ConversionActionOperation(proto.Message):
    update_mask: field_mask_pb2.FieldMask
    create: gagr_conversion_action.ConversionAction
    update: gagr_conversion_action.ConversionAction
    remove: str

class MutateConversionActionsResponse(proto.Message):
    partial_failure_error: status_pb2.Status
    results: MutableSequence['MutateConversionActionResult']

class MutateConversionActionResult(proto.Message):
    resource_name: str
    conversion_action: gagr_conversion_action.ConversionAction
