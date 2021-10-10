from typing import Any

import proto
from google.rpc import status_pb2 as status_pb2

from google.ads.googleads.v8.resources.types import batch_job as batch_job
from google.ads.googleads.v8.services.types import (
    google_ads_service as google_ads_service,
)

__protobuf__: Any

class MutateBatchJobRequest(proto.Message):
    customer_id: Any
    operation: Any

class BatchJobOperation(proto.Message):
    create: Any

class MutateBatchJobResponse(proto.Message):
    result: Any

class MutateBatchJobResult(proto.Message):
    resource_name: Any

class GetBatchJobRequest(proto.Message):
    resource_name: Any

class RunBatchJobRequest(proto.Message):
    resource_name: Any

class AddBatchJobOperationsRequest(proto.Message):
    resource_name: Any
    sequence_token: Any
    mutate_operations: Any

class AddBatchJobOperationsResponse(proto.Message):
    total_operations: Any
    next_sequence_token: Any

class ListBatchJobResultsRequest(proto.Message):
    resource_name: Any
    page_token: Any
    page_size: Any
    response_content_type: Any

class ListBatchJobResultsResponse(proto.Message):
    @property
    def raw_page(self): ...
    results: Any
    next_page_token: Any

class BatchJobResult(proto.Message):
    operation_index: Any
    mutate_operation_response: Any
    status: Any
