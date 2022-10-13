from typing import Any

import proto
from google.rpc.status_pb2 import Status

from google.ads.googleads.v10.enums.types.response_content_type import (
    ResponseContentTypeEnum,
)
from google.ads.googleads.v10.resources.types.batch_job import BatchJob
from google.ads.googleads.v10.services.types.google_ads_service import (
    MutateOperation,
    MutateOperationResponse,
)

class AddBatchJobOperationsRequest(proto.Message):
    resource_name: str
    sequence_token: str
    mutate_operations: list[MutateOperation]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        sequence_token: str = ...,
        mutate_operations: list[MutateOperation] = ...
    ) -> None: ...

class AddBatchJobOperationsResponse(proto.Message):
    total_operations: int
    next_sequence_token: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        total_operations: int = ...,
        next_sequence_token: str = ...
    ) -> None: ...

class BatchJobOperation(proto.Message):
    create: BatchJob
    remove: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        create: BatchJob = ...,
        remove: str = ...
    ) -> None: ...

class BatchJobResult(proto.Message):
    operation_index: int
    mutate_operation_response: MutateOperationResponse
    status: Status
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        operation_index: int = ...,
        mutate_operation_response: MutateOperationResponse = ...,
        status: Status = ...
    ) -> None: ...

class ListBatchJobResultsRequest(proto.Message):
    resource_name: str
    page_token: str
    page_size: int
    response_content_type: ResponseContentTypeEnum.ResponseContentType
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        page_token: str = ...,
        page_size: int = ...,
        response_content_type: ResponseContentTypeEnum.ResponseContentType = ...
    ) -> None: ...

class ListBatchJobResultsResponse(proto.Message):
    results: list[BatchJobResult]
    next_page_token: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        results: list[BatchJobResult] = ...,
        next_page_token: str = ...
    ) -> None: ...

class MutateBatchJobRequest(proto.Message):
    customer_id: str
    operation: BatchJobOperation
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        customer_id: str = ...,
        operation: BatchJobOperation = ...
    ) -> None: ...

class MutateBatchJobResponse(proto.Message):
    result: MutateBatchJobResult
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        result: MutateBatchJobResult = ...
    ) -> None: ...

class MutateBatchJobResult(proto.Message):
    resource_name: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...
    ) -> None: ...

class RunBatchJobRequest(proto.Message):
    resource_name: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...
    ) -> None: ...
