import proto
from _typeshed import Incomplete
from google.ads.googleads.v20.enums.types import response_content_type as gage_response_content_type
from google.ads.googleads.v20.resources.types import ad_group_bid_modifier as gagr_ad_group_bid_modifier
from google.protobuf import field_mask_pb2
from google.rpc import status_pb2
from typing import MutableSequence

__protobuf__: Incomplete

class MutateAdGroupBidModifiersRequest(proto.Message):
    customer_id: str
    operations: MutableSequence['AdGroupBidModifierOperation']
    partial_failure: bool
    validate_only: bool
    response_content_type: gage_response_content_type.ResponseContentTypeEnum.ResponseContentType

class AdGroupBidModifierOperation(proto.Message):
    update_mask: field_mask_pb2.FieldMask
    create: gagr_ad_group_bid_modifier.AdGroupBidModifier
    update: gagr_ad_group_bid_modifier.AdGroupBidModifier
    remove: str

class MutateAdGroupBidModifiersResponse(proto.Message):
    partial_failure_error: status_pb2.Status
    results: MutableSequence['MutateAdGroupBidModifierResult']

class MutateAdGroupBidModifierResult(proto.Message):
    resource_name: str
    ad_group_bid_modifier: gagr_ad_group_bid_modifier.AdGroupBidModifier
