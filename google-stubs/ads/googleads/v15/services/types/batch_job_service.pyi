from collections.abc import Mapping, MutableSequence
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from google.rpc.status_pb2 import Status
from typing_extensions import Literal

from google.ads.googleads.v15.enums.types.response_content_type import (
    ResponseContentTypeEnum,
)
from google.ads.googleads.v15.resources.types.batch_job import BatchJob
from google.ads.googleads.v15.services.types.google_ads_service import (
    MutateOperation,
    MutateOperationResponse,
)

_M = TypeVar("_M")

class AddBatchJobOperationsRequest(proto.Message):
    resource_name: str
    sequence_token: str
    mutate_operations: MutableSequence[MutateOperation]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        sequence_token: str = ...,
        mutate_operations: MutableSequence[MutateOperation] = ...
    ) -> None: ...
    def __contains__(self, key: Literal["resource_name", "sequence_token", "mutate_operations"]) -> bool: ...  # type: ignore[override]

class AddBatchJobOperationsResponse(proto.Message):
    total_operations: int
    next_sequence_token: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        total_operations: int = ...,
        next_sequence_token: str = ...
    ) -> None: ...
    def __contains__(self, key: Literal["total_operations", "next_sequence_token"]) -> bool: ...  # type: ignore[override]

class BatchJobOperation(proto.Message):
    create: BatchJob
    remove: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        create: BatchJob = ...,
        remove: str = ...
    ) -> None: ...
    def __contains__(self, key: Literal["create", "remove"]) -> bool: ...  # type: ignore[override]

class BatchJobResult(proto.Message):
    operation_index: int
    mutate_operation_response: MutateOperationResponse
    status: Status
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        operation_index: int = ...,
        mutate_operation_response: MutateOperationResponse = ...,
        status: Status = ...
    ) -> None: ...
    def __contains__(self, key: Literal["operation_index", "mutate_operation_response", "status"]) -> bool: ...  # type: ignore[override]

class ListBatchJobResultsRequest(proto.Message):
    resource_name: str
    page_token: str
    page_size: int
    response_content_type: ResponseContentTypeEnum.ResponseContentType
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        page_token: str = ...,
        page_size: int = ...,
        response_content_type: ResponseContentTypeEnum.ResponseContentType = ...
    ) -> None: ...
    def __contains__(self, key: Literal["resource_name", "page_token", "page_size", "response_content_type"]) -> bool: ...  # type: ignore[override]

class ListBatchJobResultsResponse(proto.Message):
    results: MutableSequence[BatchJobResult]
    next_page_token: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        results: MutableSequence[BatchJobResult] = ...,
        next_page_token: str = ...
    ) -> None: ...
    def __contains__(self, key: Literal["results", "next_page_token"]) -> bool: ...  # type: ignore[override]

class MutateBatchJobRequest(proto.Message):
    customer_id: str
    operation: BatchJobOperation
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        customer_id: str = ...,
        operation: BatchJobOperation = ...
    ) -> None: ...
    def __contains__(self, key: Literal["customer_id", "operation"]) -> bool: ...  # type: ignore[override]

class MutateBatchJobResponse(proto.Message):
    result: MutateBatchJobResult
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        result: MutateBatchJobResult = ...
    ) -> None: ...
    def __contains__(self, key: Literal["result"]) -> bool: ...  # type: ignore[override]

class MutateBatchJobResult(proto.Message):
    resource_name: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...
    ) -> None: ...
    def __contains__(self, key: Literal["resource_name"]) -> bool: ...  # type: ignore[override]

class RunBatchJobRequest(proto.Message):
    resource_name: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...
    ) -> None: ...
    def __contains__(self, key: Literal["resource_name"]) -> bool: ...  # type: ignore[override]
