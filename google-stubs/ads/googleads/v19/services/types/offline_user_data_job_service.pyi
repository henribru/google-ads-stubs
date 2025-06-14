from google.ads.googleads.v19.common.types.offline_user_data import UserData
from google.ads.googleads.v19.common.types.offline_user_data import UserData
from google.ads.googleads.v19.resources.types.offline_user_data_job import OfflineUserDataJob
from google.rpc.status_pb2 import Status
from google.rpc.status_pb2 import Status
from collections.abc import MutableSequence
import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class AddOfflineUserDataJobOperationsRequest(proto.Message):
    resource_name: str
    enable_partial_failure: bool
    enable_warnings: bool
    operations: MutableSequence[OfflineUserDataJobOperation]
    validate_only: bool
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., resource_name: str = ..., enable_partial_failure: bool = ..., enable_warnings: bool = ..., operations: MutableSequence[OfflineUserDataJobOperation] = ..., validate_only: bool = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["resource_name", "enable_partial_failure", "enable_warnings", "operations", "validate_only"]) -> bool: ...
class AddOfflineUserDataJobOperationsResponse(proto.Message):
    partial_failure_error: Status
    warning: Status
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., partial_failure_error: Status = ..., warning: Status = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["partial_failure_error", "warning"]) -> bool: ...
class CreateOfflineUserDataJobRequest(proto.Message):
    customer_id: str
    job: OfflineUserDataJob
    validate_only: bool
    enable_match_rate_range_preview: bool
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., customer_id: str = ..., job: OfflineUserDataJob = ..., validate_only: bool = ..., enable_match_rate_range_preview: bool = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["customer_id", "job", "validate_only", "enable_match_rate_range_preview"]) -> bool: ...
class CreateOfflineUserDataJobResponse(proto.Message):
    resource_name: str
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., resource_name: str = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["resource_name"]) -> bool: ...
class OfflineUserDataJobOperation(proto.Message):
    create: UserData
    remove: UserData
    remove_all: bool
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., create: UserData = ..., remove: UserData = ..., remove_all: bool = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["create", "remove", "remove_all"]) -> bool: ...
class RunOfflineUserDataJobRequest(proto.Message):
    resource_name: str
    validate_only: bool
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., resource_name: str = ..., validate_only: bool = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["resource_name", "validate_only"]) -> bool: ...
