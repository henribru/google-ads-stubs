import proto
from _typeshed import Incomplete

from google.ads.googleads.v10.enums.types import batch_job_status as batch_job_status

__protobuf__: Incomplete

class BatchJob(proto.Message):
    class BatchJobMetadata(proto.Message):
        creation_date_time: Incomplete
        start_date_time: Incomplete
        completion_date_time: Incomplete
        estimated_completion_ratio: Incomplete
        operation_count: Incomplete
        executed_operation_count: Incomplete
    resource_name: Incomplete
    id: Incomplete
    next_add_sequence_token: Incomplete
    metadata: Incomplete
    status: Incomplete
    long_running_operation: Incomplete
