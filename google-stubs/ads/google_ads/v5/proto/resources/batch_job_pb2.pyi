"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.ads.google_ads.v5.proto.enums.batch_job_status_pb2
import google.protobuf.descriptor
import google.protobuf.message
import google.protobuf.wrappers_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class BatchJob(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class BatchJobMetadata(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        CREATION_DATE_TIME_FIELD_NUMBER: builtins.int
        START_DATE_TIME_FIELD_NUMBER: builtins.int
        COMPLETION_DATE_TIME_FIELD_NUMBER: builtins.int
        ESTIMATED_COMPLETION_RATIO_FIELD_NUMBER: builtins.int
        OPERATION_COUNT_FIELD_NUMBER: builtins.int
        EXECUTED_OPERATION_COUNT_FIELD_NUMBER: builtins.int
        start_date_time: typing.Text = ...
        @property
        def creation_date_time(self) -> google.protobuf.wrappers_pb2.StringValue: ...
        @property
        def completion_date_time(self) -> google.protobuf.wrappers_pb2.StringValue: ...
        @property
        def estimated_completion_ratio(
            self,
        ) -> google.protobuf.wrappers_pb2.DoubleValue: ...
        @property
        def operation_count(self) -> google.protobuf.wrappers_pb2.Int64Value: ...
        @property
        def executed_operation_count(
            self,
        ) -> google.protobuf.wrappers_pb2.Int64Value: ...
        def __init__(
            self,
            *,
            creation_date_time: typing.Optional[
                google.protobuf.wrappers_pb2.StringValue
            ] = ...,
            start_date_time: typing.Text = ...,
            completion_date_time: typing.Optional[
                google.protobuf.wrappers_pb2.StringValue
            ] = ...,
            estimated_completion_ratio: typing.Optional[
                google.protobuf.wrappers_pb2.DoubleValue
            ] = ...,
            operation_count: typing.Optional[
                google.protobuf.wrappers_pb2.Int64Value
            ] = ...,
            executed_operation_count: typing.Optional[
                google.protobuf.wrappers_pb2.Int64Value
            ] = ...,
        ) -> None: ...
        def HasField(
            self,
            field_name: typing_extensions.Literal[
                "_start_date_time",
                b"_start_date_time",
                "completion_date_time",
                b"completion_date_time",
                "creation_date_time",
                b"creation_date_time",
                "estimated_completion_ratio",
                b"estimated_completion_ratio",
                "executed_operation_count",
                b"executed_operation_count",
                "operation_count",
                b"operation_count",
                "start_date_time",
                b"start_date_time",
            ],
        ) -> builtins.bool: ...
        def ClearField(
            self,
            field_name: typing_extensions.Literal[
                "_start_date_time",
                b"_start_date_time",
                "completion_date_time",
                b"completion_date_time",
                "creation_date_time",
                b"creation_date_time",
                "estimated_completion_ratio",
                b"estimated_completion_ratio",
                "executed_operation_count",
                b"executed_operation_count",
                "operation_count",
                b"operation_count",
                "start_date_time",
                b"start_date_time",
            ],
        ) -> None: ...
        def WhichOneof(
            self,
            oneof_group: typing_extensions.Literal[
                "_start_date_time", b"_start_date_time"
            ],
        ) -> typing_extensions.Literal["start_date_time"]: ...
    RESOURCE_NAME_FIELD_NUMBER: builtins.int
    ID_FIELD_NUMBER: builtins.int
    NEXT_ADD_SEQUENCE_TOKEN_FIELD_NUMBER: builtins.int
    METADATA_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    LONG_RUNNING_OPERATION_FIELD_NUMBER: builtins.int
    resource_name: typing.Text = ...
    status: google.ads.google_ads.v5.proto.enums.batch_job_status_pb2.BatchJobStatusEnum.BatchJobStatus.V = (
        ...
    )
    @property
    def id(self) -> google.protobuf.wrappers_pb2.Int64Value: ...
    @property
    def next_add_sequence_token(self) -> google.protobuf.wrappers_pb2.StringValue: ...
    @property
    def metadata(self) -> global___BatchJob.BatchJobMetadata: ...
    @property
    def long_running_operation(self) -> google.protobuf.wrappers_pb2.StringValue: ...
    def __init__(
        self,
        *,
        resource_name: typing.Text = ...,
        id: typing.Optional[google.protobuf.wrappers_pb2.Int64Value] = ...,
        next_add_sequence_token: typing.Optional[
            google.protobuf.wrappers_pb2.StringValue
        ] = ...,
        metadata: typing.Optional[global___BatchJob.BatchJobMetadata] = ...,
        status: google.ads.google_ads.v5.proto.enums.batch_job_status_pb2.BatchJobStatusEnum.BatchJobStatus.V = ...,
        long_running_operation: typing.Optional[
            google.protobuf.wrappers_pb2.StringValue
        ] = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "id",
            b"id",
            "long_running_operation",
            b"long_running_operation",
            "metadata",
            b"metadata",
            "next_add_sequence_token",
            b"next_add_sequence_token",
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "id",
            b"id",
            "long_running_operation",
            b"long_running_operation",
            "metadata",
            b"metadata",
            "next_add_sequence_token",
            b"next_add_sequence_token",
            "resource_name",
            b"resource_name",
            "status",
            b"status",
        ],
    ) -> None: ...

global___BatchJob = BatchJob
