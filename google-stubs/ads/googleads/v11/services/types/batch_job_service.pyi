import proto
from _typeshed import Incomplete
from google.rpc import status_pb2 as status_pb2

from google.ads.googleads.v11.resources.types import batch_job as batch_job
from google.ads.googleads.v11.services.types import (
    google_ads_service as google_ads_service,
)

__protobuf__: Incomplete

class MutateBatchJobRequest(proto.Message):
    customer_id: Incomplete
    operation: Incomplete

class BatchJobOperation(proto.Message):
    create: Incomplete
    remove: Incomplete

class MutateBatchJobResponse(proto.Message):
    result: Incomplete

class MutateBatchJobResult(proto.Message):
    resource_name: Incomplete

class RunBatchJobRequest(proto.Message):
    resource_name: Incomplete

class AddBatchJobOperationsRequest(proto.Message):
    resource_name: Incomplete
    sequence_token: Incomplete
    mutate_operations: Incomplete

class AddBatchJobOperationsResponse(proto.Message):
    total_operations: Incomplete
    next_sequence_token: Incomplete

class ListBatchJobResultsRequest(proto.Message):
    resource_name: Incomplete
    page_token: Incomplete
    page_size: Incomplete
    response_content_type: Incomplete

class ListBatchJobResultsResponse(proto.Message):
    @property
    def raw_page(self): ...
    results: Incomplete
    next_page_token: Incomplete

class BatchJobResult(proto.Message):
    operation_index: Incomplete
    mutate_operation_response: Incomplete
    status: Incomplete
