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

class WebpageConditionOperandEnum(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class _WebpageConditionOperand(
        google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[
            WebpageConditionOperand.V
        ],
        builtins.type,
    ):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        UNSPECIFIED = WebpageConditionOperandEnum.WebpageConditionOperand.V(0)
        UNKNOWN = WebpageConditionOperandEnum.WebpageConditionOperand.V(1)
        URL = WebpageConditionOperandEnum.WebpageConditionOperand.V(2)
        CATEGORY = WebpageConditionOperandEnum.WebpageConditionOperand.V(3)
        PAGE_TITLE = WebpageConditionOperandEnum.WebpageConditionOperand.V(4)
        PAGE_CONTENT = WebpageConditionOperandEnum.WebpageConditionOperand.V(5)
        CUSTOM_LABEL = WebpageConditionOperandEnum.WebpageConditionOperand.V(6)
    class WebpageConditionOperand(metaclass=_WebpageConditionOperand):
        V = typing.NewType("V", builtins.int)
    UNSPECIFIED = WebpageConditionOperandEnum.WebpageConditionOperand.V(0)
    UNKNOWN = WebpageConditionOperandEnum.WebpageConditionOperand.V(1)
    URL = WebpageConditionOperandEnum.WebpageConditionOperand.V(2)
    CATEGORY = WebpageConditionOperandEnum.WebpageConditionOperand.V(3)
    PAGE_TITLE = WebpageConditionOperandEnum.WebpageConditionOperand.V(4)
    PAGE_CONTENT = WebpageConditionOperandEnum.WebpageConditionOperand.V(5)
    CUSTOM_LABEL = WebpageConditionOperandEnum.WebpageConditionOperand.V(6)
    def __init__(
        self,
    ) -> None: ...

global___WebpageConditionOperandEnum = WebpageConditionOperandEnum
