import proto
from _typeshed import Incomplete
from google.ads.googleads.v18.enums.types import response_content_type as gage_response_content_type
from google.ads.googleads.v18.resources.types import ad_group_criterion_customizer as gagr_ad_group_criterion_customizer
from google.rpc import status_pb2
from typing import MutableSequence

__protobuf__: Incomplete

class MutateAdGroupCriterionCustomizersRequest(proto.Message):
    customer_id: str
    operations: MutableSequence['AdGroupCriterionCustomizerOperation']
    partial_failure: bool
    validate_only: bool
    response_content_type: gage_response_content_type.ResponseContentTypeEnum.ResponseContentType

class AdGroupCriterionCustomizerOperation(proto.Message):
    create: gagr_ad_group_criterion_customizer.AdGroupCriterionCustomizer
    remove: str

class MutateAdGroupCriterionCustomizersResponse(proto.Message):
    results: MutableSequence['MutateAdGroupCriterionCustomizerResult']
    partial_failure_error: status_pb2.Status

class MutateAdGroupCriterionCustomizerResult(proto.Message):
    resource_name: str
    ad_group_criterion_customizer: gagr_ad_group_criterion_customizer.AdGroupCriterionCustomizer
