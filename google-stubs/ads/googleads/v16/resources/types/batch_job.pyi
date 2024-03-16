from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v16.enums.types.batch_job_status import BatchJobStatusEnum

_M = TypeVar("_M")

class BatchJob(proto.Message):
    class BatchJobMetadata(proto.Message):
        creation_date_time: str
        start_date_time: str
        completion_date_time: str
        estimated_completion_ratio: float
        operation_count: int
        executed_operation_count: int
        execution_limit_seconds: int
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
            creation_date_time: str = ...,
            start_date_time: str = ...,
            completion_date_time: str = ...,
            estimated_completion_ratio: float = ...,
            operation_count: int = ...,
            executed_operation_count: int = ...,
            execution_limit_seconds: int = ...,
        ) -> None: ...
        def __contains__(  # type: ignore[override]
            self,
            key: Literal[
                "creation_date_time",
                "start_date_time",
                "completion_date_time",
                "estimated_completion_ratio",
                "operation_count",
                "executed_operation_count",
                "execution_limit_seconds",
            ],
        ) -> bool: ...

    resource_name: str
    id: int
    next_add_sequence_token: str
    metadata: BatchJob.BatchJobMetadata
    status: BatchJobStatusEnum.BatchJobStatus
    long_running_operation: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        id: int = ...,
        next_add_sequence_token: str = ...,
        metadata: BatchJob.BatchJobMetadata = ...,
        status: BatchJobStatusEnum.BatchJobStatus = ...,
        long_running_operation: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "resource_name",
            "id",
            "next_add_sequence_token",
            "metadata",
            "status",
            "long_running_operation",
        ],
    ) -> bool: ...
