import proto
from _typeshed import Incomplete
from google.ads.googleads.v18.enums.types import response_content_type as gage_response_content_type
from google.ads.googleads.v18.resources.types import extension_feed_item as gagr_extension_feed_item
from google.protobuf import field_mask_pb2
from google.rpc import status_pb2
from typing import MutableSequence

__protobuf__: Incomplete

class MutateExtensionFeedItemsRequest(proto.Message):
    customer_id: str
    operations: MutableSequence['ExtensionFeedItemOperation']
    partial_failure: bool
    validate_only: bool
    response_content_type: gage_response_content_type.ResponseContentTypeEnum.ResponseContentType

class ExtensionFeedItemOperation(proto.Message):
    update_mask: field_mask_pb2.FieldMask
    create: gagr_extension_feed_item.ExtensionFeedItem
    update: gagr_extension_feed_item.ExtensionFeedItem
    remove: str

class MutateExtensionFeedItemsResponse(proto.Message):
    partial_failure_error: status_pb2.Status
    results: MutableSequence['MutateExtensionFeedItemResult']

class MutateExtensionFeedItemResult(proto.Message):
    resource_name: str
    extension_feed_item: gagr_extension_feed_item.ExtensionFeedItem
