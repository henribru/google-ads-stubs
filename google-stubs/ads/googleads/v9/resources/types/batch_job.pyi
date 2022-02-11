from typing import Any

import proto

from google.ads.googleads.v9.enums.types import batch_job_status as batch_job_status

__protobuf__: Any

class BatchJob(proto.Message):
    class BatchJobMetadata(proto.Message):
        creation_date_time: Any
        start_date_time: Any
        completion_date_time: Any
        estimated_completion_ratio: Any
        operation_count: Any
        executed_operation_count: Any
    resource_name: Any
    id: Any
    next_add_sequence_token: Any
    metadata: Any
    status: Any
    long_running_operation: Any
