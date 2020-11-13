# @generated by mypy-protobuf.  Do not edit manually!
import sys
from typing import (
    Iterable as typing___Iterable,
    Optional as typing___Optional,
    Text as typing___Text,
)

from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    FileDescriptor as google___protobuf___descriptor___FileDescriptor,
)
from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
)
from google.protobuf.message import Message as google___protobuf___message___Message
from google.rpc.status_pb2 import Status as google___rpc___status_pb2___Status
from typing_extensions import Literal as typing_extensions___Literal

from google.ads.google_ads.v6.proto.common.offline_user_data_pb2 import (
    UserData as google___ads___googleads___v6___common___offline_user_data_pb2___UserData,
)
from google.ads.google_ads.v6.proto.resources.offline_user_data_job_pb2 import (
    OfflineUserDataJob as google___ads___googleads___v6___resources___offline_user_data_job_pb2___OfflineUserDataJob,
)

builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int

DESCRIPTOR: google___protobuf___descriptor___FileDescriptor = ...

class CreateOfflineUserDataJobRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    customer_id: typing___Text = ...
    @property
    def job(
        self,
    ) -> google___ads___googleads___v6___resources___offline_user_data_job_pb2___OfflineUserDataJob: ...
    def __init__(
        self,
        *,
        customer_id: typing___Optional[typing___Text] = None,
        job: typing___Optional[
            google___ads___googleads___v6___resources___offline_user_data_job_pb2___OfflineUserDataJob
        ] = None,
    ) -> None: ...
    def HasField(
        self, field_name: typing_extensions___Literal["job", b"job"]
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "customer_id", b"customer_id", "job", b"job"
        ],
    ) -> None: ...

type___CreateOfflineUserDataJobRequest = CreateOfflineUserDataJobRequest

class CreateOfflineUserDataJobResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    resource_name: typing___Text = ...
    def __init__(
        self, *, resource_name: typing___Optional[typing___Text] = None,
    ) -> None: ...
    def ClearField(
        self, field_name: typing_extensions___Literal["resource_name", b"resource_name"]
    ) -> None: ...

type___CreateOfflineUserDataJobResponse = CreateOfflineUserDataJobResponse

class GetOfflineUserDataJobRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    resource_name: typing___Text = ...
    def __init__(
        self, *, resource_name: typing___Optional[typing___Text] = None,
    ) -> None: ...
    def ClearField(
        self, field_name: typing_extensions___Literal["resource_name", b"resource_name"]
    ) -> None: ...

type___GetOfflineUserDataJobRequest = GetOfflineUserDataJobRequest

class RunOfflineUserDataJobRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    resource_name: typing___Text = ...
    def __init__(
        self, *, resource_name: typing___Optional[typing___Text] = None,
    ) -> None: ...
    def ClearField(
        self, field_name: typing_extensions___Literal["resource_name", b"resource_name"]
    ) -> None: ...

type___RunOfflineUserDataJobRequest = RunOfflineUserDataJobRequest

class AddOfflineUserDataJobOperationsRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    resource_name: typing___Text = ...
    enable_partial_failure: builtin___bool = ...
    @property
    def operations(
        self,
    ) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[
        type___OfflineUserDataJobOperation
    ]: ...
    def __init__(
        self,
        *,
        resource_name: typing___Optional[typing___Text] = None,
        enable_partial_failure: typing___Optional[builtin___bool] = None,
        operations: typing___Optional[
            typing___Iterable[type___OfflineUserDataJobOperation]
        ] = None,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "_enable_partial_failure",
            b"_enable_partial_failure",
            "enable_partial_failure",
            b"enable_partial_failure",
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "_enable_partial_failure",
            b"_enable_partial_failure",
            "enable_partial_failure",
            b"enable_partial_failure",
            "operations",
            b"operations",
            "resource_name",
            b"resource_name",
        ],
    ) -> None: ...
    def WhichOneof(
        self,
        oneof_group: typing_extensions___Literal[
            "_enable_partial_failure", b"_enable_partial_failure"
        ],
    ) -> typing_extensions___Literal["enable_partial_failure"]: ...

type___AddOfflineUserDataJobOperationsRequest = AddOfflineUserDataJobOperationsRequest

class OfflineUserDataJobOperation(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    remove_all: builtin___bool = ...
    @property
    def create(
        self,
    ) -> google___ads___googleads___v6___common___offline_user_data_pb2___UserData: ...
    @property
    def remove(
        self,
    ) -> google___ads___googleads___v6___common___offline_user_data_pb2___UserData: ...
    def __init__(
        self,
        *,
        create: typing___Optional[
            google___ads___googleads___v6___common___offline_user_data_pb2___UserData
        ] = None,
        remove: typing___Optional[
            google___ads___googleads___v6___common___offline_user_data_pb2___UserData
        ] = None,
        remove_all: typing___Optional[builtin___bool] = None,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "create",
            b"create",
            "operation",
            b"operation",
            "remove",
            b"remove",
            "remove_all",
            b"remove_all",
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "create",
            b"create",
            "operation",
            b"operation",
            "remove",
            b"remove",
            "remove_all",
            b"remove_all",
        ],
    ) -> None: ...
    def WhichOneof(
        self, oneof_group: typing_extensions___Literal["operation", b"operation"]
    ) -> typing_extensions___Literal["create", "remove", "remove_all"]: ...

type___OfflineUserDataJobOperation = OfflineUserDataJobOperation

class AddOfflineUserDataJobOperationsResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    @property
    def partial_failure_error(self) -> google___rpc___status_pb2___Status: ...
    def __init__(
        self,
        *,
        partial_failure_error: typing___Optional[
            google___rpc___status_pb2___Status
        ] = None,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "partial_failure_error", b"partial_failure_error"
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "partial_failure_error", b"partial_failure_error"
        ],
    ) -> None: ...

type___AddOfflineUserDataJobOperationsResponse = AddOfflineUserDataJobOperationsResponse
