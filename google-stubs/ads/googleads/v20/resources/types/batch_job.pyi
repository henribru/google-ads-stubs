import proto
from _typeshed import Incomplete
from google.ads.googleads.v20.enums.types import batch_job_status

__protobuf__: Incomplete

class BatchJob(proto.Message):
    class BatchJobMetadata(proto.Message):
        creation_date_time: str
        start_date_time: str
        completion_date_time: str
        estimated_completion_ratio: float
        operation_count: int
        executed_operation_count: int
        execution_limit_seconds: int
    resource_name: str
    id: int
    next_add_sequence_token: str
    metadata: BatchJobMetadata
    status: batch_job_status.BatchJobStatusEnum.BatchJobStatus
    long_running_operation: str
