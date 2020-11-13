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

class ResourceChangeOperationEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    ResourceChangeOperationValue = typing___NewType(
        "ResourceChangeOperationValue", builtin___int
    )
    type___ResourceChangeOperationValue = ResourceChangeOperationValue
    ResourceChangeOperation: _ResourceChangeOperation
    class _ResourceChangeOperation(
        google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[
            ResourceChangeOperationEnum.ResourceChangeOperationValue
        ]
    ):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        UNSPECIFIED = typing___cast(
            ResourceChangeOperationEnum.ResourceChangeOperationValue, 0
        )
        UNKNOWN = typing___cast(
            ResourceChangeOperationEnum.ResourceChangeOperationValue, 1
        )
        CREATE = typing___cast(
            ResourceChangeOperationEnum.ResourceChangeOperationValue, 2
        )
        UPDATE = typing___cast(
            ResourceChangeOperationEnum.ResourceChangeOperationValue, 3
        )
        REMOVE = typing___cast(
            ResourceChangeOperationEnum.ResourceChangeOperationValue, 4
        )
    UNSPECIFIED = typing___cast(
        ResourceChangeOperationEnum.ResourceChangeOperationValue, 0
    )
    UNKNOWN = typing___cast(ResourceChangeOperationEnum.ResourceChangeOperationValue, 1)
    CREATE = typing___cast(ResourceChangeOperationEnum.ResourceChangeOperationValue, 2)
    UPDATE = typing___cast(ResourceChangeOperationEnum.ResourceChangeOperationValue, 3)
    REMOVE = typing___cast(ResourceChangeOperationEnum.ResourceChangeOperationValue, 4)
    type___ResourceChangeOperation = ResourceChangeOperation
    def __init__(self,) -> None: ...

type___ResourceChangeOperationEnum = ResourceChangeOperationEnum
