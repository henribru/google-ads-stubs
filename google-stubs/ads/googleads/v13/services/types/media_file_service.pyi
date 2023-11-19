from collections.abc import Mapping, MutableSequence
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from google.rpc.status_pb2 import Status
from typing_extensions import Literal

from google.ads.googleads.v13.enums.types.response_content_type import (
    ResponseContentTypeEnum,
)
from google.ads.googleads.v13.resources.types.media_file import MediaFile

_M = TypeVar("_M")

class MediaFileOperation(proto.Message):
    create: MediaFile
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        create: MediaFile = ...
    ) -> None: ...
    def __contains__(self, key: Literal["create"]) -> bool: ...  # type: ignore[override]

class MutateMediaFileResult(proto.Message):
    resource_name: str
    media_file: MediaFile
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        media_file: MediaFile = ...
    ) -> None: ...
    def __contains__(self, key: Literal["resource_name", "media_file"]) -> bool: ...  # type: ignore[override]

class MutateMediaFilesRequest(proto.Message):
    customer_id: str
    operations: MutableSequence[MediaFileOperation]
    partial_failure: bool
    validate_only: bool
    response_content_type: ResponseContentTypeEnum.ResponseContentType
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        customer_id: str = ...,
        operations: MutableSequence[MediaFileOperation] = ...,
        partial_failure: bool = ...,
        validate_only: bool = ...,
        response_content_type: ResponseContentTypeEnum.ResponseContentType = ...
    ) -> None: ...
    def __contains__(self, key: Literal["customer_id", "operations", "partial_failure", "validate_only", "response_content_type"]) -> bool: ...  # type: ignore[override]

class MutateMediaFilesResponse(proto.Message):
    partial_failure_error: Status
    results: MutableSequence[MutateMediaFileResult]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        partial_failure_error: Status = ...,
        results: MutableSequence[MutateMediaFileResult] = ...
    ) -> None: ...
    def __contains__(self, key: Literal["partial_failure_error", "results"]) -> bool: ...  # type: ignore[override]
