import proto
from _typeshed import Incomplete
from google.ads.googleads.v19.enums.types import response_content_type as gage_response_content_type
from google.ads.googleads.v19.resources.types import conversion_value_rule as gagr_conversion_value_rule
from google.protobuf import field_mask_pb2
from google.rpc import status_pb2
from typing import MutableSequence

__protobuf__: Incomplete

class MutateConversionValueRulesRequest(proto.Message):
    customer_id: str
    operations: MutableSequence['ConversionValueRuleOperation']
    partial_failure: bool
    validate_only: bool
    response_content_type: gage_response_content_type.ResponseContentTypeEnum.ResponseContentType

class ConversionValueRuleOperation(proto.Message):
    update_mask: field_mask_pb2.FieldMask
    create: gagr_conversion_value_rule.ConversionValueRule
    update: gagr_conversion_value_rule.ConversionValueRule
    remove: str

class MutateConversionValueRulesResponse(proto.Message):
    results: MutableSequence['MutateConversionValueRuleResult']
    partial_failure_error: status_pb2.Status

class MutateConversionValueRuleResult(proto.Message):
    resource_name: str
    conversion_value_rule: gagr_conversion_value_rule.ConversionValueRule
