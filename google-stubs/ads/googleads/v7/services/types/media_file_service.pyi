from typing import Any

import proto

__protobuf__: Any

class GetMediaFileRequest(proto.Message):
    resource_name: Any

class MutateMediaFilesRequest(proto.Message):
    customer_id: Any
    operations: Any
    partial_failure: Any
    validate_only: Any
    response_content_type: Any

class MediaFileOperation(proto.Message):
    create: Any

class MutateMediaFilesResponse(proto.Message):
    partial_failure_error: Any
    results: Any

class MutateMediaFileResult(proto.Message):
    resource_name: Any
    media_file: Any
