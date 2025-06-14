import proto
from _typeshed import Incomplete
from google.ads.googleads.v18.enums.types import response_content_type as gage_response_content_type
from google.ads.googleads.v18.resources.types import label as gagr_label
from google.protobuf import field_mask_pb2
from google.rpc import status_pb2
from typing import MutableSequence

__protobuf__: Incomplete

class MutateLabelsRequest(proto.Message):
    customer_id: str
    operations: MutableSequence['LabelOperation']
    partial_failure: bool
    validate_only: bool
    response_content_type: gage_response_content_type.ResponseContentTypeEnum.ResponseContentType

class LabelOperation(proto.Message):
    update_mask: field_mask_pb2.FieldMask
    create: gagr_label.Label
    update: gagr_label.Label
    remove: str

class MutateLabelsResponse(proto.Message):
    partial_failure_error: status_pb2.Status
    results: MutableSequence['MutateLabelResult']

class MutateLabelResult(proto.Message):
    resource_name: str
    label: gagr_label.Label
