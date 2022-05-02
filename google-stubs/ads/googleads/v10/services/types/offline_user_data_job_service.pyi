import proto
from _typeshed import Incomplete
from google.rpc import status_pb2 as status_pb2

from google.ads.googleads.v10.common.types import offline_user_data as offline_user_data
from google.ads.googleads.v10.resources.types import (
    offline_user_data_job as offline_user_data_job,
)

__protobuf__: Incomplete

class CreateOfflineUserDataJobRequest(proto.Message):
    customer_id: Incomplete
    job: Incomplete
    validate_only: Incomplete
    enable_match_rate_range_preview: Incomplete

class CreateOfflineUserDataJobResponse(proto.Message):
    resource_name: Incomplete

class RunOfflineUserDataJobRequest(proto.Message):
    resource_name: Incomplete
    validate_only: Incomplete

class AddOfflineUserDataJobOperationsRequest(proto.Message):
    resource_name: Incomplete
    enable_partial_failure: Incomplete
    enable_warnings: Incomplete
    operations: Incomplete
    validate_only: Incomplete

class OfflineUserDataJobOperation(proto.Message):
    create: Incomplete
    remove: Incomplete
    remove_all: Incomplete

class AddOfflineUserDataJobOperationsResponse(proto.Message):
    partial_failure_error: Incomplete
    warning: Incomplete
