import proto
from _typeshed import Incomplete
from google.ads.googleads.v19.enums.types import response_content_type as gage_response_content_type
from google.ads.googleads.v19.resources.types import batch_job
from google.ads.googleads.v19.services.types import google_ads_service
from google.rpc import status_pb2
from typing import MutableSequence

__protobuf__: Incomplete

class MutateBatchJobRequest(proto.Message):
    customer_id: str
    operation: BatchJobOperation

class BatchJobOperation(proto.Message):
    create: batch_job.BatchJob
    remove: str

class MutateBatchJobResponse(proto.Message):
    result: MutateBatchJobResult

class MutateBatchJobResult(proto.Message):
    resource_name: str

class RunBatchJobRequest(proto.Message):
    resource_name: str

class AddBatchJobOperationsRequest(proto.Message):
    resource_name: str
    sequence_token: str
    mutate_operations: MutableSequence[google_ads_service.MutateOperation]

class AddBatchJobOperationsResponse(proto.Message):
    total_operations: int
    next_sequence_token: str

class ListBatchJobResultsRequest(proto.Message):
    resource_name: str
    page_token: str
    page_size: int
    response_content_type: gage_response_content_type.ResponseContentTypeEnum.ResponseContentType

class ListBatchJobResultsResponse(proto.Message):
    @property
    def raw_page(self): ...
    results: MutableSequence['BatchJobResult']
    next_page_token: str

class BatchJobResult(proto.Message):
    operation_index: int
    mutate_operation_response: google_ads_service.MutateOperationResponse
    status: status_pb2.Status
