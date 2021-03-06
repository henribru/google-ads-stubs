# @generated by mypy-protobuf.  Do not edit manually!
import sys
from typing import NewType as typing___NewType, cast as typing___cast

from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    EnumDescriptor as google___protobuf___descriptor___EnumDescriptor,
    FileDescriptor as google___protobuf___descriptor___FileDescriptor,
)
from google.protobuf.internal.enum_type_wrapper import (
    _EnumTypeWrapper as google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper,
)
from google.protobuf.message import Message as google___protobuf___message___Message

builtin___int = int

DESCRIPTOR: google___protobuf___descriptor___FileDescriptor = ...

class BatchJobErrorEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    BatchJobErrorValue = typing___NewType("BatchJobErrorValue", builtin___int)
    type___BatchJobErrorValue = BatchJobErrorValue
    BatchJobError: _BatchJobError
    class _BatchJobError(
        google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[
            BatchJobErrorEnum.BatchJobErrorValue
        ]
    ):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        UNSPECIFIED = typing___cast(BatchJobErrorEnum.BatchJobErrorValue, 0)
        UNKNOWN = typing___cast(BatchJobErrorEnum.BatchJobErrorValue, 1)
        CANNOT_MODIFY_JOB_AFTER_JOB_STARTS_RUNNING = typing___cast(
            BatchJobErrorEnum.BatchJobErrorValue, 2
        )
        EMPTY_OPERATIONS = typing___cast(BatchJobErrorEnum.BatchJobErrorValue, 3)
        INVALID_SEQUENCE_TOKEN = typing___cast(BatchJobErrorEnum.BatchJobErrorValue, 4)
        RESULTS_NOT_READY = typing___cast(BatchJobErrorEnum.BatchJobErrorValue, 5)
        INVALID_PAGE_SIZE = typing___cast(BatchJobErrorEnum.BatchJobErrorValue, 6)
        CAN_ONLY_REMOVE_PENDING_JOB = typing___cast(
            BatchJobErrorEnum.BatchJobErrorValue, 7
        )
    UNSPECIFIED = typing___cast(BatchJobErrorEnum.BatchJobErrorValue, 0)
    UNKNOWN = typing___cast(BatchJobErrorEnum.BatchJobErrorValue, 1)
    CANNOT_MODIFY_JOB_AFTER_JOB_STARTS_RUNNING = typing___cast(
        BatchJobErrorEnum.BatchJobErrorValue, 2
    )
    EMPTY_OPERATIONS = typing___cast(BatchJobErrorEnum.BatchJobErrorValue, 3)
    INVALID_SEQUENCE_TOKEN = typing___cast(BatchJobErrorEnum.BatchJobErrorValue, 4)
    RESULTS_NOT_READY = typing___cast(BatchJobErrorEnum.BatchJobErrorValue, 5)
    INVALID_PAGE_SIZE = typing___cast(BatchJobErrorEnum.BatchJobErrorValue, 6)
    CAN_ONLY_REMOVE_PENDING_JOB = typing___cast(BatchJobErrorEnum.BatchJobErrorValue, 7)
    type___BatchJobError = BatchJobError
    def __init__(self,) -> None: ...

type___BatchJobErrorEnum = BatchJobErrorEnum
