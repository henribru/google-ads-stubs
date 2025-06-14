import proto
from _typeshed import Incomplete
from google.ads.googleads.v18.enums.types import response_content_type as gage_response_content_type
from google.ads.googleads.v18.resources.types import ad_group_customizer as gagr_ad_group_customizer
from google.rpc import status_pb2
from typing import MutableSequence

__protobuf__: Incomplete

class MutateAdGroupCustomizersRequest(proto.Message):
    customer_id: str
    operations: MutableSequence['AdGroupCustomizerOperation']
    partial_failure: bool
    validate_only: bool
    response_content_type: gage_response_content_type.ResponseContentTypeEnum.ResponseContentType

class AdGroupCustomizerOperation(proto.Message):
    create: gagr_ad_group_customizer.AdGroupCustomizer
    remove: str

class MutateAdGroupCustomizersResponse(proto.Message):
    results: MutableSequence['MutateAdGroupCustomizerResult']
    partial_failure_error: status_pb2.Status

class MutateAdGroupCustomizerResult(proto.Message):
    resource_name: str
    ad_group_customizer: gagr_ad_group_customizer.AdGroupCustomizer
