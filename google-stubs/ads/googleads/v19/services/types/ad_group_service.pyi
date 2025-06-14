import proto
from _typeshed import Incomplete
from google.ads.googleads.v19.enums.types import response_content_type as gage_response_content_type
from google.ads.googleads.v19.resources.types import ad_group as gagr_ad_group
from google.protobuf import field_mask_pb2
from google.rpc import status_pb2
from typing import MutableSequence

__protobuf__: Incomplete

class MutateAdGroupsRequest(proto.Message):
    customer_id: str
    operations: MutableSequence['AdGroupOperation']
    partial_failure: bool
    validate_only: bool
    response_content_type: gage_response_content_type.ResponseContentTypeEnum.ResponseContentType

class AdGroupOperation(proto.Message):
    update_mask: field_mask_pb2.FieldMask
    create: gagr_ad_group.AdGroup
    update: gagr_ad_group.AdGroup
    remove: str

class MutateAdGroupsResponse(proto.Message):
    partial_failure_error: status_pb2.Status
    results: MutableSequence['MutateAdGroupResult']

class MutateAdGroupResult(proto.Message):
    resource_name: str
    ad_group: gagr_ad_group.AdGroup
