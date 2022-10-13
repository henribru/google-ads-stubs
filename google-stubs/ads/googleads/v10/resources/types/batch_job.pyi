from typing import Any

import proto

from google.ads.googleads.v10.enums.types.batch_job_status import BatchJobStatusEnum

class BatchJob(proto.Message):
    class BatchJobMetadata(proto.Message):
        creation_date_time: str
        start_date_time: str
        completion_date_time: str
        estimated_completion_ratio: float
        operation_count: int
        executed_operation_count: int
        def __init__(
            self,
            mapping: Any | None = ...,
            *,
            ignore_unknown_fields: bool = ...,
            creation_date_time: str = ...,
            start_date_time: str = ...,
            completion_date_time: str = ...,
            estimated_completion_ratio: float = ...,
            operation_count: int = ...,
            executed_operation_count: int = ...
        ) -> None: ...
    resource_name: str
    id: int
    next_add_sequence_token: str
    metadata: BatchJob.BatchJobMetadata
    status: BatchJobStatusEnum.BatchJobStatus
    long_running_operation: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        id: int = ...,
        next_add_sequence_token: str = ...,
        metadata: BatchJob.BatchJobMetadata = ...,
        status: BatchJobStatusEnum.BatchJobStatus = ...,
        long_running_operation: str = ...
    ) -> None: ...
