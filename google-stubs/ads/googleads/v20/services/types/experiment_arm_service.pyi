import proto
from _typeshed import Incomplete
from google.ads.googleads.v20.enums.types import response_content_type as gage_response_content_type
from google.ads.googleads.v20.resources.types import experiment_arm as gagr_experiment_arm
from google.protobuf import field_mask_pb2
from google.rpc import status_pb2
from typing import MutableSequence

__protobuf__: Incomplete

class MutateExperimentArmsRequest(proto.Message):
    customer_id: str
    operations: MutableSequence['ExperimentArmOperation']
    partial_failure: bool
    validate_only: bool
    response_content_type: gage_response_content_type.ResponseContentTypeEnum.ResponseContentType

class ExperimentArmOperation(proto.Message):
    update_mask: field_mask_pb2.FieldMask
    create: gagr_experiment_arm.ExperimentArm
    update: gagr_experiment_arm.ExperimentArm
    remove: str

class MutateExperimentArmsResponse(proto.Message):
    partial_failure_error: status_pb2.Status
    results: MutableSequence['MutateExperimentArmResult']

class MutateExperimentArmResult(proto.Message):
    resource_name: str
    experiment_arm: gagr_experiment_arm.ExperimentArm
