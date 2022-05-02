import proto
from _typeshed import Incomplete
from google.rpc import status_pb2 as status_pb2

__protobuf__: Incomplete

class MutateMediaFilesRequest(proto.Message):
    customer_id: Incomplete
    operations: Incomplete
    partial_failure: Incomplete
    validate_only: Incomplete
    response_content_type: Incomplete

class MediaFileOperation(proto.Message):
    create: Incomplete

class MutateMediaFilesResponse(proto.Message):
    partial_failure_error: Incomplete
    results: Incomplete

class MutateMediaFileResult(proto.Message):
    resource_name: Incomplete
    media_file: Incomplete
