import proto
from _typeshed import Incomplete
from google.ads.googleads.v18.enums.types import response_content_type as gage_response_content_type
from google.ads.googleads.v18.resources.types import customer_feed as gagr_customer_feed
from google.protobuf import field_mask_pb2
from google.rpc import status_pb2
from typing import MutableSequence

__protobuf__: Incomplete

class MutateCustomerFeedsRequest(proto.Message):
    customer_id: str
    operations: MutableSequence['CustomerFeedOperation']
    partial_failure: bool
    validate_only: bool
    response_content_type: gage_response_content_type.ResponseContentTypeEnum.ResponseContentType

class CustomerFeedOperation(proto.Message):
    update_mask: field_mask_pb2.FieldMask
    create: gagr_customer_feed.CustomerFeed
    update: gagr_customer_feed.CustomerFeed
    remove: str

class MutateCustomerFeedsResponse(proto.Message):
    partial_failure_error: status_pb2.Status
    results: MutableSequence['MutateCustomerFeedResult']

class MutateCustomerFeedResult(proto.Message):
    resource_name: str
    customer_feed: gagr_customer_feed.CustomerFeed
