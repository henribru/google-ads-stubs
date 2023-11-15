from collections.abc import Mapping, MutableSequence
from typing import Any, TypeVar

import google.protobuf.message
import proto
from google.rpc.status_pb2 import Status

from google.ads.googleads.v13.common.types.offline_user_data import UserData
from google.ads.googleads.v13.resources.types.offline_user_data_job import (
    OfflineUserDataJob,
)

_M = TypeVar("_M")

class AddOfflineUserDataJobOperationsRequest(proto.Message):
    resource_name: str
    enable_partial_failure: bool
    enable_warnings: bool
    operations: MutableSequence[OfflineUserDataJobOperation]
    validate_only: bool
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        enable_partial_failure: bool = ...,
        enable_warnings: bool = ...,
        operations: MutableSequence[OfflineUserDataJobOperation] = ...,
        validate_only: bool = ...
    ) -> None: ...

class AddOfflineUserDataJobOperationsResponse(proto.Message):
    partial_failure_error: Status
    warning: Status
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        partial_failure_error: Status = ...,
        warning: Status = ...
    ) -> None: ...

class CreateOfflineUserDataJobRequest(proto.Message):
    customer_id: str
    job: OfflineUserDataJob
    validate_only: bool
    enable_match_rate_range_preview: bool
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        customer_id: str = ...,
        job: OfflineUserDataJob = ...,
        validate_only: bool = ...,
        enable_match_rate_range_preview: bool = ...
    ) -> None: ...

class CreateOfflineUserDataJobResponse(proto.Message):
    resource_name: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...
    ) -> None: ...

class OfflineUserDataJobOperation(proto.Message):
    create: UserData
    remove: UserData
    remove_all: bool
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        create: UserData = ...,
        remove: UserData = ...,
        remove_all: bool = ...
    ) -> None: ...

class RunOfflineUserDataJobRequest(proto.Message):
    resource_name: str
    validate_only: bool
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        validate_only: bool = ...
    ) -> None: ...
