from typing import Any

import proto
from google.rpc.status_pb2 import Status

from google.ads.googleads.v11.enums.types.response_content_type import (
    ResponseContentTypeEnum,
)
from google.ads.googleads.v11.resources.types.media_file import MediaFile

class MediaFileOperation(proto.Message):
    create: MediaFile
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        create: MediaFile = ...
    ) -> None: ...

class MutateMediaFileResult(proto.Message):
    resource_name: str
    media_file: MediaFile
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        media_file: MediaFile = ...
    ) -> None: ...

class MutateMediaFilesRequest(proto.Message):
    customer_id: str
    operations: list[MediaFileOperation]
    partial_failure: bool
    validate_only: bool
    response_content_type: ResponseContentTypeEnum.ResponseContentType
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        customer_id: str = ...,
        operations: list[MediaFileOperation] = ...,
        partial_failure: bool = ...,
        validate_only: bool = ...,
        response_content_type: ResponseContentTypeEnum.ResponseContentType = ...
    ) -> None: ...

class MutateMediaFilesResponse(proto.Message):
    partial_failure_error: Status
    results: list[MutateMediaFileResult]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        partial_failure_error: Status = ...,
        results: list[MutateMediaFileResult] = ...
    ) -> None: ...
