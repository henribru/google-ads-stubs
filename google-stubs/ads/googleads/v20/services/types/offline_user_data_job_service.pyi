import proto
from _typeshed import Incomplete
from google.ads.googleads.v20.common.types import offline_user_data
from google.ads.googleads.v20.resources.types import offline_user_data_job
from google.rpc import status_pb2
from typing import MutableSequence

__protobuf__: Incomplete

class CreateOfflineUserDataJobRequest(proto.Message):
    customer_id: str
    job: offline_user_data_job.OfflineUserDataJob
    validate_only: bool
    enable_match_rate_range_preview: bool

class CreateOfflineUserDataJobResponse(proto.Message):
    resource_name: str

class RunOfflineUserDataJobRequest(proto.Message):
    resource_name: str
    validate_only: bool

class AddOfflineUserDataJobOperationsRequest(proto.Message):
    resource_name: str
    enable_partial_failure: bool
    enable_warnings: bool
    operations: MutableSequence['OfflineUserDataJobOperation']
    validate_only: bool

class OfflineUserDataJobOperation(proto.Message):
    create: offline_user_data.UserData
    remove: offline_user_data.UserData
    remove_all: bool

class AddOfflineUserDataJobOperationsResponse(proto.Message):
    partial_failure_error: status_pb2.Status
    warning: status_pb2.Status
