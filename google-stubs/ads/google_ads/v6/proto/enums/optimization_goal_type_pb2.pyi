"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class OptimizationGoalTypeEnum(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class _OptimizationGoalType(
        google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[
            OptimizationGoalType.V
        ],
        builtins.type,
    ):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        UNSPECIFIED = OptimizationGoalTypeEnum.OptimizationGoalType.V(0)
        UNKNOWN = OptimizationGoalTypeEnum.OptimizationGoalType.V(1)
        CALL_CLICKS = OptimizationGoalTypeEnum.OptimizationGoalType.V(2)
        DRIVING_DIRECTIONS = OptimizationGoalTypeEnum.OptimizationGoalType.V(3)
    class OptimizationGoalType(metaclass=_OptimizationGoalType):
        V = typing.NewType("V", builtins.int)
    UNSPECIFIED = OptimizationGoalTypeEnum.OptimizationGoalType.V(0)
    UNKNOWN = OptimizationGoalTypeEnum.OptimizationGoalType.V(1)
    CALL_CLICKS = OptimizationGoalTypeEnum.OptimizationGoalType.V(2)
    DRIVING_DIRECTIONS = OptimizationGoalTypeEnum.OptimizationGoalType.V(3)
    def __init__(
        self,
    ) -> None: ...

global___OptimizationGoalTypeEnum = OptimizationGoalTypeEnum
