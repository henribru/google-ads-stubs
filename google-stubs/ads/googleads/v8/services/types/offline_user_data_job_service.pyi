from typing import Any

import proto
from google.rpc import status_pb2 as status_pb2

from google.ads.googleads.v8.common.types import offline_user_data as offline_user_data
from google.ads.googleads.v8.resources.types import (
    offline_user_data_job as offline_user_data_job,
)

__protobuf__: Any

class CreateOfflineUserDataJobRequest(proto.Message):
    customer_id: Any
    job: Any
    validate_only: Any

class CreateOfflineUserDataJobResponse(proto.Message):
    resource_name: Any

class GetOfflineUserDataJobRequest(proto.Message):
    resource_name: Any

class RunOfflineUserDataJobRequest(proto.Message):
    resource_name: Any
    validate_only: Any

class AddOfflineUserDataJobOperationsRequest(proto.Message):
    resource_name: Any
    enable_partial_failure: Any
    operations: Any
    validate_only: Any

class OfflineUserDataJobOperation(proto.Message):
    create: Any
    remove: Any
    remove_all: Any

class AddOfflineUserDataJobOperationsResponse(proto.Message):
    partial_failure_error: Any
