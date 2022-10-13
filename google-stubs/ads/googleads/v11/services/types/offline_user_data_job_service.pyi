from typing import Any

import proto
from google.rpc.status_pb2 import Status

from google.ads.googleads.v11.common.types.offline_user_data import UserData
from google.ads.googleads.v11.resources.types.offline_user_data_job import (
    OfflineUserDataJob,
)

class AddOfflineUserDataJobOperationsRequest(proto.Message):
    resource_name: str
    enable_partial_failure: bool
    enable_warnings: bool
    operations: list[OfflineUserDataJobOperation]
    validate_only: bool
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        enable_partial_failure: bool = ...,
        enable_warnings: bool = ...,
        operations: list[OfflineUserDataJobOperation] = ...,
        validate_only: bool = ...
    ) -> None: ...

class AddOfflineUserDataJobOperationsResponse(proto.Message):
    partial_failure_error: Status
    warning: Status
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        partial_failure_error: Status = ...,
        warning: Status = ...
    ) -> None: ...

class CreateOfflineUserDataJobRequest(proto.Message):
    customer_id: str
    job: OfflineUserDataJob
    validate_only: bool
    enable_match_rate_range_preview: bool
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        customer_id: str = ...,
        job: OfflineUserDataJob = ...,
        validate_only: bool = ...,
        enable_match_rate_range_preview: bool = ...
    ) -> None: ...

class CreateOfflineUserDataJobResponse(proto.Message):
    resource_name: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...
    ) -> None: ...

class OfflineUserDataJobOperation(proto.Message):
    create: UserData
    remove: UserData
    remove_all: bool
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        create: UserData = ...,
        remove: UserData = ...,
        remove_all: bool = ...
    ) -> None: ...

class RunOfflineUserDataJobRequest(proto.Message):
    resource_name: str
    validate_only: bool
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        validate_only: bool = ...
    ) -> None: ...
