import proto
from _typeshed import Incomplete
from google.ads.googleads.v20.enums.types import response_content_type as gage_response_content_type
from google.ads.googleads.v20.resources.types import conversion_value_rule_set as gagr_conversion_value_rule_set
from google.protobuf import field_mask_pb2
from google.rpc import status_pb2
from typing import MutableSequence

__protobuf__: Incomplete

class MutateConversionValueRuleSetsRequest(proto.Message):
    customer_id: str
    operations: MutableSequence['ConversionValueRuleSetOperation']
    partial_failure: bool
    validate_only: bool
    response_content_type: gage_response_content_type.ResponseContentTypeEnum.ResponseContentType

class ConversionValueRuleSetOperation(proto.Message):
    update_mask: field_mask_pb2.FieldMask
    create: gagr_conversion_value_rule_set.ConversionValueRuleSet
    update: gagr_conversion_value_rule_set.ConversionValueRuleSet
    remove: str

class MutateConversionValueRuleSetsResponse(proto.Message):
    results: MutableSequence['MutateConversionValueRuleSetResult']
    partial_failure_error: status_pb2.Status

class MutateConversionValueRuleSetResult(proto.Message):
    resource_name: str
    conversion_value_rule_set: gagr_conversion_value_rule_set.ConversionValueRuleSet
