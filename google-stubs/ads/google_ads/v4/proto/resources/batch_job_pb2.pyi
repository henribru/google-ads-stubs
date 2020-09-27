# @generated by mypy-protobuf.  Do not edit manually!
import sys
from typing import Optional as typing___Optional, Text as typing___Text

from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    FileDescriptor as google___protobuf___descriptor___FileDescriptor,
)
from google.protobuf.message import Message as google___protobuf___message___Message
from google.protobuf.wrappers_pb2 import (
    DoubleValue as google___protobuf___wrappers_pb2___DoubleValue,
    Int64Value as google___protobuf___wrappers_pb2___Int64Value,
    StringValue as google___protobuf___wrappers_pb2___StringValue,
)
from typing_extensions import Literal as typing_extensions___Literal

from google.ads.google_ads.v4.proto.enums.batch_job_status_pb2 import (
    BatchJobStatusEnum as google___ads___googleads___v4___enums___batch_job_status_pb2___BatchJobStatusEnum,
)

builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int

DESCRIPTOR: google___protobuf___descriptor___FileDescriptor = ...

class BatchJob(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class BatchJobMetadata(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        @property
        def creation_date_time(
            self,
        ) -> google___protobuf___wrappers_pb2___StringValue: ...
        @property
        def completion_date_time(
            self,
        ) -> google___protobuf___wrappers_pb2___StringValue: ...
        @property
        def estimated_completion_ratio(
            self,
        ) -> google___protobuf___wrappers_pb2___DoubleValue: ...
        @property
        def operation_count(self) -> google___protobuf___wrappers_pb2___Int64Value: ...
        @property
        def executed_operation_count(
            self,
        ) -> google___protobuf___wrappers_pb2___Int64Value: ...
        def __init__(
            self,
            *,
            creation_date_time: typing___Optional[
                google___protobuf___wrappers_pb2___StringValue
            ] = None,
            completion_date_time: typing___Optional[
                google___protobuf___wrappers_pb2___StringValue
            ] = None,
            estimated_completion_ratio: typing___Optional[
                google___protobuf___wrappers_pb2___DoubleValue
            ] = None,
            operation_count: typing___Optional[
                google___protobuf___wrappers_pb2___Int64Value
            ] = None,
            executed_operation_count: typing___Optional[
                google___protobuf___wrappers_pb2___Int64Value
            ] = None,
        ) -> None: ...
        def HasField(
            self,
            field_name: typing_extensions___Literal[
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
            ],
        ) -> builtin___bool: ...
        def ClearField(
            self,
            field_name: typing_extensions___Literal[
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
            ],
        ) -> None: ...
    type___BatchJobMetadata = BatchJobMetadata

    resource_name: typing___Text = ...
    status: google___ads___googleads___v4___enums___batch_job_status_pb2___BatchJobStatusEnum.BatchJobStatusValue = ...
    @property
    def id(self) -> google___protobuf___wrappers_pb2___Int64Value: ...
    @property
    def next_add_sequence_token(
        self,
    ) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def metadata(self) -> type___BatchJob.BatchJobMetadata: ...
    @property
    def long_running_operation(
        self,
    ) -> google___protobuf___wrappers_pb2___StringValue: ...
    def __init__(
        self,
        *,
        resource_name: typing___Optional[typing___Text] = None,
        id: typing___Optional[google___protobuf___wrappers_pb2___Int64Value] = None,
        next_add_sequence_token: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        metadata: typing___Optional[type___BatchJob.BatchJobMetadata] = None,
        status: typing___Optional[
            google___ads___googleads___v4___enums___batch_job_status_pb2___BatchJobStatusEnum.BatchJobStatusValue
        ] = None,
        long_running_operation: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "id",
            b"id",
            "long_running_operation",
            b"long_running_operation",
            "metadata",
            b"metadata",
            "next_add_sequence_token",
            b"next_add_sequence_token",
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
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

type___BatchJob = BatchJob